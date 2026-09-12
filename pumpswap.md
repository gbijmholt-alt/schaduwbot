# PumpSwap-dekking — 2026-09-12 14:23 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **56608 SOL** over 23185 posities. Hiervan gecheckt: 2392 posities (52033 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 2303 | 50807.5 |
| deels_verkocht | 46 | 818.1 |
| nog_in_bezit | 43 | 407.4 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **467.6 SOL** tegen 474.1 SOL kostprijs (64 posities met een goedgekeurde prijs).

Poolprijzen: geen_wsol_of_tokens: 6, goedgekeurd: 19, prijs_onwaarschijnlijk: 19. Mediane verhouding met de laatste curveprijs: 0.88×. Afgekeurde prijzen tellen niet mee in de restwaarde: de grootste tokenhouder is niet altijd de pool, en bij een gewone wallet met veel WSOL rolt er een onzinprijs uit.

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | deels_verkocht | 3 | 4.1 |
| gevolgd | nog_in_bezit | 1 | 0.1 |
| gevolgd | verkocht | 120 | 266.9 |
| niet_gevolgd | deels_verkocht | 43 | 814.0 |
| niet_gevolgd | nog_in_bezit | 42 | 407.4 |
| niet_gevolgd | verkocht | 2183 | 50540.6 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 800 transacties opgehaald, 327 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |
|---|---|---|---|---|---|---|---|---|---|---|
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 198 | @8 (98%) | @96 (98%) | – | @353 (100%) | @144 (86%) | pool | ja |
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 132 | @8 (98%) | @96 (98%) | – | @240 (100%) | @144 (97%) | pool | ja |
| `c62e1552b4d9e870` | ? | inner | 15 | – | – | – | – | – | – | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 9 | – | – | – | @36 (100%) | @0 (89%) | pool | nee |
| `86240d48e86582d8` | ? | inner_cpi+log | 5 | – | – | – | @32 (100%) | @0 (100%) | pool | nee |
| `33e685a4017f83ad` | ? | inner | 3 | @0 (100%) | – | – | – | – | – | nee |
| `31487b2d6e40b085` | ? | log | 2 | @73 (100%) | – | @33 (100%) | @259 (100%) | @1 (100%) | mint | nee |
| `66063d1201daebea` | ? | inner | 2 | @0 (100%) | @8 (100%) | – | – | – | – | nee |
| `4d4d00c10e34a2f2` | ? | log | 1 | – | – | – | – | – | – | nee |
| `4d4d00810e34a2f2` | ? | log | 1 | – | – | – | – | – | – | nee |

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.
Uitgesloten als bewijs: 359 transacties met meer dan twee partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan één event van dat type (0 transacties). In die gevallen is het netto saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de layout fout is.

Waar de tokens niet matchen, zit de dichtstbijzijnde waarde er mediaan BuyEvent: 32.51%, 929fbdac925838f4: 74.17%, 86240d48e86582d8: 9.55% naast. Een klein percentage wijst op kosten die het event anders rekent dan de balans; een groot percentage op een verkeerd veld.

**Layout vastgelegd** in `data/pumpswap_layout.json`: BuyEvent (match 98%, n=198, herkenning via pool), SellEvent (match 98%, n=132, herkenning via pool)

De layout klopt, maar het event noemt de **pool** en niet de mint. De bot weet niet welke pool bij welk token hoort, dus de ingestie blijft uit tot die koppeling er is. Dat is een volgende stap, geen fout in de layout.

