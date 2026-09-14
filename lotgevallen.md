# Wat is er van de tokens geworden? — 2026-09-14 21:19 UTC

77310 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 77310 | 3.6% (2773) | 17.9% (13808) | 78.5% (60729) | 4.4% (3391) |
| gescreend (ongeacht uitkomst) | 10089 | 20.2% (2040) | 10.8% (1086) | 69.0% (6963) | 33.4% (3369) |
| gescreend, houdercheck ok | 8136 | 17.4% (1416) | 12.0% (980) | 70.5% (5740) | 35.1% (2854) |
| gescreend, houdercheck gezakt | 1953 | 31.9% (624) | 5.4% (106) | 62.6% (1223) | 26.4% (515) |
| volledige screening gehaald | 1206 | 9.3% (112) | 10.0% (121) | 80.7% (973) | 38.2% (461) |
| volledige screening gezakt | 8883 | 21.7% (1928) | 10.9% (965) | 67.4% (5990) | 32.7% (2908) |
| volledige screening + X-link | 693 | 7.1% (49) | 10.1% (70) | 82.8% (574) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (3062 punten): startwaarde varieert (29.6%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (29.6%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 10169 | 0 | 0 | 0 | 10169 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 10089 | 0 | 0 | 0 | 10089 | – | – | – | – |
| gescreend, houdercheck ok | 8136 | 0 | 0 | 0 | 8136 | – | – | – | – |
| gescreend, houdercheck gezakt | 1953 | 0 | 0 | 0 | 1953 | – | – | – | – |
| volledige screening gehaald | 1206 | 0 | 0 | 0 | 1206 | – | – | – | – |
| volledige screening gezakt | 8883 | 0 | 0 | 0 | 8883 | – | – | – | – |
| volledige screening + X-link | 693 | 0 | 0 | 0 | 693 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 4170 opgehaald, 55 nog te gaan (337 deze run, 737 calls, 118 mislukte calls, 55 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

