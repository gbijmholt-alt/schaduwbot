# Wat is er van de tokens geworden? — 2026-09-14 16:20 UTC

67960 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 67960 | 3.8% (2553) | 13.4% (9078) | 82.9% (56329) | 4.5% (3045) |
| gescreend (ongeacht uitkomst) | 9176 | 20.7% (1896) | 9.3% (852) | 70.0% (6428) | 33.2% (3045) |
| gescreend, houdercheck ok | 7333 | 17.7% (1299) | 10.6% (777) | 71.7% (5257) | 34.9% (2563) |
| gescreend, houdercheck gezakt | 1843 | 32.4% (597) | 4.1% (75) | 63.5% (1171) | 26.2% (482) |
| volledige screening gehaald | 1158 | 9.2% (107) | 14.0% (162) | 76.8% (889) | 38.1% (441) |
| volledige screening gezakt | 8018 | 22.3% (1789) | 8.6% (690) | 69.1% (5539) | 32.5% (2604) |
| volledige screening + X-link | 666 | 6.8% (45) | 15.0% (100) | 78.2% (521) | 25.8% (172) |

## Controle op de koers uit de keten

**IJking mislukt** (2535 punten): startwaarde varieert (26.9%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (26.9%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 9080 | 0 | 0 | 0 | 9080 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 9080 | 0 | 0 | 0 | 9080 | – | – | – | – |
| gescreend, houdercheck ok | 7251 | 0 | 0 | 0 | 7251 | – | – | – | – |
| gescreend, houdercheck gezakt | 1829 | 0 | 0 | 0 | 1829 | – | – | – | – |
| volledige screening gehaald | 1152 | 0 | 0 | 0 | 1152 | – | – | – | – |
| volledige screening gezakt | 7928 | 0 | 0 | 0 | 7928 | – | – | – | – |
| volledige screening + X-link | 662 | 0 | 0 | 0 | 662 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 3217 opgehaald, 100 nog te gaan (374 deze run, 854 calls, 206 mislukte calls, 100 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

