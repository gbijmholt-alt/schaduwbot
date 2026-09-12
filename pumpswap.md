# PumpSwap-dekking — 2026-09-12 17:07 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **63539 SOL** over 26030 posities. Hiervan gecheckt: 2552 posities (57469 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 2458 | 56071.7 |
| deels_verkocht | 51 | 1001.4 |
| nog_in_bezit | 43 | 395.8 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **871.4 SOL** tegen 571.4 SOL kostprijs (68 posities met een goedgekeurde prijs).

Poolprijzen: geen_wsol_of_tokens: 7, goedgekeurd: 22, prijs_onwaarschijnlijk: 20. Mediane verhouding met de laatste curveprijs: 0.94×. Afgekeurde prijzen tellen niet mee in de restwaarde: de grootste tokenhouder is niet altijd de pool, en bij een gewone wallet met veel WSOL rolt er een onzinprijs uit.

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | deels_verkocht | 3 | 4.1 |
| gevolgd | nog_in_bezit | 1 | 0.1 |
| gevolgd | verkocht | 131 | 289.6 |
| niet_gevolgd | deels_verkocht | 48 | 997.3 |
| niet_gevolgd | nog_in_bezit | 42 | 395.7 |
| niet_gevolgd | verkocht | 2327 | 55782.2 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 368 transacties opgehaald, 80 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |
|---|---|---|---|---|---|---|---|---|---|---|
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 56 | @8 (100%) | @96 (100%) | – | @112 (100%) | @144 (64%) | pool | ja |
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 24 | @8 (100%) | @96 (100%) | – | @112 (100%) | @144 (71%) | pool | nee |
| `c62e1552b4d9e870` | ? | inner | 3 | – | @7 (33%) | – | – | – | – | nee |
| `33e685a4017f83ad` | ? | inner | 2 | @0 (100%) | – | – | – | – | – | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 2 | – | – | – | @36 (100%) | @0 (100%) | – | nee |
| `e2d6f62107f293e5` | ? | inner_cpi+log | 1 | – | – | – | – | @0 (100%) | – | nee |
| `40c6cde8260871e2` | ? | log | 1 | @144 (100%) | @128 (100%) | – | @32 (100%) | @0 (100%) | – | nee |

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.
Uitgesloten als bewijs: 48 transacties met meer dan twee partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan één event van dat type (0 transacties). In die gevallen is het netto saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de layout fout is.

**Welke offset is de pool?** In één event staan meerdere accounts, dus meerdere offsets halen 100%. De hoogste eruit pakken is willekeurig, dus vragen we bij de keten na wie de eigenaar van het account is: een pool is eigendom van het AMM-programma, een wallet van het systeemprogramma.

| event | offset | match | eigenaar-programma | pool |
|---|---|---|---|---|
| BuyEvent | @112 | 100% | pAMMBay6… | ja |
| BuyEvent | @176 | 100% | TokenzQd… | nee |
| BuyEvent | @208 | 100% | onbekend | ja |
| BuyEvent | @240 | 100% | 11111111… | nee |
| BuyEvent | @272 | 100% | Tokenkeg… | nee |
| BuyEvent | @353 | 100% | NativeLo… | nee |
| SellEvent | @112 | 100% | pAMMBay6… | ja |
| SellEvent | @176 | 100% | TokenzQd… | nee |
| SellEvent | @208 | 100% | onbekend | ja |
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

Waar de tokens niet matchen, zit de dichtstbijzijnde waarde er mediaan c62e1552b4d9e870: 20.00%, e2d6f62107f293e5: 33.52% naast. Een klein percentage wijst op kosten die het event anders rekent dan de balans; een groot percentage op een verkeerd veld.

**Layout vastgelegd** in `data/pumpswap_layout.json`: BuyEvent (match 100%, n=56, herkenning via pool)

De layout klopt, maar het event noemt de **pool** en niet de mint. De bot weet niet welke pool bij welk token hoort, dus de ingestie blijft uit tot die koppeling er is. Dat is een volgende stap, geen fout in de layout.

