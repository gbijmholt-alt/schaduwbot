# Wat is er van de tokens geworden? — 2026-09-14 06:03 UTC

58643 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 58643 | 3.8% (2200) | 15.4% (9052) | 80.8% (47391) | 4.3% (2552) |
| gescreend (ongeacht uitkomst) | 7773 | 20.8% (1617) | 8.7% (678) | 70.5% (5478) | 32.8% (2552) |
| gescreend, houdercheck ok | 6090 | 18.0% (1097) | 10.6% (645) | 71.4% (4348) | 34.7% (2115) |
| gescreend, houdercheck gezakt | 1683 | 30.9% (520) | 2.0% (33) | 67.1% (1130) | 26.0% (437) |
| volledige screening gehaald | 952 | 9.0% (86) | 14.6% (139) | 76.4% (727) | 35.4% (337) |
| volledige screening gezakt | 6821 | 22.4% (1531) | 7.9% (539) | 69.7% (4751) | 32.5% (2215) |
| volledige screening + X-link | 546 | 5.9% (32) | 9.3% (51) | 84.8% (463) | 24.7% (135) |

## Controle op de koers uit de keten

**IJking mislukt** (1597 punten): startwaarde varieert (14.5%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (14.5%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 7710 | 0 | 0 | 0 | 7710 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 7710 | 0 | 0 | 0 | 7710 | – | – | – | – |
| gescreend, houdercheck ok | 6032 | 0 | 0 | 0 | 6032 | – | – | – | – |
| gescreend, houdercheck gezakt | 1678 | 0 | 0 | 0 | 1678 | – | – | – | – |
| volledige screening gehaald | 946 | 0 | 0 | 0 | 946 | – | – | – | – |
| volledige screening gezakt | 6764 | 0 | 0 | 0 | 6764 | – | – | – | – |
| volledige screening + X-link | 546 | 0 | 0 | 0 | 546 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 2218 opgehaald, 19 nog te gaan (80 deze run, 179 calls, 38 mislukte calls, 19 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

