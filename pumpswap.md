# PumpSwap-dekking — 2026-09-13 18:07 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **105891 SOL** over 44703 posities. Hiervan gecheckt: 2956 posities (58456 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 2861 | 57306.9 |
| deels_verkocht | 49 | 829.6 |
| nog_in_bezit | 46 | 319.3 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **177.7 SOL** tegen 265.0 SOL kostprijs (39 posities met een goedgekeurde prijs).

Poolprijzen: geen_antwoord: 2, goedgekeurd: 33, prijs_onwaarschijnlijk: 218. Mediane verhouding met de laatste curveprijs: 0.17×. Afgekeurde prijzen tellen niet mee in de restwaarde: de grootste tokenhouder is niet altijd de pool, en bij een gewone wallet met veel WSOL rolt er een onzinprijs uit.

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | nog_in_bezit | 1 | 0.8 |
| gevolgd | verkocht | 217 | 508.9 |
| niet_gevolgd | deels_verkocht | 49 | 829.6 |
| niet_gevolgd | nog_in_bezit | 45 | 318.5 |
| niet_gevolgd | verkocht | 2644 | 56798.0 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 1736 transacties opgehaald, 498 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |
|---|---|---|---|---|---|---|---|---|---|---|
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 341 | @8 (98%) | @96 (98%) | – | @112 (100%) | @144 (80%) | pool | ja |
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 165 | @8 (95%) | @376 (99%) | – | @112 (100%) | @144 (83%) | pool | ja |
| `33e685a4017f83ad` | ? | inner | 24 | @0 (100%) | – | – | – | – | – | nee |
| `c62e1552b4d9e870` | ? | inner | 23 | – | @7 (4%) | – | – | – | – | nee |
| `e2d6f62107f293e5` | ? | inner_cpi+log | 6 | – | – | – | – | @0 (83%) | – | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 6 | – | – | – | @36 (100%) | @0 (83%) | – | nee |
| `40c6cde8260871e2` | ? | log | 1 | @144 (100%) | @128 (100%) | – | @32 (100%) | @0 (100%) | – | nee |
| `e1ca49af932ba096` | ? | log | 1 | @73 (100%) | @65 (100%) | – | @0 (100%) | – | – | nee |
| `5351533102020100` | ? | log | 1 | – | – | – | @1 (100%) | – | – | nee |
| `5343575305010205` | ? | log | 1 | – | @24 (100%) | – | – | – | – | nee |
| `5056325401430206` | ? | log | 1 | – | – | – | – | – | – | nee |
| `5052534d04050300` | ? | log | 1 | – | @8 (100%) | – | – | – | – | nee |
| `504558430400b923` | ? | log | 1 | – | – | – | – | – | – | nee |
| `66063d1201daebea` | ? | inner | 1 | @0 (100%) | – | – | – | – | – | nee |
| `86240d48e86582d8` | ? | inner_cpi+log | 1 | – | – | – | @32 (100%) | @0 (100%) | – | nee |

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.
Uitgesloten als bewijs: 401 transacties met meer dan twee partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan één event van dat type (0 transacties). In die gevallen is het netto saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de layout fout is.

**Welke offset is de pool?** In één event staan meerdere accounts, dus meerdere offsets halen 100%. De hoogste eruit pakken is willekeurig, dus vragen we bij de keten na wie de eigenaar van het account is: een pool is eigendom van het AMM-programma, een wallet van het systeemprogramma.

| event | offset | match | eigenaar-programma | pool |
|---|---|---|---|---|
| BuyEvent | @112 | 100% | pAMMBay6… | ja |
| BuyEvent | @176 | 100% | TokenzQd… | nee |
| BuyEvent | @208 | 100% | onbekend | nee |
| BuyEvent | @240 | 100% | 11111111… | nee |
| BuyEvent | @272 | 100% | Tokenkeg… | nee |
| BuyEvent | @353 | 100% | NativeLo… | nee |
| SellEvent | @112 | 100% | pAMMBay6… | ja |
| SellEvent | @176 | 100% | onbekend | nee |
| SellEvent | @208 | 100% | onbekend | nee |
| SellEvent | @240 | 100% | 11111111… | nee |
| SellEvent | @272 | 100% | Tokenkeg… | nee |
| 929fbdac925838f4 | @36 | 100% | NativeLo… | nee |
| 929fbdac925838f4 | @37 | 100% | NativeLo… | nee |
| 929fbdac925838f4 | @38 | 100% | NativeLo… | nee |
| 929fbdac925838f4 | @39 | 100% | NativeLo… | nee |
| 929fbdac925838f4 | @40 | 100% | NativeLo… | nee |
| 40c6cde8260871e2 | @32 | 100% | 11111111… | nee |
| 40c6cde8260871e2 | @64 | 100% | Tokenkeg… | nee |
| 40c6cde8260871e2 | @96 | 100% | TokenzQd… | nee |
| e1ca49af932ba096 | @0 | 100% | whirLbMi… | nee |
| 5351533102020100 | @1 | 100% | NativeLo… | nee |
| 5351533102020100 | @2 | 100% | NativeLo… | nee |
| 5351533102020100 | @3 | 100% | NativeLo… | nee |
| 5351533102020100 | @4 | 100% | NativeLo… | nee |
| 5351533102020100 | @5 | 100% | NativeLo… | nee |
| 5351533102020100 | @6 | 100% | NativeLo… | nee |
| 5351533102020100 | @7 | 100% | NativeLo… | nee |
| 5351533102020100 | @8 | 100% | NativeLo… | nee |
| 5351533102020100 | @9 | 100% | NativeLo… | nee |
| 5351533102020100 | @10 | 100% | NativeLo… | nee |
| 5351533102020100 | @11 | 100% | NativeLo… | nee |
| 5351533102020100 | @12 | 100% | NativeLo… | nee |
| 5351533102020100 | @13 | 100% | NativeLo… | nee |
| 5351533102020100 | @14 | 100% | NativeLo… | nee |
| 5351533102020100 | @15 | 100% | NativeLo… | nee |
| 5351533102020100 | @16 | 100% | NativeLo… | nee |
| 86240d48e86582d8 | @32 | 100% | 11111111… | nee |

Waar de tokens niet matchen, zit de dichtstbijzijnde waarde er mediaan BuyEvent: 45.16%, SellEvent: 46.73%, c62e1552b4d9e870: 20.00%, e2d6f62107f293e5: 33.52%, 929fbdac925838f4: 38.91%, 504558430400b923: 64.01% naast. Een klein percentage wijst op kosten die het event anders rekent dan de balans; een groot percentage op een verkeerd veld.

**Layout vastgelegd** in `data/pumpswap_layout.json`: BuyEvent (match 98%, n=341, herkenning via pool), SellEvent (match 95%, n=165, herkenning via pool)

De layout klopt, maar het event noemt de **pool** en niet de mint. De bot weet niet welke pool bij welk token hoort, dus de ingestie blijft uit tot die koppeling er is. Dat is een volgende stap, geen fout in de layout.

## 3. Welke pool hoort bij welk token?

Het event noemt de pool. Waar in het poolaccount de mint staat, is niet gedocumenteerd, dus meten we het: van paren (pool, mint) die uit transacties bekend zijn, zoeken we waar de 32 bytes van de mint in de accountdata staan. Komt dat bij minstens 20 pools op dezelfde plek uit (95% van de gevallen), dan is dat het veld. Zo niet, dan gebeurt er niets — een gegokt veld levert de koers van een willekeurig token op.

**Veld vastgesteld op offset 43** (85 van 85 pools, 100%; accountlengte 301 bytes). Daarmee vraagt de analyse bij de keten op welke pool bij een mint hoort, en leest daarna de twee vaten van die pool. Dat vervangt de oude noodgreep 'de grootste tokenhouder is vermoedelijk de pool'.

| offset | pools waar de mint daar staat |
|---|---|
| @43 | 85 |

Deze run: 14 poolaccounts bekeken, 0 calls mislukt (niet opgeslagen, volgende keer opnieuw), 0 zonder mint in de data, 0 paren te gaan.

**Is die route ook geijkt?** Een token dat net gemigreerd is kan zijn koers nog niet ver bewogen hebben, dus daar hóórt de poolprijs gelijk te zijn aan de laatste curveprijs. Dat is de enige plek waar deze route te controleren valt zonder AMM-trades.

**Nog niet geijkt**: nog 20 migraties van minder dan 120 minuten oud te gaan (0 migraties jonger dan 120 minuten gemeten, 285 kandidaten in de laatste 12 uur). Zolang dit niet staat, wordt elke prijs die meer dan 20× van de curveprijs afwijkt afgekeurd — streng, maar zonder ijking is er geen reden die grens te verruimen.


De losse getallen van de laatste metingen, zodat te zien is welke kant er scheef staat. `SOL in pool` is het WSOL-vat van de pool; `SOL uit curve` is wat er volgens onze eigen trades op de curve is ingelegd — die twee horen op de migratiekosten na gelijk te zijn.

| min. na migratie | SOL in pool | SOL uit curve | tokens in pool | poolprijs | curveprijs | verhouding |
|---|---|---|---|---|---|---|
| 39.6 | 55.4479 | -103.1242 | 244,657,546 | 2.266347424286905e-07 | 2.3119924374092729e-07 | 0.98026 |
| 57.5 | 5317.3199 | -86.0679 | 3,303,560 | 0.0016095727758264442 | 4.108801681207574e-07 | 3917.37762 |
| 58.0 | 0.143 | -86.0679 | 998,692,761 | 1.43187179806121e-10 | 4.108801681207574e-07 | 0.00035 |
| 59.4 | 5195.8984 | -86.0679 | 3,379,926 | 0.0015372815618336488 | 4.108801681207574e-07 | 3741.43529 |
| 59.8 | 27.4416 | -87.7753 | 401,392,423 | 6.836601391218208e-08 | 4.108801685280457e-07 | 0.16639 |
| 62.1 | 0.72 | -86.0679 | 970,253,388 | 7.420741928896408e-10 | 4.108801681207574e-07 | 0.00181 |
| 63.7 | 0.5107 | -86.0679 | 978,480,852 | 5.219315217910611e-10 | 4.108801681207574e-07 | 0.00127 |
| 65.2 | 885.496 | -86.0679 | 19,523,104 | 4.5356312606917475e-05 | 4.108801681207574e-07 | 110.38818 |
| 70.5 | 3.4384 | -86.0679 | 845,230,485 | 4.068002822381007e-09 | 4.1088016814576633e-07 | 0.0099 |
| 70.8 | 1.1382 | -86.0679 | 949,107,794 | 1.1992315383846691e-09 | 4.108801681207574e-07 | 0.00292 |

| route | prijzen | p10 | mediaan | p90 | (poolprijs ÷ laatste curveprijs)
|---|---|---|---|---|---|
| pool_uit_programma | 251 | 0.00046 | 0.00767 | 110.87971 | |

Koersen van gemigreerde tokens opgehaald voor de afloopanalyse: 109 deze run, 1632 te gaan, 11 calls mislukt.

Koersen per route: pool_uit_programma/geen_antwoord: 2, pool_uit_programma/goedgekeurd: 33, pool_uit_programma/prijs_onwaarschijnlijk: 218

