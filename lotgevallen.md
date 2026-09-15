# Wat is er van de tokens geworden? — 2026-09-15 04:24 UTC

87724 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 87724 | 3.5% (3056) | 13.7% (12049) | 82.8% (72619) | 4.3% (3756) |
| gescreend (ongeacht uitkomst) | 11293 | 19.8% (2235) | 6.9% (784) | 73.3% (8274) | 33.0% (3721) |
| gescreend, houdercheck ok | 9203 | 17.1% (1573) | 7.8% (715) | 75.1% (6915) | 34.4% (3169) |
| gescreend, houdercheck gezakt | 2090 | 31.7% (662) | 3.3% (69) | 65.0% (1359) | 26.4% (552) |
| volledige screening gehaald | 1206 | 9.3% (112) | 0.2% (3) | 90.5% (1091) | 38.2% (461) |
| volledige screening gezakt | 10087 | 21.1% (2123) | 7.7% (781) | 71.2% (7183) | 32.3% (3260) |
| volledige screening + X-link | 693 | 7.1% (49) | 0.1% (1) | 92.8% (643) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (4365 punten): startwaarde varieert (16.9%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (16.9%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 11430 | 0 | 0 | 0 | 11430 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 11293 | 0 | 0 | 0 | 11293 | – | – | – | – |
| gescreend, houdercheck ok | 9203 | 0 | 0 | 0 | 9203 | – | – | – | – |
| gescreend, houdercheck gezakt | 2090 | 0 | 0 | 0 | 2090 | – | – | – | – |
| volledige screening gehaald | 1206 | 0 | 0 | 0 | 1206 | – | – | – | – |
| volledige screening gezakt | 10087 | 0 | 0 | 0 | 10087 | – | – | – | – |
| volledige screening + X-link | 693 | 0 | 0 | 0 | 693 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 5216 opgehaald, 42 nog te gaan (356 deze run, 763 calls, 93 mislukte calls, 42 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

