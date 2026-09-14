# Wat is er van de tokens geworden? — 2026-09-14 05:16 UTC

58178 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 58178 | 3.7% (2164) | 16.4% (9536) | 79.9% (46478) | 4.3% (2525) |
| gescreend (ongeacht uitkomst) | 7695 | 20.7% (1591) | 9.4% (722) | 69.9% (5382) | 32.8% (2525) |
| gescreend, houdercheck ok | 6018 | 17.8% (1074) | 11.4% (688) | 70.7% (4256) | 34.7% (2090) |
| gescreend, houdercheck gezakt | 1677 | 30.8% (517) | 2.0% (34) | 67.1% (1126) | 25.9% (435) |
| volledige screening gehaald | 944 | 9.0% (85) | 16.1% (152) | 74.9% (707) | 35.2% (332) |
| volledige screening gezakt | 6751 | 22.3% (1506) | 8.4% (570) | 69.2% (4675) | 32.5% (2193) |
| volledige screening + X-link | 545 | 5.9% (32) | 10.8% (59) | 83.3% (454) | 24.6% (134) |

## Controle op de koers uit de keten

**IJking mislukt** (1501 punten): startwaarde varieert (14.2%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (14.2%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 7630 | 0 | 0 | 0 | 7630 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 7630 | 0 | 0 | 0 | 7630 | – | – | – | – |
| gescreend, houdercheck ok | 5960 | 0 | 0 | 0 | 5960 | – | – | – | – |
| gescreend, houdercheck gezakt | 1670 | 0 | 0 | 0 | 1670 | – | – | – | – |
| volledige screening gehaald | 934 | 0 | 0 | 0 | 934 | – | – | – | – |
| volledige screening gezakt | 6696 | 0 | 0 | 0 | 6696 | – | – | – | – |
| volledige screening + X-link | 541 | 0 | 0 | 0 | 541 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 2157 opgehaald, 21 nog te gaan (219 deze run, 463 calls, 46 mislukte calls, 21 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

