# PumpSwap-dekking — 2026-09-13 13:34 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **94245 SOL** over 37562 posities. Hiervan gecheckt: 2936 posities (58415 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 2841 | 57264.6 |
| deels_verkocht | 50 | 831.8 |
| nog_in_bezit | 45 | 318.5 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **97.2 SOL** tegen 208.9 SOL kostprijs (24 posities met een goedgekeurde prijs).

Poolprijzen: goedgekeurd: 6, prijs_onwaarschijnlijk: 14. Mediane verhouding met de laatste curveprijs: 0.2×. Afgekeurde prijzen tellen niet mee in de restwaarde: de grootste tokenhouder is niet altijd de pool, en bij een gewone wallet met veel WSOL rolt er een onzinprijs uit.

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | deels_verkocht | 1 | 2.2 |
| gevolgd | verkocht | 197 | 466.6 |
| niet_gevolgd | deels_verkocht | 49 | 829.6 |
| niet_gevolgd | nog_in_bezit | 45 | 318.5 |
| niet_gevolgd | verkocht | 2644 | 56798.0 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 1141 transacties opgehaald, 274 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |
|---|---|---|---|---|---|---|---|---|---|---|
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 196 | @8 (97%) | @96 (97%) | – | @112 (100%) | @144 (77%) | pool | ja |
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 84 | @8 (93%) | @376 (100%) | – | @112 (100%) | @144 (83%) | pool | nee |
| `c62e1552b4d9e870` | ? | inner | 8 | – | @7 (12%) | – | – | – | – | nee |
| `33e685a4017f83ad` | ? | inner | 6 | @0 (100%) | – | – | – | – | – | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 3 | – | – | – | @36 (100%) | @0 (67%) | – | nee |
| `e2d6f62107f293e5` | ? | inner_cpi+log | 2 | – | – | – | – | @0 (50%) | – | nee |
| `40c6cde8260871e2` | ? | log | 1 | @144 (100%) | @128 (100%) | – | @32 (100%) | @0 (100%) | – | nee |

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.
Uitgesloten als bewijs: 239 transacties met meer dan twee partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan één event van dat type (0 transacties). In die gevallen is het netto saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de layout fout is.

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

Waar de tokens niet matchen, zit de dichtstbijzijnde waarde er mediaan BuyEvent: 45.16%, SellEvent: 46.73%, c62e1552b4d9e870: 20.00%, e2d6f62107f293e5: 33.52% naast. Een klein percentage wijst op kosten die het event anders rekent dan de balans; een groot percentage op een verkeerd veld.

**Layout vastgelegd** in `data/pumpswap_layout.json`: BuyEvent (match 97%, n=196, herkenning via pool)

De layout klopt, maar het event noemt de **pool** en niet de mint. De bot weet niet welke pool bij welk token hoort, dus de ingestie blijft uit tot die koppeling er is. Dat is een volgende stap, geen fout in de layout.

## 3. Welke pool hoort bij welk token?

Het event noemt de pool. Waar in het poolaccount de mint staat, is niet gedocumenteerd, dus meten we het: van paren (pool, mint) die uit transacties bekend zijn, zoeken we waar de 32 bytes van de mint in de accountdata staan. Komt dat bij minstens 20 pools op dezelfde plek uit (95% van de gevallen), dan is dat het veld. Zo niet, dan gebeurt er niets — een gegokt veld levert de koers van een willekeurig token op.

**Veld vastgesteld op offset 43** (28 van 28 pools, 100%; accountlengte 301 bytes). Daarmee vraagt de analyse bij de keten op welke pool bij een mint hoort, en leest daarna de twee vaten van die pool. Dat vervangt de oude noodgreep 'de grootste tokenhouder is vermoedelijk de pool'.

| offset | pools waar de mint daar staat |
|---|---|
| @43 | 28 |

Deze run: 28 poolaccounts bekeken, 0 calls mislukt (niet opgeslagen, volgende keer opnieuw), 0 zonder mint in de data, 0 paren te gaan.

Koersen per route: pool_uit_programma/goedgekeurd: 6, pool_uit_programma/prijs_onwaarschijnlijk: 14

