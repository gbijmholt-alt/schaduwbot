# PumpSwap-dekking — 2026-09-14 05:05 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **134719 SOL** over 59674 posities. Hiervan gecheckt: 3001 posities (58752 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 2901 | 57504.5 |
| deels_verkocht | 52 | 917.9 |
| nog_in_bezit | 48 | 329.6 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **168.0 SOL** tegen 72.3 SOL kostprijs (18 posities met een goedgekeurde prijs).

Poolprijzen: geen_antwoord: 21, goedgekeurd: 63, prijs_onwaarschijnlijk: 456. Mediane verhouding met de laatste curveprijs: 0.24×. Afgekeurde prijzen tellen niet mee in de restwaarde: de grootste tokenhouder is niet altijd de pool, en bij een gewone wallet met veel WSOL rolt er een onzinprijs uit.

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | deels_verkocht | 2 | 1.9 |
| gevolgd | nog_in_bezit | 3 | 11.1 |
| gevolgd | verkocht | 257 | 706.5 |
| niet_gevolgd | deels_verkocht | 50 | 916.0 |
| niet_gevolgd | nog_in_bezit | 45 | 318.5 |
| niet_gevolgd | verkocht | 2644 | 56798.0 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 2326 transacties opgehaald, 783 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |
|---|---|---|---|---|---|---|---|---|---|---|
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 527 | @8 (98%) | @96 (98%) | – | @112 (100%) | @144 (81%) | pool | ja |
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 266 | @8 (96%) | @376 (99%) | – | @112 (100%) | @144 (86%) | pool | ja |
| `c62e1552b4d9e870` | ? | inner | 34 | – | @7 (3%) | – | – | – | – | nee |
| `33e685a4017f83ad` | ? | inner | 29 | @0 (100%) | – | – | – | – | – | nee |
| `e2d6f62107f293e5` | ? | inner_cpi+log | 6 | – | – | – | – | @0 (83%) | – | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 6 | – | – | – | @36 (100%) | @0 (83%) | – | nee |
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

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.
Uitgesloten als bewijs: 518 transacties met meer dan twee partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan één event van dat type (0 transacties). In die gevallen is het netto saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de layout fout is.

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

Waar de tokens niet matchen, zit de dichtstbijzijnde waarde er mediaan BuyEvent: 37.38%, SellEvent: 52.45%, c62e1552b4d9e870: 20.35%, e2d6f62107f293e5: 33.52%, 929fbdac925838f4: 38.91%, 504558430400b923: 64.01% naast. Een klein percentage wijst op kosten die het event anders rekent dan de balans; een groot percentage op een verkeerd veld.

**Layout vastgelegd** in `data/pumpswap_layout.json`: BuyEvent (match 98%, n=527, herkenning via pool), SellEvent (match 96%, n=266, herkenning via pool)

De layout klopt, maar het event noemt de **pool** en niet de mint. De bot weet niet welke pool bij welk token hoort, dus de ingestie blijft uit tot die koppeling er is. Dat is een volgende stap, geen fout in de layout.

## 3. Welke pool hoort bij welk token?

Het event noemt de pool. Waar in het poolaccount de mint staat, is niet gedocumenteerd, dus meten we het: van paren (pool, mint) die uit transacties bekend zijn, zoeken we waar de 32 bytes van de mint in de accountdata staan. Komt dat bij minstens 20 pools op dezelfde plek uit (95% van de gevallen), dan is dat het veld. Zo niet, dan gebeurt er niets — een gegokt veld levert de koers van een willekeurig token op.

**Veld vastgesteld op offset 43** (154 van 154 pools, 100%; accountlengte 301 bytes). Daarmee vraagt de analyse bij de keten op welke pool bij een mint hoort, en leest daarna de twee vaten van die pool. Dat vervangt de oude noodgreep 'de grootste tokenhouder is vermoedelijk de pool'.

| offset | pools waar de mint daar staat |
|---|---|
| @43 | 154 |

Deze run: 21 poolaccounts bekeken, 0 calls mislukt (niet opgeslagen, volgende keer opnieuw), 0 zonder mint in de data, 0 paren te gaan.

**Is die route ook geijkt?** Een token dat net gemigreerd is kan zijn koers nog niet ver bewogen hebben, dus daar hóórt de poolprijs gelijk te zijn aan de laatste curveprijs. Dat is de enige plek waar deze route te controleren valt zonder AMM-trades.

**Nog niet geijkt**: mediane afwijking 100% boven 25% (104 migraties jonger dan 120 minuten gemeten, 261 kandidaten in de laatste 12 uur). Zolang dit niet staat, wordt elke prijs die meer dan 20× van de curveprijs afwijkt afgekeurd — streng, maar zonder ijking is er geen reden die grens te verruimen.


**Klopt de opzoeking mint → pool?** De enige directe test: in een echte AMM-transactie staan de mint én de pool die de trade deed. Levert de opzoeking dezelfde pool op?

| dezelfde pool | andere pool | geen pool gevonden | meerdere pools | calls mislukt |
|---|---|---|---|---|
| 25 | 0 | 0 | 0 | 0 |

**De opzoeking klopt.** De koersen komen dus uit de pool die het token echt verhandelt.


De losse getallen van de laatste metingen, zodat te zien is welke kant er scheef staat. `SOL in pool` is het WSOL-vat van de pool; `SOL uit curve` is wat er volgens onze eigen trades op de curve is ingelegd — die twee horen op de migratiekosten na gelijk te zijn.

| min. na migratie | SOL in pool | SOL uit curve | tokens in pool | poolprijs | curveprijs | verhouding |
|---|---|---|---|---|---|---|
| 12.3 | 61.479 | 91.0686 | 222,694,255 | 2.760690889719859e-07 | 1.5526567626712698e-07 | 1.77804 |
| 15.1 | 70.854 | 88.054 | 199,190,989 | 3.557088620964992e-07 | 1.242811929414436e-07 | 2.86213 |
| 34.4 | 0.0184 | 0.2865 | 1,493,899,946 | 1.2316755251347526e-11 | 1.2041450017863522e-09 | 0.01023 |
| 39.6 | 55.4479 | -103.1242 | 244,657,546 | 2.266347424286905e-07 | 2.3119924374092729e-07 | 0.98026 |
| 47.6 | 1.9343 | 92.4971 | 905,516,961 | 2.1361278503904953e-09 | 4.108801721686317e-07 | 0.0052 |
| 47.8 | 4.7321 | 89.6614 | 790,499,925 | 5.986211829745256e-09 | 4.1088017037513397e-07 | 0.01457 |
| 48.6 | 0.0166 | 1.1705 | 1,198,392,121 | 1.385189346977149e-11 | 9.101667810088045e-12 | 1.52191 |
| 50.0 | 0.0053 | 0.6933 | 1,749,894,221 | 3.028754502513375e-12 | 1.4302205491047229e-11 | 0.21177 |
| 50.5 | 0.132 | 0.3855 | 340,074,692 | 3.881500247769436e-10 | 1.5428177522074042e-10 | 2.51585 |
| 52.3 | 4.6898 | 92.2929 | 791,736,680 | 5.923434041295104e-09 | 4.1088017249732044e-07 | 0.01442 |

| route | prijzen | p10 | mediaan | p90 | (poolprijs ÷ laatste curveprijs)
|---|---|---|---|---|---|
| pool_uit_programma | 519 | 0.00045 | 0.00699 | 68.15658 | |

Koersen van gemigreerde tokens opgehaald voor de afloopanalyse: 79 deze run, 1681 te gaan, 41 calls mislukt.

Koersen per route: pool_uit_programma/geen_antwoord: 21, pool_uit_programma/goedgekeurd: 63, pool_uit_programma/prijs_onwaarschijnlijk: 456

