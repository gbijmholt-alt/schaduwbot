# PumpSwap-dekking — 2026-09-12 13:05 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **53529 SOL** over 22120 posities. Hiervan gecheckt: 1990 posities (48573 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 1911 | 47206.8 |
| deels_verkocht | 45 | 955.2 |
| nog_in_bezit | 34 | 411.0 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **405.0 SOL** tegen 447.8 SOL kostprijs (55 posities met een goedgekeurde prijs).

Poolprijzen: geen_wsol_of_tokens: 3, goedgekeurd: 18, prijs_onwaarschijnlijk: 18. Mediane verhouding met de laatste curveprijs: 0.91×. Afgekeurde prijzen tellen niet mee in de restwaarde: de grootste tokenhouder is niet altijd de pool, en bij een gewone wallet met veel WSOL rolt er een onzinprijs uit.

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | deels_verkocht | 3 | 4.1 |
| gevolgd | nog_in_bezit | 1 | 0.1 |
| gevolgd | verkocht | 118 | 264.4 |
| niet_gevolgd | deels_verkocht | 42 | 951.1 |
| niet_gevolgd | nog_in_bezit | 33 | 410.9 |
| niet_gevolgd | verkocht | 1793 | 46942.3 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 1195 transacties opgehaald, 501 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |
|---|---|---|---|---|---|---|---|---|---|---|
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 122 | @8 (98%) | @376 (142%) | – | @208 (100%) | @144 (99%) | pool | ja |
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 84 | @8 (98%) | @96 (98%) | – | @112 (100%) | @144 (84%) | pool | ja |
| `c62e1552b4d9e870` | ? | inner | 13 | – | – | – | – | – | – | nee |
| `33e685a4017f83ad` | ? | inner | 8 | @0 (100%) | – | – | – | – | – | nee |
| `66063d1201daebea` | ? | inner | 1 | @0 (100%) | – | – | – | – | – | nee |
| `6161d7905d92167c` | ExtendAccountEvent | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `e2d6f62107f293e5` | ? | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 0 | – | – | – | – | – | – | nee |

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.
Uitgesloten als bewijs: 420 transacties met meer dan twee partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan één event van dat type (297 transacties). In die gevallen is het netto saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de layout fout is.

Waar de tokens niet matchen, zit de dichtstbijzijnde waarde er mediaan SellEvent: 42.96%, BuyEvent: 39.17% naast. Een klein percentage wijst op kosten die het event anders rekent dan de balans; een groot percentage op een verkeerd veld.

**Layout vastgelegd** in `data/pumpswap_layout.json`: SellEvent (match 98%, n=122, herkenning via pool), BuyEvent (match 98%, n=84, herkenning via pool)

De layout klopt, maar het event noemt de **pool** en niet de mint. De bot weet niet welke pool bij welk token hoort, dus de ingestie blijft uit tot die koppeling er is. Dat is een volgende stap, geen fout in de layout.

