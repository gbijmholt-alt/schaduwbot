# PumpSwap-dekking — 2026-09-12 09:59 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **45404 SOL** over 18017 posities. Hiervan gecheckt: 1198 posities (40277 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 1177 | 39413.9 |
| deels_verkocht | 15 | 657.8 |
| nog_in_bezit | 6 | 205.0 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **26646.6 SOL** tegen 604.6 SOL kostprijs (17 posities met prijs).

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | deels_verkocht | 2 | 1.9 |
| gevolgd | nog_in_bezit | 1 | 0.1 |
| gevolgd | verkocht | 105 | 255.4 |
| niet_gevolgd | deels_verkocht | 13 | 655.9 |
| niet_gevolgd | nog_in_bezit | 5 | 204.9 |
| niet_gevolgd | verkocht | 1072 | 39158.5 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 400 transacties opgehaald, 163 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |
|---|---|---|---|---|---|---|---|---|---|---|
| `c62e1552b4d9e870` | ? | inner | 2 | – | – | – | – | – | – | nee |
| `33e685a4017f83ad` | ? | inner | 2 | @0 (100%) | – | – | – | – | – | nee |
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `6161d7905d92167c` | ExtendAccountEvent | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 0 | – | – | – | – | – | – | nee |
| `e2d6f62107f293e5` | ? | inner_cpi+log | 0 | – | – | – | – | – | – | nee |

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.
Uitgesloten als bewijs: 172 transacties met meer dan twee partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan één event van dat type (163 transacties). In die gevallen is het netto saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de layout fout is.

**Geen layout vastgelegd**: de eis is niet gehaald. De bot leest dus géén AMM-trades in. Dat is opzet: liever geen data dan verkeerd gedecodeerde data.

