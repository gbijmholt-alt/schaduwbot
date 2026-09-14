# Wat is er van de tokens geworden? — 2026-09-14 22:11 UTC

78876 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 78876 | 3.6% (2813) | 18.0% (14228) | 78.4% (61835) | 4.4% (3442) |
| gescreend (ongeacht uitkomst) | 10235 | 20.2% (2062) | 10.5% (1080) | 69.3% (7093) | 33.3% (3405) |
| gescreend, houdercheck ok | 8266 | 17.3% (1432) | 11.8% (978) | 70.8% (5856) | 34.9% (2885) |
| gescreend, houdercheck gezakt | 1969 | 32.0% (630) | 5.2% (102) | 62.8% (1237) | 26.4% (520) |
| volledige screening gehaald | 1206 | 9.3% (112) | 8.2% (99) | 82.5% (995) | 38.2% (461) |
| volledige screening gezakt | 9029 | 21.6% (1950) | 10.9% (981) | 67.5% (6098) | 32.6% (2944) |
| volledige screening + X-link | 693 | 7.1% (49) | 7.6% (53) | 85.3% (591) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (3192 punten): startwaarde varieert (28.5%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (28.5%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 10356 | 0 | 0 | 0 | 10356 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 10235 | 0 | 0 | 0 | 10235 | – | – | – | – |
| gescreend, houdercheck ok | 8266 | 0 | 0 | 0 | 8266 | – | – | – | – |
| gescreend, houdercheck gezakt | 1969 | 0 | 0 | 0 | 1969 | – | – | – | – |
| volledige screening gehaald | 1206 | 0 | 0 | 0 | 1206 | – | – | – | – |
| volledige screening gezakt | 9029 | 0 | 0 | 0 | 9029 | – | – | – | – |
| volledige screening + X-link | 693 | 0 | 0 | 0 | 693 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 4287 opgehaald, 98 nog te gaan (215 deze run, 533 calls, 201 mislukte calls, 98 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

