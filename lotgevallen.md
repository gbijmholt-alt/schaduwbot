# Wat is er van de tokens geworden? — 2026-09-14 10:09 UTC

61581 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 61581 | 3.8% (2338) | 12.0% (7373) | 84.2% (51870) | 4.4% (2691) |
| gescreend (ongeacht uitkomst) | 8198 | 21.1% (1733) | 7.0% (578) | 71.8% (5887) | 32.8% (2691) |
| gescreend, houdercheck ok | 6470 | 18.3% (1182) | 8.5% (551) | 73.2% (4737) | 34.8% (2251) |
| gescreend, houdercheck gezakt | 1728 | 31.9% (551) | 1.6% (27) | 66.5% (1150) | 25.5% (440) |
| volledige screening gehaald | 1007 | 9.4% (95) | 11.0% (111) | 79.5% (801) | 37.0% (373) |
| volledige screening gezakt | 7191 | 22.8% (1638) | 6.5% (467) | 70.7% (5086) | 32.2% (2318) |
| volledige screening + X-link | 573 | 6.3% (36) | 8.7% (50) | 85.0% (487) | 25.7% (147) |

## Controle op de koers uit de keten

**IJking mislukt** (2003 punten): startwaarde varieert (16.8%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (16.8%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 8127 | 0 | 0 | 0 | 8127 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 8127 | 0 | 0 | 0 | 8127 | – | – | – | – |
| gescreend, houdercheck ok | 6409 | 0 | 0 | 0 | 6409 | – | – | – | – |
| gescreend, houdercheck gezakt | 1718 | 0 | 0 | 0 | 1718 | – | – | – | – |
| volledige screening gehaald | 1001 | 0 | 0 | 0 | 1001 | – | – | – | – |
| volledige screening gezakt | 7126 | 0 | 0 | 0 | 7126 | – | – | – | – |
| volledige screening + X-link | 570 | 0 | 0 | 0 | 570 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 2498 opgehaald, 34 nog te gaan (143 deze run, 322 calls, 70 mislukte calls, 34 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

