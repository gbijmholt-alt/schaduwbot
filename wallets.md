# Wallet-analyse pump.fun — 2026-09-11 18:40 UTC

## Kort antwoord

- Geluk-toets: 29 van 3801 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=10.27, geluk-grens 5.09).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.1% per positie (alle wallets: -14.0%; 12 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.9%, 2 s: -16.8%, 10 s: -17.7%, 60 s: -21.1% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 18:39 UTC (28.9 uur), helft A/B-grens: 2026-09-11 04:13 UTC
- 2080675 trades, 14217 tokens, 118282 wallets, 660793 posities (500309 geopend vanaf ≥ $7k, 160484 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 65858
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 6792 | 4662 | -16.71 | -53.34 | +392.68 | 20250.26 | 4936 | +647.32 |
| swing | 626 | 6732 | -268.65 | -370.34 | -170.81 | 31.06 | 2090 | -2.86 |
| dev | 903 | 2942 | +462.12 | -463.74 | +473.07 | 4096.59 | 3237 | +238.85 |
| bot_hf | 1996 | 108183 | -134.79 | -1110.21 | +1968.72 | 7703.41 | 56043 | +2393.06 |
| scalper | 15680 | 239407 | -7111.99 | -8810.61 | +9777.03 | 6633.72 | 43277 | +235.00 |
| incidenteel | 92285 | 138383 | -5461.43 | -9051.00 | +5972.00 | 6734.46 | 50901 | +2797.07 |

Wallets met ≥ 10 posities: 8716, waarvan winstgevend: 22%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -12531.45 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 2882 (37) | 44% | +3.83 | +2.61 | +0% | 18.53 | ja | 21 s | +1.34 / +2.49 |
| 2 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 3409 (27) | 38% | +4.49 | +3.49 | +1% | 18.03 | ja | 19 s | +2.40 / +2.10 |
| 3 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 1577 (7) | 63% | +3.20 | +3.11 | +8% | 16.5 | ja | 4 s | +1.76 / +1.44 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1164 (25) | 58% | +2.60 | +2.46 | +6% | 12.73 | ja | 4 s | +1.57 / +1.03 |
| 5 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 742 (21) | 43% | +1.42 | +1.00 | +2% | 10.85 | ja | 61 s | +0.82 / +0.60 |
| 6 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 31 (0) | 74% | +18.91 | +16.93 | +70% | 10.38 | ja | 77 s | +13.47 / +5.44 |
| 7 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1004 (4) | 54% | +0.42 | +0.33 | +1% | 9.85 | nee | 10 s | +0.07 / +0.35 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 277 (1) | 61% | +6.08 | +5.25 | +8% | 9.83 | ja | 1 s | +2.01 / +4.07 |
| 9 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 45 (0) | 53% | +13.76 | +10.14 | +49% | 9.37 | ja | 20 s | +13.41 / +0.36 |
| 10 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 2040 (15) | 63% | +0.33 | +0.31 | +3% | 9.16 | nee | 4 s | +0.17 / +0.17 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 501 (3) | 44% | +6.08 | +5.04 | +4% | 9.06 | ja | 29 s | +4.59 / +1.50 |
| 12 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 600 (21) | 46% | +7.72 | +6.39 | +3% | 8.61 | nee | 2 min | +4.91 / +2.81 |
| 13 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 473 (2) | 49% | +3.83 | +3.46 | +3% | 8.47 | nee | 70 s | +3.56 / +0.28 |
| 14 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 864 (9) | 51% | +1.43 | +1.37 | +10% | 8.36 | nee | 4 s | +0.84 / +0.59 |
| 15 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 407 (5) | 69% | +2.39 | +2.14 | +2% | 8.27 | nee | 11 s | +1.71 / +0.68 |
| 16 | [3H7x…Reso](https://solscan.io/account/3H7xDiUm8MEb144KuUvRVaTL43LJVHwLAZTqLL5jReso) | scalper | 30 (0) | 57% | +12.95 | +10.90 | +47% | 8.08 | ja | 67 s | +8.92 / +4.03 |
| 17 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 31 (0) | 64% | +12.80 | +10.79 | +46% | 8.06 | ja | 70 s | +7.88 / +4.92 |
| 18 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 178 (9) | 53% | +0.72 | +0.62 | +10% | 7.81 | ja | 7 s | +0.47 / +0.25 |
| 19 | [6rH3…try1](https://solscan.io/account/6rH3c2DLQvd8CSNVF4geb6GLWYPBSeTqepALSfKbtry1) | bot_hf | 277 (1) | 55% | +1.88 | +1.68 | +3% | 7.4 | nee | 3 s | +1.59 / +0.29 |
| 20 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 21 (1) | 71% | +23.65 | +17.48 | +56% | 7.34 | ja | 80 s | +10.06 / +13.59 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.17 | nee | 13 s | +0.00 / +206.40 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 21 (0) | 71% | +124.83 | +109.34 | +81% | 6.69 | ja | 9 s | -0.81 / +125.64 |
| 3 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 129 (0) | 64% | +48.76 | +43.40 | +11% | 6.12 | nee | 15 s | +23.75 / +25.00 |
| 4 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 102 (5) | 54% | +31.47 | +24.27 | +14% | 5.82 | nee | 94 s | +31.17 / +0.30 |
| 5 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 99 (1) | 76% | +31.04 | +27.43 | +13% | 5.8 | nee | 9 s | +20.22 / +10.82 |
| 6 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 21 (1) | 71% | +23.65 | +17.48 | +56% | 7.34 | ja | 80 s | +10.06 / +13.59 |
| 7 | [FKdm…kemf](https://solscan.io/account/FKdmT4MqPVTbDw2B3nncXhBjrUgmUE2vhQGMzb7fkemf) | vroege_houder | 13 (0) | 62% | +23.15 | +14.79 | +23% | 2.63 | nee | 29 s | -4.42 / +27.57 |
| 8 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 8 (0) | 88% | +22.48 | +15.45 | +30% | 2.86 | nee | 67 s | +20.58 / +1.90 |
| 9 | [2CHr…NE71](https://solscan.io/account/2CHrnc2LyagAbMaMFgthiDWh7ZZ9zT9TF8WEJf7MNE71) | scalper | 13 (0) | 77% | +22.10 | +17.78 | +47% | 4.16 | nee | 18 s | +6.80 / +15.30 |
| 10 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | vroege_houder | 41 (3) | 93% | +22.00 | +19.99 | +18% | 3.83 | nee | 19 s | +12.61 / +9.38 |
| 11 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 70 (10) | 49% | +21.00 | +16.20 | +11% | 4.28 | nee | 104 s | +15.20 / +5.81 |
| 12 | [FM1Y…Jgke](https://solscan.io/account/FM1YCKED2KaqB8Uat8aB1nsffR1vezr7s6FAEieXJgke) | dev | 5 (0) | 20% | +20.83 | -3.01 | +63% | -0.26 | nee | 8 min | +21.46 / -0.62 |
| 13 | [Dd2n…KanL](https://solscan.io/account/Dd2nB2vD1XvDsdKqhtmCuh1q6tzWckkqLq3JubznKanL) | vroege_houder | 46 (2) | 61% | +19.71 | +17.00 | +13% | 4.19 | nee | 20 s | +12.71 / +7.00 |
| 14 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 49 (0) | 78% | +19.61 | +17.28 | +12% | 4.13 | nee | 24 s | +13.32 / +6.29 |
| 15 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 31 (0) | 74% | +18.91 | +16.93 | +70% | 10.38 | ja | 77 s | +13.47 / +5.44 |
| 16 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 33 (0) | 67% | +18.60 | +14.68 | +12% | 3.28 | nee | 37 s | +8.90 / +9.70 |
| 17 | [K6Eh…KHnR](https://solscan.io/account/K6Eh9fwKkrhVNq6SpRtJn7F4Myi3HUst5QP8x5BKHnR) | dev | 168 (6) | 40% | +18.05 | +10.01 | +5% | 4.93 | nee | 15 s | -0.35 / +18.40 |
| 18 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 7 (0) | 57% | +17.52 | +2.96 | +72% | 4.11 | nee | 13 s | +1.05 / +16.46 |
| 19 | [7kDp…Y1sC](https://solscan.io/account/7kDpxMJDNvPXhdd4XSQfgmYPGo5asd9eHf2gLGDZY1sC) | scalper | 11 (0) | 73% | +17.30 | +12.58 | +20% | 2.94 | nee | 25 s | +17.30 / +0.00 |
| 20 | [75Hc…g74J](https://solscan.io/account/75Hc8hVYZuCnSEN4kNbK4BbWi3kogjirBfjTWgKMg74J) | dev | 11 (0) | 27% | +17.01 | -69.58 | +7% | -0.07 | nee | 20 s | +0.00 / +17.01 |

## Geluk-toets

Populatie: 3801 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 10.27 | 4.33 | 5.09 |
| #10 | 7.51 | 3.14 | 3.33 |
| #20 | 5.93 | 2.83 | 2.98 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.09): **29**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 5545 | 49% | +5.1% | -0.2% | +40.90 |
| top 20 op winst (A) | 18/20 | 370 | 59% | +12.2% | +3.6% | +97.22 |
| alle wallets | – | 194055 | 30% | -14.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.0% / +1.8% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 1578): ρ = 0.456. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 63

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 5545 | 28% | -13.9% | -8.2% | -154.60 |
| 2 s | 5545 | 24% | -16.8% | -10.0% | -186.21 |
| 10 s | 5545 | 22% | -17.7% | -10.2% | -196.52 |
| 60 s | 5545 | 20% | -21.1% | -9.0% | -233.93 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 162

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 16553 | 29% | -15.9% | -10.0% | -525.99 |
| 2 s | 16553 | 24% | -19.3% | -12.6% | -638.40 |
| 10 s | 16553 | 21% | -21.0% | -12.8% | -695.70 |
| 60 s | 16553 | 17% | -26.4% | -12.4% | -872.31 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 18

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 884 | 39% | +4.3% | -5.0% | +7.54 |
| 2 s | 884 | 26% | -8.4% | -10.9% | -14.89 |
| 10 s | 884 | 25% | -8.3% | -8.7% | -14.60 |
| 60 s | 884 | 18% | -9.0% | -6.2% | -15.98 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
