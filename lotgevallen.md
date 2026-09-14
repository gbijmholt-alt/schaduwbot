# Wat is er van de tokens geworden? — 2026-09-14 12:14 UTC

63389 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 63389 | 3.8% (2388) | 12.2% (7747) | 84.0% (53254) | 4.4% (2791) |
| gescreend (ongeacht uitkomst) | 8469 | 20.9% (1772) | 7.7% (654) | 71.4% (6043) | 33.0% (2791) |
| gescreend, houdercheck ok | 6717 | 17.9% (1205) | 9.3% (625) | 72.8% (4887) | 34.8% (2341) |
| gescreend, houdercheck gezakt | 1752 | 32.4% (567) | 1.7% (29) | 66.0% (1156) | 25.7% (450) |
| volledige screening gehaald | 1049 | 9.4% (99) | 12.5% (131) | 78.1% (819) | 37.0% (388) |
| volledige screening gezakt | 7420 | 22.6% (1673) | 7.0% (523) | 70.4% (5224) | 32.4% (2403) |
| volledige screening + X-link | 602 | 6.6% (40) | 10.6% (64) | 82.7% (498) | 25.4% (153) |

## Controle op de koers uit de keten

**IJking mislukt** (2159 punten): startwaarde varieert (15.7%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (15.7%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 8397 | 0 | 0 | 0 | 8397 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 8397 | 0 | 0 | 0 | 8397 | – | – | – | – |
| gescreend, houdercheck ok | 6652 | 0 | 0 | 0 | 6652 | – | – | – | – |
| gescreend, houdercheck gezakt | 1745 | 0 | 0 | 0 | 1745 | – | – | – | – |
| volledige screening gehaald | 1039 | 0 | 0 | 0 | 1039 | – | – | – | – |
| volledige screening gezakt | 7358 | 0 | 0 | 0 | 7358 | – | – | – | – |
| volledige screening + X-link | 596 | 0 | 0 | 0 | 596 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 2699 opgehaald, 60 nog te gaan (261 deze run, 588 calls, 126 mislukte calls, 60 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

