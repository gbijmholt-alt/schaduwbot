# Wat is er van de tokens geworden? — 2026-09-15 06:10 UTC

89564 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 89564 | 3.5% (3123) | 12.6% (11245) | 84.0% (75196) | 4.3% (3831) |
| gescreend (ongeacht uitkomst) | 11585 | 19.9% (2303) | 5.8% (673) | 74.3% (8609) | 32.8% (3800) |
| gescreend, houdercheck ok | 9467 | 17.2% (1633) | 6.6% (627) | 76.1% (7207) | 34.2% (3239) |
| gescreend, houdercheck gezakt | 2118 | 31.6% (670) | 2.2% (46) | 66.2% (1402) | 26.5% (561) |
| volledige screening gehaald | 1206 | 9.3% (112) | 0.0% (0) | 90.7% (1094) | 38.2% (461) |
| volledige screening gezakt | 10379 | 21.1% (2191) | 6.5% (673) | 72.4% (7515) | 32.2% (3339) |
| volledige screening + X-link | 693 | 7.1% (49) | 0.0% (0) | 92.9% (644) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (4700 punten): startwaarde varieert (16.8%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (16.8%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 11697 | 0 | 0 | 0 | 11697 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 11585 | 0 | 0 | 0 | 11585 | – | – | – | – |
| gescreend, houdercheck ok | 9467 | 0 | 0 | 0 | 9467 | – | – | – | – |
| gescreend, houdercheck gezakt | 2118 | 0 | 0 | 0 | 2118 | – | – | – | – |
| volledige screening gehaald | 1206 | 0 | 0 | 0 | 1206 | – | – | – | – |
| volledige screening gezakt | 10379 | 0 | 0 | 0 | 10379 | – | – | – | – |
| volledige screening + X-link | 693 | 0 | 0 | 0 | 693 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 5410 opgehaald, 63 nog te gaan (257 deze run, 582 calls, 131 mislukte calls, 63 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

