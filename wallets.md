# Wallet-analyse pump.fun — 2026-09-11 14:03 UTC

## Kort antwoord

- Geluk-toets: 20 van 2953 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=9.52, geluk-grens 5.05).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +4.3% per positie (alle wallets: -11.8%; 7 van 13 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.6%, 2 s: -15.9%, 10 s: -17.0%, 60 s: -19.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 14:03 UTC (24.2 uur), helft A/B-grens: 2026-09-11 01:55 UTC
- 1453102 trades, 8342 tokens, 94951 wallets, 475850 posities (409300 geopend vanaf ≥ $7k, 66550 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 56065
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 6254 | 4251 | -57.98 | -83.19 | +271.85 | 20668.40 | 2504 | +267.80 |
| swing | 483 | 5214 | -200.99 | -278.32 | -133.69 | 30.13 | 793 | -0.33 |
| dev | 702 | 2373 | -37.55 | -793.90 | -203.56 | 3854.10 | 1427 | +41.52 |
| bot_hf | 1806 | 88822 | -177.80 | -1109.77 | +1512.64 | 6591.08 | 22755 | +527.99 |
| scalper | 13416 | 193894 | -5593.38 | -7060.92 | +5787.18 | 6387.81 | 16867 | +26.50 |
| incidenteel | 72290 | 114746 | -4403.02 | -7865.76 | +5462.74 | 6410.63 | 22204 | +999.98 |

Wallets met ≥ 10 posities: 7319, waarvan winstgevend: 23%. De top 1% winnaars pakt 32% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -10470.73 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 2964 (25) | 38% | +4.12 | +3.12 | +1% | 16.42 | ja | 19 s | +2.20 / +1.93 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 1288 (5) | 63% | +2.58 | +2.51 | +8% | 15.22 | ja | 4 s | +1.42 / +1.16 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 935 (19) | 58% | +2.11 | +1.96 | +6% | 11.99 | ja | 4 s | +1.32 / +0.79 |
| 4 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 1818 (15) | 63% | +0.27 | +0.25 | +2% | 8.43 | nee | 4 s | +0.16 / +0.11 |
| 5 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 41 (0) | 54% | +13.51 | +9.89 | +49% | 8.41 | ja | 20 s | +9.91 / +3.59 |
| 6 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 403 (3) | 45% | +5.53 | +4.49 | +4% | 8.19 | nee | 30 s | +3.53 / +2.00 |
| 7 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 802 (4) | 52% | +0.26 | +0.18 | +1% | 8.12 | nee | 10 s | +0.20 / +0.06 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 200 (1) | 60% | +4.34 | +3.51 | +8% | 8.0 | ja | 1 s | +1.29 / +3.05 |
| 9 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 412 (1) | 49% | +3.65 | +3.29 | +3% | 7.77 | nee | 70 s | +3.19 / +0.47 |
| 10 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 346 (5) | 68% | +2.68 | +2.44 | +3% | 7.76 | nee | 12 s | +1.46 / +1.22 |
| 11 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 328 (6) | 71% | +3.27 | +3.00 | +3% | 7.74 | nee | 11 s | +2.42 / +0.85 |
| 12 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 527 (18) | 46% | +7.35 | +6.01 | +3% | 7.73 | nee | 2 min | +5.34 / +2.01 |
| 13 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 658 (9) | 49% | +0.97 | +0.92 | +9% | 7.35 | nee | 4 s | +0.77 / +0.20 |
| 14 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 234 (0) | 47% | +1.65 | +0.89 | +2% | 6.92 | nee | 0 s | +0.35 / +1.30 |
| 15 | [4wbr…gpVq](https://solscan.io/account/4wbrLxXe4pwZe1u4g56BcKBN8uWi8xNoqwwN5tktgpVq) | scalper | 285 (2) | 57% | +1.01 | +0.94 | +5% | 6.6 | nee | 60 s | +0.79 / +0.22 |
| 16 | [DQiE…sbQh](https://solscan.io/account/DQiEUHLVWCQAmLE9T2LauNb9o7LniUQNFt3XabYesbQh) | scalper | 309 (2) | 41% | +0.22 | +0.03 | +1% | 6.34 | nee | 78 s | +0.04 / +0.18 |
| 17 | [6rH3…try1](https://solscan.io/account/6rH3c2DLQvd8CSNVF4geb6GLWYPBSeTqepALSfKbtry1) | bot_hf | 198 (0) | 55% | +1.82 | +1.63 | +5% | 6.27 | nee | 3 s | +1.14 / +0.68 |
| 18 | [F6XJ…Youk](https://solscan.io/account/F6XJTh93VGFcbnf2FJmyR6f3y2HZsav25EeEaZosYouk) | scalper | 329 (0) | 50% | +3.19 | +2.60 | +2% | 6.25 | nee | 18 s | +2.35 / +0.84 |
| 19 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | scalper | 64 (0) | 48% | +18.76 | +15.50 | +23% | 6.25 | ja | 17 s | +12.96 / +5.80 |
| 20 | [4WxE…dzhP](https://solscan.io/account/4WxE3GAiFG6EofdSF4N3DWXg5na9V3BQJJN5LuE5dzhP) | scalper | 328 (0) | 51% | +4.56 | +4.07 | +2% | 6.17 | nee | 18 s | +3.51 / +1.05 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 110 (0) | 62% | +38.70 | +33.33 | +11% | 5.47 | nee | 15 s | +21.98 / +16.72 |
| 2 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 87 (5) | 54% | +31.48 | +24.28 | +16% | 5.57 | nee | 88 s | +31.17 / +0.31 |
| 3 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 83 (1) | 82% | +27.70 | +25.55 | +14% | 5.54 | nee | 9 s | +19.57 / +8.12 |
| 4 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | vroege_houder | 6 (0) | 100% | +22.18 | +15.15 | +40% | 3.0 | nee | 67 s | +13.89 / +8.28 |
| 5 | [FM1Y…Jgke](https://solscan.io/account/FM1YCKED2KaqB8Uat8aB1nsffR1vezr7s6FAEieXJgke) | dev | 5 (0) | 20% | +20.83 | -3.01 | +63% | -0.27 | nee | 8 min | +21.46 / -0.62 |
| 6 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | scalper | 64 (0) | 48% | +18.76 | +15.50 | +23% | 6.25 | ja | 17 s | +12.96 / +5.80 |
| 7 | [Dd2n…KanL](https://solscan.io/account/Dd2nB2vD1XvDsdKqhtmCuh1q6tzWckkqLq3JubznKanL) | vroege_houder | 40 (2) | 62% | +17.90 | +15.19 | +14% | 3.98 | nee | 20 s | +11.00 / +6.90 |
| 8 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 7 (0) | 57% | +17.52 | +2.96 | +72% | 4.14 | nee | 13 s | +1.05 / +16.46 |
| 9 | [7kDp…Y1sC](https://solscan.io/account/7kDpxMJDNvPXhdd4XSQfgmYPGo5asd9eHf2gLGDZY1sC) | scalper | 11 (0) | 73% | +17.30 | +12.58 | +20% | 2.96 | nee | 25 s | +17.30 / +0.00 |
| 10 | [75Hc…g74J](https://solscan.io/account/75Hc8hVYZuCnSEN4kNbK4BbWi3kogjirBfjTWgKMg74J) | dev | 11 (0) | 27% | +17.01 | -69.58 | +7% | -0.07 | nee | 20 s | +0.00 / +17.01 |
| 11 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 31 (0) | 64% | +15.84 | +11.91 | +11% | 3.04 | nee | 37 s | +1.77 / +14.06 |
| 12 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 56 (8) | 46% | +15.32 | +10.52 | +10% | 3.55 | nee | 116 s | +17.08 / -1.76 |
| 13 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 38 (0) | 74% | +14.67 | +12.34 | +11% | 3.47 | nee | 20 s | +10.45 / +4.22 |
| 14 | [2KP9…PURD](https://solscan.io/account/2KP9miexioqgNbjPwysggcbi3sKqhH8JsPaDmFxRPURD) | bot_hf | 14 (0) | 71% | +14.56 | +9.46 | +23% | 3.33 | nee | 9 s | +13.97 / +0.59 |
| 15 | [H8UK…FzHm](https://solscan.io/account/H8UKNvUeaqpVT7DZ8TXJVreSQEXDjTA7fEv8hjD3FzHm) | bot_hf | 10 (0) | 80% | +14.56 | +6.88 | +32% | 2.96 | nee | 15 s | +9.62 / +4.93 |
| 16 | [3PwX…pdvA](https://solscan.io/account/3PwXa9BRA2sUdjtcGxs4bVLBau2dHTuZwtb6CbpTpdvA) | scalper | 38 (1) | 55% | +14.31 | +9.72 | +31% | 4.31 | nee | 2 min | +11.19 / +3.12 |
| 17 | [FNvL…x4bs](https://solscan.io/account/FNvLdMfo2aB9xf14x4TFN3dr2TDpKz78Rji1k8bTx4bs) | vroege_houder | 90 (3) | 53% | +13.99 | +8.89 | +5% | 4.21 | nee | 3 min | +10.98 / +3.02 |
| 18 | [2CHr…NE71](https://solscan.io/account/2CHrnc2LyagAbMaMFgthiDWh7ZZ9zT9TF8WEJf7MNE71) | scalper | 9 (0) | 78% | +13.59 | +10.72 | +43% | 3.15 | nee | 18 s | +6.80 / +6.79 |
| 19 | [5L7a…aBUD](https://solscan.io/account/5L7aqweEkQWzogyyqi1xs2oU2ePseSXQnpnxYrg2aBUD) | bot_hf | 14 (0) | 64% | +13.55 | +8.90 | +22% | 2.8 | nee | 15 s | +3.34 / +10.21 |
| 20 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 41 (0) | 54% | +13.51 | +9.89 | +49% | 8.41 | ja | 20 s | +9.91 / +3.59 |

## Geluk-toets

Populatie: 2953 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 9.52 | 4.14 | 5.05 |
| #10 | 5.91 | 3.04 | 3.27 |
| #20 | 5.12 | 2.73 | 2.87 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.05): **20**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 13/20 | 4532 | 49% | +4.3% | +0.0% | +17.80 |
| top 20 op winst (A) | 15/20 | 251 | 54% | +9.8% | +2.1% | +51.11 |
| alle wallets | – | 136130 | 31% | -11.8% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -4.3% / +3.0% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 1093): ρ = 0.471. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 58

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 4532 | 28% | -13.6% | -7.7% | -122.82 |
| 2 s | 4532 | 23% | -15.9% | -9.6% | -144.13 |
| 10 s | 4532 | 22% | -17.0% | -9.7% | -154.11 |
| 60 s | 4532 | 20% | -19.6% | -8.6% | -177.35 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 95

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 12469 | 30% | -17.1% | -11.3% | -427.07 |
| 2 s | 12469 | 24% | -20.3% | -13.9% | -505.56 |
| 10 s | 12469 | 20% | -22.4% | -14.5% | -557.32 |
| 60 s | 12469 | 16% | -28.3% | -14.2% | -706.56 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 15

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 765 | 38% | +4.0% | -4.8% | +6.07 |
| 2 s | 765 | 28% | -5.3% | -10.5% | -8.06 |
| 10 s | 765 | 25% | -7.5% | -9.5% | -11.50 |
| 60 s | 765 | 22% | -8.1% | -6.8% | -12.35 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
