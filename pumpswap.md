# PumpSwap-dekking — 2026-09-12 12:01 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **50371 SOL** over 20035 posities. Hiervan gecheckt: 1591 posities (45088 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 1532 | 43875.9 |
| deels_verkocht | 36 | 843.8 |
| nog_in_bezit | 23 | 368.6 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **27819.0 SOL** tegen 862.5 SOL kostprijs (52 posities met prijs).

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | deels_verkocht | 3 | 4.1 |
| gevolgd | nog_in_bezit | 1 | 0.1 |
| gevolgd | verkocht | 111 | 261.6 |
| niet_gevolgd | deels_verkocht | 33 | 839.7 |
| niet_gevolgd | nog_in_bezit | 22 | 368.6 |
| niet_gevolgd | verkocht | 1421 | 43614.3 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 795 transacties opgehaald, 297 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |
|---|---|---|---|---|---|---|---|---|---|---|
| `c62e1552b4d9e870` | ? | inner | 10 | – | – | – | – | – | – | nee |
| `33e685a4017f83ad` | ? | inner | 8 | @0 (100%) | – | – | – | – | – | nee |
| `66063d1201daebea` | ? | inner | 1 | @0 (100%) | – | – | – | – | – | nee |
| `6161d7905d92167c` | ExtendAccountEvent | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `e2d6f62107f293e5` | ? | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 0 | – | – | – | – | – | – | nee |

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.
Uitgesloten als bewijs: 299 transacties met meer dan twee partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan één event van dat type (297 transacties). In die gevallen is het netto saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de layout fout is.

**Geen layout vastgelegd**: de eis is niet gehaald. De bot leest dus géén AMM-trades in. Dat is opzet: liever geen data dan verkeerd gedecodeerde data.

