# Wat is er van de tokens geworden? — 2026-09-15 09:12 UTC

92447 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 92447 | 3.5% (3238) | 10.8% (9980) | 85.7% (79229) | 4.3% (3982) |
| gescreend (ongeacht uitkomst) | 12097 | 19.9% (2407) | 6.0% (724) | 74.1% (8966) | 32.8% (3970) |
| gescreend, houdercheck ok | 9914 | 17.2% (1708) | 6.7% (668) | 76.0% (7538) | 34.1% (3383) |
| gescreend, houdercheck gezakt | 2183 | 32.0% (699) | 2.6% (56) | 65.4% (1428) | 26.9% (587) |
| volledige screening gehaald | 1206 | 9.3% (112) | 0.0% (0) | 90.7% (1094) | 38.2% (461) |
| volledige screening gezakt | 10891 | 21.1% (2295) | 6.7% (724) | 72.3% (7872) | 32.2% (3509) |
| volledige screening + X-link | 693 | 7.1% (49) | 0.0% (0) | 92.9% (644) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (5057 punten): startwaarde varieert (14.7%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (14.7%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 12144 | 0 | 0 | 0 | 12144 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 12097 | 0 | 0 | 0 | 12097 | – | – | – | – |
| gescreend, houdercheck ok | 9914 | 0 | 0 | 0 | 9914 | – | – | – | – |
| gescreend, houdercheck gezakt | 2183 | 0 | 0 | 0 | 2183 | – | – | – | – |
| volledige screening gehaald | 1206 | 0 | 0 | 0 | 1206 | – | – | – | – |
| volledige screening gezakt | 10891 | 0 | 0 | 0 | 10891 | – | – | – | – |
| volledige screening + X-link | 693 | 0 | 0 | 0 | 693 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 5784 opgehaald, 53 nog te gaan (212 deze run, 480 calls, 109 mislukte calls, 53 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

