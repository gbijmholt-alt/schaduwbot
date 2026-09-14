# Wat is er van de tokens geworden? — 2026-09-14 18:26 UTC

71835 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 71835 | 3.7% (2638) | 15.7% (11301) | 80.6% (57896) | 4.5% (3194) |
| gescreend (ongeacht uitkomst) | 9583 | 20.5% (1961) | 10.5% (1006) | 69.0% (6616) | 33.3% (3194) |
| gescreend, houdercheck ok | 7705 | 17.5% (1349) | 12.0% (924) | 70.5% (5432) | 35.0% (2698) |
| gescreend, houdercheck gezakt | 1878 | 32.6% (612) | 4.4% (82) | 63.0% (1184) | 26.4% (496) |
| volledige screening gehaald | 1206 | 9.3% (112) | 14.9% (180) | 75.8% (914) | 38.2% (461) |
| volledige screening gezakt | 8377 | 22.1% (1849) | 9.9% (826) | 68.1% (5702) | 32.6% (2733) |
| volledige screening + X-link | 693 | 7.1% (49) | 15.9% (110) | 77.1% (534) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (2719 punten): startwaarde varieert (30.7%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (30.7%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 9530 | 0 | 0 | 0 | 9530 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 9530 | 0 | 0 | 0 | 9530 | – | – | – | – |
| gescreend, houdercheck ok | 7658 | 0 | 0 | 0 | 7658 | – | – | – | – |
| gescreend, houdercheck gezakt | 1872 | 0 | 0 | 0 | 1872 | – | – | – | – |
| volledige screening gehaald | 1205 | 0 | 0 | 0 | 1205 | – | – | – | – |
| volledige screening gezakt | 8325 | 0 | 0 | 0 | 8325 | – | – | – | – |
| volledige screening + X-link | 692 | 0 | 0 | 0 | 692 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 3536 opgehaald, 156 nog te gaan (400 deze run, 887 calls, 168 mislukte calls, 81 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

