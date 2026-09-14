# Wat is er van de tokens geworden? — 2026-09-14 03:10 UTC

56334 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 56334 | 3.7% (2081) | 18.8% (10568) | 77.5% (43685) | 4.3% (2438) |
| gescreend (ongeacht uitkomst) | 7463 | 20.5% (1528) | 11.7% (872) | 67.8% (5063) | 32.7% (2438) |
| gescreend, houdercheck ok | 5809 | 17.6% (1025) | 14.1% (821) | 68.2% (3963) | 34.5% (2007) |
| gescreend, houdercheck gezakt | 1654 | 30.4% (503) | 3.1% (51) | 66.5% (1100) | 26.1% (431) |
| volledige screening gehaald | 899 | 9.1% (82) | 19.8% (178) | 71.1% (639) | 34.0% (306) |
| volledige screening gezakt | 6564 | 22.0% (1446) | 10.6% (694) | 67.4% (4424) | 32.5% (2132) |
| volledige screening + X-link | 534 | 6.0% (32) | 14.8% (79) | 79.2% (423) | 24.0% (128) |

## Controle op de koers uit de keten

**IJking mislukt** (1182 punten): startwaarde varieert (10.2%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (10.2%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 7367 | 0 | 0 | 0 | 7367 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 7367 | 0 | 0 | 0 | 7367 | – | – | – | – |
| gescreend, houdercheck ok | 5726 | 0 | 0 | 0 | 5726 | – | – | – | – |
| gescreend, houdercheck gezakt | 1641 | 0 | 0 | 0 | 1641 | – | – | – | – |
| volledige screening gehaald | 886 | 0 | 0 | 0 | 886 | – | – | – | – |
| volledige screening gezakt | 6481 | 0 | 0 | 0 | 6481 | – | – | – | – |
| volledige screening + X-link | 528 | 0 | 0 | 0 | 528 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 1959 opgehaald, 25 nog te gaan (321 deze run, 669 calls, 52 mislukte calls, 25 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

