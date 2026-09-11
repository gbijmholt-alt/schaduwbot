# Wallet-analyse pump.fun — 2026-09-11 19:42 UTC

## Kort antwoord

- Geluk-toets: 34 van 3978 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=10.55, geluk-grens 5.0).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.2% per positie (alle wallets: -14.1%; 14 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.9%, 2 s: -15.5%, 10 s: -16.3%, 60 s: -19.8% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 19:41 UTC (29.9 uur), helft A/B-grens: 2026-09-11 04:45 UTC
- 2226699 trades, 15658 tokens, 123108 wallets, 703882 posities (523618 geopend vanaf ≥ $7k, 180264 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 69069
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 6827 | 4640 | +9.20 | -29.71 | +422.53 | 20155.42 | 5443 | +782.44 |
| swing | 633 | 7037 | -278.34 | -380.36 | -179.29 | 31.75 | 2283 | -3.69 |
| dev | 940 | 3258 | +514.96 | -471.47 | +503.65 | 4116.05 | 3877 | +301.84 |
| bot_hf | 2064 | 112200 | -71.35 | -1101.86 | +1924.47 | 8237.22 | 64933 | +2961.57 |
| incidenteel | 96187 | 143797 | -5532.72 | -9143.11 | +6127.37 | 6714.61 | 55414 | +3317.83 |
| scalper | 16457 | 252686 | -7536.36 | -9284.05 | +10837.02 | 6634.39 | 48314 | +309.74 |

Wallets met ≥ 10 posities: 9055, waarvan winstgevend: 21%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -12894.61 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 2974 (41) | 44% | +4.35 | +3.13 | +0% | 18.87 | ja | 21 s | +0.94 / +3.41 |
| 2 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 3437 (27) | 38% | +3.98 | +2.98 | +1% | 18.15 | ja | 19 s | +2.06 / +1.92 |
| 3 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 1640 (7) | 63% | +3.61 | +3.52 | +8% | 16.78 | ja | 4 s | +1.86 / +1.75 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1207 (25) | 59% | +2.75 | +2.60 | +6% | 13.47 | ja | 4 s | +1.74 / +1.01 |
| 5 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 772 (21) | 43% | +1.70 | +1.28 | +2% | 11.29 | ja | 61 s | +0.77 / +0.93 |
| 6 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 31 (0) | 74% | +18.91 | +16.93 | +70% | 10.38 | ja | 77 s | +13.47 / +5.44 |
| 7 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1041 (4) | 55% | +0.54 | +0.45 | +1% | 10.23 | ja | 10 s | +0.05 / +0.49 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 294 (1) | 60% | +6.26 | +5.43 | +8% | 10.08 | ja | 1 s | +1.97 / +4.29 |
| 9 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 46 (0) | 54% | +16.31 | +12.69 | +55% | 9.9 | ja | 20 s | +14.04 / +2.27 |
| 10 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 527 (3) | 44% | +6.87 | +5.83 | +4% | 9.59 | ja | 28 s | +4.48 / +2.39 |
| 11 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 2040 (15) | 63% | +0.33 | +0.31 | +3% | 9.16 | nee | 4 s | +0.17 / +0.16 |
| 12 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 909 (11) | 51% | +1.53 | +1.47 | +10% | 8.83 | nee | 4 s | +0.88 / +0.65 |
| 13 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 621 (24) | 46% | +7.05 | +5.71 | +3% | 8.59 | nee | 2 min | +5.40 / +1.65 |
| 14 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 228 (11) | 52% | +0.68 | +0.58 | +8% | 8.58 | ja | 7 s | +0.44 / +0.25 |
| 15 | [5Vox…UA6U](https://solscan.io/account/5Voxqwa8y9KRJNY71mrKHHs5MEVwuVVdySCJExrrUA6U) | bot_hf | 132 (4) | 55% | +3.09 | +0.98 | +6% | 8.52 | ja | 15 s | +0.11 / +2.98 |
| 16 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 421 (5) | 69% | +2.55 | +2.31 | +2% | 8.39 | ja | 11 s | +1.81 / +0.75 |
| 17 | [3H7x…Reso](https://solscan.io/account/3H7xDiUm8MEb144KuUvRVaTL43LJVHwLAZTqLL5jReso) | scalper | 30 (0) | 57% | +12.95 | +10.90 | +47% | 8.09 | ja | 67 s | +8.92 / +4.03 |
| 18 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 31 (0) | 64% | +12.80 | +10.79 | +46% | 8.06 | ja | 70 s | +7.88 / +4.92 |
| 19 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 399 (6) | 70% | +2.50 | +2.23 | +2% | 7.92 | nee | 11 s | +2.48 / +0.02 |
| 20 | [6rH3…try1](https://solscan.io/account/6rH3c2DLQvd8CSNVF4geb6GLWYPBSeTqepALSfKbtry1) | bot_hf | 306 (1) | 56% | +2.23 | +2.03 | +4% | 7.9 | ja | 3 s | +1.64 / +0.59 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.18 | nee | 13 s | +0.00 / +206.40 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 32 (0) | 75% | +203.49 | +187.99 | +76% | 8.29 | ja | 8 s | -0.81 / +204.29 |
| 3 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 132 (0) | 63% | +49.06 | +43.70 | +11% | 6.22 | nee | 15 s | +23.75 / +25.31 |
| 4 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 105 (1) | 75% | +35.32 | +31.72 | +14% | 6.1 | nee | 9 s | +21.39 / +13.93 |
| 5 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 102 (5) | 54% | +31.47 | +24.27 | +14% | 5.82 | nee | 94 s | +31.17 / +0.30 |
| 6 | [9NgH…w6pz](https://solscan.io/account/9NgHs3A8F2cnM2w6kWsMp8AGAeyQyJckQ2unJvmiw6pz) | bot_hf | 117 (0) | 60% | +23.71 | +20.86 | +6% | 4.55 | nee | 8 s | +7.62 / +16.09 |
| 7 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 21 (1) | 71% | +23.65 | +17.48 | +56% | 7.34 | ja | 80 s | +10.06 / +13.59 |
| 8 | [FKdm…kemf](https://solscan.io/account/FKdmT4MqPVTbDw2B3nncXhBjrUgmUE2vhQGMzb7fkemf) | vroege_houder | 13 (0) | 62% | +23.15 | +14.79 | +23% | 2.63 | nee | 29 s | -2.96 / +26.11 |
| 9 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 8 (0) | 88% | +22.48 | +15.45 | +30% | 2.89 | nee | 67 s | +20.58 / +1.90 |
| 10 | [2CHr…NE71](https://solscan.io/account/2CHrnc2LyagAbMaMFgthiDWh7ZZ9zT9TF8WEJf7MNE71) | scalper | 13 (0) | 77% | +22.10 | +17.78 | +47% | 4.17 | nee | 18 s | +6.80 / +15.30 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | vroege_houder | 41 (3) | 93% | +22.00 | +19.99 | +18% | 3.85 | nee | 19 s | +12.74 / +9.26 |
| 12 | [FM1Y…Jgke](https://solscan.io/account/FM1YCKED2KaqB8Uat8aB1nsffR1vezr7s6FAEieXJgke) | scalper | 6 (1) | 17% | +20.83 | -3.01 | +61% | -0.22 | nee | 8 min | +21.46 / -0.62 |
| 13 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 51 (0) | 78% | +20.76 | +18.43 | +12% | 4.25 | nee | 24 s | +13.32 / +7.44 |
| 14 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 73 (11) | 47% | +20.21 | +15.41 | +10% | 4.3 | nee | 104 s | +15.19 / +5.03 |
| 15 | [B92U…ApaF](https://solscan.io/account/B92UBzhsvMu8xw4mwnPzuaDEWiy2WoLjwmyj3aUUApaF) | bot_hf | 11 (0) | 73% | +20.13 | +9.14 | +28% | 2.76 | nee | 5 s | +13.13 / +7.00 |
| 16 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 34 (0) | 68% | +19.66 | +15.73 | +12% | 3.43 | nee | 34 s | +10.08 / +9.58 |
| 17 | [Dd2n…KanL](https://solscan.io/account/Dd2nB2vD1XvDsdKqhtmCuh1q6tzWckkqLq3JubznKanL) | scalper | 50 (3) | 60% | +19.52 | +16.81 | +12% | 4.23 | nee | 19 s | +13.00 / +6.53 |
| 18 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 31 (0) | 74% | +18.91 | +16.93 | +70% | 10.38 | ja | 77 s | +13.47 / +5.44 |
| 19 | [K6Eh…KHnR](https://solscan.io/account/K6Eh9fwKkrhVNq6SpRtJn7F4Myi3HUst5QP8x5BKHnR) | dev | 168 (6) | 40% | +18.05 | +10.01 | +5% | 4.97 | nee | 15 s | +0.20 / +17.85 |
| 20 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 7 (0) | 57% | +17.52 | +2.96 | +72% | 4.11 | nee | 13 s | +15.61 / +1.91 |

## Geluk-toets

Populatie: 3978 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 10.55 | 4.16 | 5.0 |
| #10 | 7.75 | 3.12 | 3.32 |
| #20 | 6.29 | 2.82 | 2.97 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.0): **34**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 6043 | 49% | +5.2% | -0.1% | +56.27 |
| top 20 op winst (A) | 18/20 | 506 | 54% | +6.3% | +2.0% | +83.31 |
| alle wallets | – | 211574 | 30% | -14.1% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.2% / +2.3% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 1682): ρ = 0.453. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 76

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6043 | 29% | -12.9% | -7.8% | -155.97 |
| 2 s | 6043 | 24% | -15.5% | -9.6% | -187.79 |
| 10 s | 6043 | 23% | -16.3% | -9.7% | -196.52 |
| 60 s | 6043 | 20% | -19.8% | -8.5% | -239.03 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 178

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 17086 | 30% | -15.8% | -9.8% | -539.09 |
| 2 s | 17086 | 24% | -19.0% | -12.4% | -650.54 |
| 10 s | 17086 | 21% | -20.5% | -12.4% | -701.79 |
| 60 s | 17086 | 16% | -26.2% | -12.0% | -895.06 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 19

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 1021 | 40% | +4.3% | -4.8% | +8.77 |
| 2 s | 1021 | 26% | -8.4% | -10.6% | -17.10 |
| 10 s | 1021 | 25% | -8.3% | -8.2% | -16.96 |
| 60 s | 1021 | 17% | -9.2% | -5.8% | -18.84 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
