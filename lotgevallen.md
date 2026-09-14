# Wat is er van de tokens geworden? — 2026-09-14 01:08 UTC

53793 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 53793 | 3.7% (1993) | 20.0% (10740) | 76.3% (41060) | 4.3% (2329) |
| gescreend (ongeacht uitkomst) | 7161 | 20.4% (1464) | 12.1% (869) | 67.4% (4828) | 32.5% (2329) |
| gescreend, houdercheck ok | 5531 | 17.5% (970) | 14.9% (824) | 67.6% (3737) | 34.4% (1901) |
| gescreend, houdercheck gezakt | 1630 | 30.3% (494) | 2.8% (45) | 66.9% (1091) | 26.3% (428) |
| volledige screening gehaald | 853 | 8.9% (76) | 20.9% (178) | 70.2% (599) | 33.7% (287) |
| volledige screening gezakt | 6308 | 22.0% (1388) | 10.9% (691) | 67.0% (4229) | 32.4% (2042) |
| volledige screening + X-link | 514 | 5.5% (28) | 16.5% (85) | 78.0% (401) | 23.5% (121) |

## Controle op de koers uit de keten

**IJking mislukt** (948 punten): startwaarde varieert (6.8%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (6.8%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 7078 | 0 | 0 | 0 | 7078 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 7078 | 0 | 0 | 0 | 7078 | – | – | – | – |
| gescreend, houdercheck ok | 5451 | 0 | 0 | 0 | 5451 | – | – | – | – |
| gescreend, houdercheck gezakt | 1627 | 0 | 0 | 0 | 1627 | – | – | – | – |
| volledige screening gehaald | 843 | 0 | 0 | 0 | 843 | – | – | – | – |
| volledige screening gezakt | 6235 | 0 | 0 | 0 | 6235 | – | – | – | – |
| volledige screening + X-link | 509 | 0 | 0 | 0 | 509 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 1663 opgehaald, 87 nog te gaan (343 deze run, 778 calls, 179 mislukte calls, 87 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

