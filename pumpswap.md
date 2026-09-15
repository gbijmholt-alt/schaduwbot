# PumpSwap-dekking — 2026-09-15 00:05 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **185478 SOL** over 83408 posities. Hiervan gecheckt: 3043 posities (58835 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 2940 | 57664.8 |
| deels_verkocht | 52 | 832.1 |
| nog_in_bezit | 51 | 338.3 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **7.8 SOL** tegen 2.1 SOL kostprijs (2 posities met een goedgekeurde prijs).

Poolprijzen: geen_antwoord: 40, goedgekeurd: 115, prijs_onwaarschijnlijk: 1253. Mediane verhouding met de laatste curveprijs: 0.34×. Afgekeurde prijzen tellen niet mee in de restwaarde: de grootste tokenhouder is niet altijd de pool, en bij een gewone wallet met veel WSOL rolt er een onzinprijs uit.

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | deels_verkocht | 3 | 2.5 |
| gevolgd | nog_in_bezit | 6 | 19.8 |
| gevolgd | verkocht | 295 | 780.4 |
| niet_gevolgd | deels_verkocht | 49 | 829.6 |
| niet_gevolgd | nog_in_bezit | 45 | 318.5 |
| niet_gevolgd | verkocht | 2645 | 56884.4 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 3947 transacties opgehaald, 1345 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |
|---|---|---|---|---|---|---|---|---|---|---|
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 890 | @8 (96%) | @96 (96%) | – | @112 (100%) | @144 (81%) | pool | ja |
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 485 | @8 (93%) | @376 (97%) | – | @112 (100%) | @144 (87%) | pool | nee |
| `c62e1552b4d9e870` | ? | inner | 60 | – | @0 (3%) | – | – | – | – | nee |
| `33e685a4017f83ad` | ? | inner | 56 | @0 (93%) | @8 (2%) | – | – | – | – | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 7 | – | – | – | @36 (100%) | @0 (86%) | – | nee |
| `e2d6f62107f293e5` | ? | inner_cpi+log | 6 | – | – | – | – | @0 (83%) | – | nee |
| `bddb7fd34ee661ee` | TradeEvent | log | 2 | @40 (100%) | – | @0 (100%) | @121 (100%) | @49 (50%) | mint | nee |
| `40c6cde8260871e2` | ? | log | 2 | @144 (50%) | @128 (50%) | – | @64 (50%) | @0 (50%) | – | nee |
| `e1ca49af932ba096` | ? | log | 1 | @73 (100%) | @65 (100%) | – | @0 (100%) | – | – | nee |
| `5351533102020100` | ? | log | 1 | – | – | – | @1 (100%) | – | – | nee |
| `5343575305010205` | ? | log | 1 | – | @24 (100%) | – | – | – | – | nee |
| `5056325401430206` | ? | log | 1 | – | – | – | – | – | – | nee |
| `5052534d04050300` | ? | log | 1 | – | @8 (100%) | – | – | – | – | nee |
| `504558430400b923` | ? | log | 1 | – | – | – | – | – | – | nee |
| `66063d1201daebea` | ? | inner | 1 | @0 (100%) | – | – | – | – | – | nee |
| `86240d48e86582d8` | ? | inner_cpi+log | 1 | – | – | – | @32 (100%) | @0 (100%) | – | nee |
| `96aa7a934171ee99` | ? | log | 1 | – | – | – | – | – | – | nee |
| `1459dfc6c27cdb0d` | ? | log | 1 | – | – | – | @40 (100%) | @8 (100%) | – | nee |
| `560ced64f3abe39f` | ? | log | 1 | – | – | – | – | – | – | nee |
| `31487b2d6e40b085` | ? | log | 1 | @73 (100%) | – | @33 (100%) | @259 (100%) | @1 (100%) | mint | nee |
| `4d4d00827d8aac51` | ? | log | 1 | – | – | – | – | – | – | nee |

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.
Uitgesloten als bewijs: 999 transacties met meer dan twee partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan één event van dat type (0 transacties). In die gevallen is het netto saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de layout fout is.

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
| TradeEvent | @121 | 100% | 11111111… | nee |
| TradeEvent | @212 | 100% | NativeLo… | nee |
| TradeEvent | @213 | 100% | NativeLo… | nee |
| TradeEvent | @214 | 100% | NativeLo… | nee |
| TradeEvent | @215 | 100% | NativeLo… | nee |
| TradeEvent | @216 | 100% | NativeLo… | nee |
| TradeEvent | @217 | 100% | NativeLo… | nee |
| TradeEvent | @218 | 100% | NativeLo… | nee |
| TradeEvent | @287 | 100% | NativeLo… | nee |
| TradeEvent | @288 | 100% | NativeLo… | nee |
| TradeEvent | @289 | 100% | NativeLo… | nee |
| TradeEvent | @290 | 100% | NativeLo… | nee |
| TradeEvent | @291 | 100% | NativeLo… | nee |
| TradeEvent | @292 | 100% | NativeLo… | nee |
| TradeEvent | @293 | 100% | NativeLo… | nee |
| TradeEvent | @294 | 100% | NativeLo… | nee |
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
| 1459dfc6c27cdb0d | @40 | 100% | NativeLo… | nee |
| 31487b2d6e40b085 | @259 | 100% | NativeLo… | nee |
| 31487b2d6e40b085 | @260 | 100% | NativeLo… | nee |
| 31487b2d6e40b085 | @261 | 100% | NativeLo… | nee |
| 31487b2d6e40b085 | @262 | 100% | NativeLo… | nee |
| 31487b2d6e40b085 | @263 | 100% | NativeLo… | nee |

Waar de tokens niet matchen, zit de dichtstbijzijnde waarde er mediaan BuyEvent: 45.12%, SellEvent: 34.98%, c62e1552b4d9e870: 20.18%, 929fbdac925838f4: 38.91%, e2d6f62107f293e5: 33.52%, 504558430400b923: 64.01% naast. Een klein percentage wijst op kosten die het event anders rekent dan de balans; een groot percentage op een verkeerd veld.

**Layout vastgelegd** in `data/pumpswap_layout.json`: BuyEvent (match 96%, n=890, herkenning via pool)

De layout klopt, maar het event noemt de **pool** en niet de mint. De bot weet niet welke pool bij welk token hoort, dus de ingestie blijft uit tot die koppeling er is. Dat is een volgende stap, geen fout in de layout.

## 3. Welke pool hoort bij welk token?

Het event noemt de pool. Waar in het poolaccount de mint staat, is niet gedocumenteerd, dus meten we het: van paren (pool, mint) die uit transacties bekend zijn, zoeken we waar de 32 bytes van de mint in de accountdata staan. Komt dat bij minstens 20 pools op dezelfde plek uit (95% van de gevallen), dan is dat het veld. Zo niet, dan gebeurt er niets — een gegokt veld levert de koers van een willekeurig token op.

**Veld vastgesteld op offset 43** (305 van 305 pools, 100%; accountlengte 301 bytes). Daarmee vraagt de analyse bij de keten op welke pool bij een mint hoort, en leest daarna de twee vaten van die pool. Dat vervangt de oude noodgreep 'de grootste tokenhouder is vermoedelijk de pool'.

| offset | pools waar de mint daar staat |
|---|---|
| @43 | 305 |

Deze run: 12 poolaccounts bekeken, 0 calls mislukt (niet opgeslagen, volgende keer opnieuw), 0 zonder mint in de data, 0 paren te gaan.

**Is die route ook geijkt?** Een token dat net gemigreerd is kan zijn koers nog niet ver bewogen hebben, dus daar hóórt de poolprijs gelijk te zijn aan de laatste curveprijs. Dat is de enige plek waar deze route te controleren valt zonder AMM-trades.

Alleen de eerste bak mag oordelen: een memecoin beweegt in een uur makkelijk een factor 1000, dus een verschil na een uur zegt niets over of we goed lezen. Het verloop over de bakken is zelf het bewijs — loopt de afwijking op met de leeftijd, dan lezen we goed en beweegt de koers; is hij overal gelijk, dan lezen we iets verkeerd.

| minuten na migratie | metingen | mediane afwijking van de curveprijs |
|---|---|---|
| 0–5 | 50 | 100% |
| 5–15 | 29 | 100% |
| 15–60 | 52 | 99% |
| 60–120 | 180 | 100% |
| 120+ | 0 | – |

**Nog niet geijkt**: mediane afwijking 100% boven 25% binnen 5 minuten na de migratie. Zolang dit niet staat, wordt elke prijs die meer dan 20× van de curveprijs afwijkt afgekeurd en worden er geen koersen van gemigreerde tokens weggeschreven.


**Klopt de opzoeking mint → pool?** De enige directe test: in een echte AMM-transactie staan de mint én de pool die de trade deed. Levert de opzoeking dezelfde pool op?

| dezelfde pool | andere pool | geen pool gevonden | meerdere pools | calls mislukt |
|---|---|---|---|---|
| 25 | 0 | 0 | 0 | 0 |

**De opzoeking klopt.** De koersen komen dus uit de pool die het token echt verhandelt.


De losse getallen van de laatste metingen, zodat te zien is welke kant er scheef staat. `SOL in pool` is het WSOL-vat van de pool; `SOL uit curve` is wat er volgens onze eigen trades op de curve is ingelegd — die twee horen op de migratiekosten na gelijk te zijn.

| min. na migratie | SOL in pool | SOL uit curve | tokens in pool | poolprijs | curveprijs | verhouding |
|---|---|---|---|---|---|---|
| -3.0 | 62.6526 | None | 220,257,319 | 2.844518418736187e-07 | 4.1088016811718474e-07 | 0.6923 |
| -2.6 | 54.5481 | None | 244,328,324 | 2.2325737356781963e-07 | 4.1088016811718474e-07 | 0.54336 |
| -2.6 | 0.0 | None | 501,100,823 | None | 4.1088016811718474e-07 | None |
| -2.5 | 791.8962 | None | 21,762,211 | 3.638859152334176e-05 | 4.1088016811718474e-07 | 88.56254 |
| -2.4 | 0.1027 | None | 1,159,349,784 | 8.858413688936885e-11 | 4.1088016811718474e-07 | 0.00022 |
| -1.9 | 1467.9065 | None | 11,875,015 | 0.00012361301918174138 | 4.1088016811718474e-07 | 300.84932 |
| -1.4 | 0.0153 | None | 799,613,897 | 1.9134234737690948e-11 | 4.1088016811718474e-07 | 5e-05 |
| -1.0 | 0.0157 | 0.534 | 746,747,051 | 2.1024522267471548e-11 | 1.0196232862786969e-11 | 2.06199 |
| -1.0 | 161.3737 | None | 98,359,779 | 1.6406472376422565e-06 | 4.1088016811718474e-07 | 3.99301 |
| -1.0 | 0.0 | 0.0 | 336,512,315 | None | 4.1088016811718474e-07 | None |

| route | prijzen | p10 | mediaan | p90 | (poolprijs ÷ laatste curveprijs)
|---|---|---|---|---|---|
| pool_uit_programma | 1368 | 0.00045 | 0.0059 | 58.26677 | |

Koersen van gemigreerde tokens opgehaald voor de afloopanalyse: 62 deze run, 1588 te gaan, 58 calls mislukt.

Koersen per route: pool_uit_programma/geen_antwoord: 40, pool_uit_programma/goedgekeurd: 115, pool_uit_programma/prijs_onwaarschijnlijk: 1253

