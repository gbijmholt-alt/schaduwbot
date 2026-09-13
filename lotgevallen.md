# Wat is er van de tokens geworden? — 2026-09-13 23:03 UTC

51218 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 51218 | 3.7% (1911) | 21.2% (10849) | 75.1% (38458) | 4.4% (2231) |
| gescreend (ongeacht uitkomst) | 6871 | 20.6% (1413) | 12.9% (885) | 66.6% (4573) | 32.5% (2231) |
| gescreend, houdercheck ok | 5263 | 17.6% (926) | 16.0% (843) | 66.4% (3494) | 34.4% (1810) |
| gescreend, houdercheck gezakt | 1608 | 30.3% (487) | 2.6% (42) | 67.1% (1079) | 26.2% (421) |
| volledige screening gehaald | 811 | 8.8% (71) | 23.4% (190) | 67.8% (550) | 33.4% (271) |
| volledige screening gezakt | 6060 | 22.1% (1342) | 11.5% (695) | 66.4% (4023) | 32.3% (1960) |
| volledige screening + X-link | 495 | 5.5% (27) | 20.0% (99) | 74.6% (369) | 23.8% (118) |

## Controle op de koers uit de keten

**IJking mislukt** (693 punten): startwaarde varieert (14.8%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (14.8%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 6768 | 0 | 0 | 0 | 6768 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 6768 | 0 | 0 | 0 | 6768 | – | – | – | – |
| gescreend, houdercheck ok | 5168 | 0 | 0 | 0 | 5168 | – | – | – | – |
| gescreend, houdercheck gezakt | 1600 | 0 | 0 | 0 | 1600 | – | – | – | – |
| volledige screening gehaald | 789 | 0 | 0 | 0 | 789 | – | – | – | – |
| volledige screening gezakt | 5979 | 0 | 0 | 0 | 5979 | – | – | – | – |
| volledige screening + X-link | 484 | 0 | 0 | 0 | 484 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 1407 opgehaald, 86 nog te gaan (294 deze run, 679 calls, 177 mislukte calls, 86 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

