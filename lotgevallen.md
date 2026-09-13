# Wat is er van de tokens geworden? — 2026-09-13 20:54 UTC

48407 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 48407 | 3.8% (1831) | 20.8% (10061) | 75.4% (36515) | 4.3% (2104) |
| gescreend (ongeacht uitkomst) | 6533 | 20.8% (1356) | 12.1% (790) | 67.2% (4387) | 32.2% (2104) |
| gescreend, houdercheck ok | 4952 | 17.7% (877) | 15.4% (761) | 66.9% (3314) | 34.2% (1693) |
| gescreend, houdercheck gezakt | 1581 | 30.3% (479) | 1.8% (29) | 67.9% (1073) | 26.0% (411) |
| volledige screening gehaald | 757 | 9.0% (68) | 22.1% (167) | 69.0% (522) | 32.4% (245) |
| volledige screening gezakt | 5776 | 22.3% (1288) | 10.8% (623) | 66.9% (3865) | 32.2% (1859) |
| volledige screening + X-link | 470 | 5.3% (25) | 19.4% (91) | 75.3% (354) | 23.2% (109) |

## Controle op de koers uit de keten

**IJking mislukt** (507 punten): startwaarde varieert (12.6%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (12.6%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 6420 | 0 | 0 | 0 | 6420 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 6420 | 0 | 0 | 0 | 6420 | – | – | – | – |
| gescreend, houdercheck ok | 4846 | 0 | 0 | 0 | 4846 | – | – | – | – |
| gescreend, houdercheck gezakt | 1574 | 0 | 0 | 0 | 1574 | – | – | – | – |
| volledige screening gehaald | 738 | 0 | 0 | 0 | 738 | – | – | – | – |
| volledige screening gezakt | 5682 | 0 | 0 | 0 | 5682 | – | – | – | – |
| volledige screening + X-link | 464 | 0 | 0 | 0 | 464 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 1199 opgehaald, 10 nog te gaan (89 deze run, 188 calls, 20 mislukte calls, 10 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

