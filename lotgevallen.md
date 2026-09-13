# Wat is er van de tokens geworden? — 2026-09-13 20:21 UTC

47606 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 47606 | 3.8% (1805) | 20.4% (9723) | 75.8% (36078) | 4.4% (2081) |
| gescreend (ongeacht uitkomst) | 6437 | 20.8% (1336) | 11.6% (748) | 67.6% (4353) | 32.3% (2081) |
| gescreend, houdercheck ok | 4861 | 17.7% (860) | 14.8% (720) | 67.5% (3281) | 34.4% (1671) |
| gescreend, houdercheck gezakt | 1576 | 30.2% (476) | 1.8% (28) | 68.0% (1072) | 26.0% (410) |
| volledige screening gehaald | 740 | 9.0% (67) | 20.5% (152) | 70.4% (521) | 32.8% (243) |
| volledige screening gezakt | 5697 | 22.3% (1269) | 10.5% (596) | 67.3% (3832) | 32.3% (1838) |
| volledige screening + X-link | 465 | 5.4% (25) | 18.5% (86) | 76.1% (354) | 23.4% (109) |

## Controle op de koers uit de keten

**IJking mislukt** (473 punten): startwaarde varieert (10.5%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (10.5%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 6349 | 0 | 0 | 0 | 6349 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 6349 | 0 | 0 | 0 | 6349 | – | – | – | – |
| gescreend, houdercheck ok | 4779 | 0 | 0 | 0 | 4779 | – | – | – | – |
| gescreend, houdercheck gezakt | 1570 | 0 | 0 | 0 | 1570 | – | – | – | – |
| volledige screening gehaald | 732 | 0 | 0 | 0 | 732 | – | – | – | – |
| volledige screening gezakt | 5617 | 0 | 0 | 0 | 5617 | – | – | – | – |
| volledige screening + X-link | 459 | 0 | 0 | 0 | 459 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 1120 opgehaald, 32 nog te gaan (253 deze run, 549 calls, 75 mislukte calls, 32 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

