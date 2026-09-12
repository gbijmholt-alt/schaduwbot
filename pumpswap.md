# PumpSwap-dekking — 2026-09-12 09:49 UTC

Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.

## 1. Open posities in gemigreerde tokens

Totaal open (SOL erin min eruit op de curve): **49324 SOL** over 18543 posities. Hiervan gecheckt: 800 posities (35531 SOL).

| status nu | posities | open SOL |
|---|---|---|
| verkocht | 786 | 34708.2 |
| deels_verkocht | 10 | 630.2 |
| nog_in_bezit | 4 | 192.5 |

Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **26472.8 SOL** tegen 564.5 SOL kostprijs (10 posities met prijs).

| groep | status | posities | open SOL |
|---|---|---|---|
| gevolgd | deels_verkocht | 2 | 1.9 |
| gevolgd | nog_in_bezit | 1 | 0.1 |
| gevolgd | verkocht | 105 | 255.4 |
| niet_gevolgd | deels_verkocht | 8 | 628.3 |
| niet_gevolgd | nog_in_bezit | 3 | 192.5 |
| niet_gevolgd | verkocht | 681 | 34452.8 |

kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. 'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.

## 2. Layout-verificatie van het AMM-programma

Programma `pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA`. 120 transacties opgehaald, 107 bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). Eis om een layout vast te stellen: match ≥ 95% over ≥ 50 voorbeelden.

| discriminator | naam | waar | n | tokens | lamports | mint | user | vastgesteld |
|---|---|---|---|---|---|---|---|---|
| `67f4521f2cf57777` | BuyEvent | inner_cpi+log | 130 | @8 (55%) | @96 (55%) | – | @144 (80%) | nee |
| `3e2f370aa503dc2a` | SellEvent | inner_cpi+log | 106 | @96 (62%) | @8 (62%) | – | @112 (68%) | nee |
| `929fbdac925838f4` | ? | inner_cpi+log | 2 | – | – | – | @0 (100%) | nee |
| `c62e1552b4d9e870` | ? | inner | 2 | – | – | – | – | nee |
| `33e685a4017f83ad` | ? | inner | 2 | @0 (100%) | – | – | – | nee |

`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen niet in de logs en is een andere bron nodig.

**Geen layout vastgelegd**: de eis is niet gehaald. De bot leest dus géén AMM-trades in. Dat is opzet: liever geen data dan verkeerd gedecodeerde data.

