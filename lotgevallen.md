# Wat is er van de tokens geworden? — 2026-09-13 17:35 UTC

43955 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 43955 | 3.8% (1682) | 19.0% (8339) | 77.2% (33934) | 4.4% (1945) |
| gescreend (ongeacht uitkomst) | 6043 | 20.6% (1246) | 10.2% (617) | 69.2% (4180) | 32.2% (1945) |
| gescreend, houdercheck ok | 4498 | 17.5% (788) | 13.2% (592) | 69.3% (3118) | 34.2% (1537) |
| gescreend, houdercheck gezakt | 1545 | 29.6% (458) | 1.6% (25) | 68.7% (1062) | 26.4% (408) |
| volledige screening gehaald | 674 | 9.0% (61) | 19.6% (132) | 71.4% (481) | 31.6% (213) |
| volledige screening gezakt | 5369 | 22.1% (1185) | 9.0% (485) | 68.9% (3699) | 32.3% (1732) |
| volledige screening + X-link | 428 | 5.4% (23) | 19.6% (84) | 75.0% (321) | 23.1% (99) |

## Controle op de koers uit de keten

**IJking mislukt** (300 punten): startwaarde varieert (27.3%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (27.3%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 5920 | 0 | 0 | 0 | 5920 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 5920 | 0 | 0 | 0 | 5920 | – | – | – | – |
| gescreend, houdercheck ok | 4380 | 0 | 0 | 0 | 4380 | – | – | – | – |
| gescreend, houdercheck gezakt | 1540 | 0 | 0 | 0 | 1540 | – | – | – | – |
| volledige screening gehaald | 655 | 0 | 0 | 0 | 655 | – | – | – | – |
| volledige screening gezakt | 5265 | 0 | 0 | 0 | 5265 | – | – | – | – |
| volledige screening + X-link | 416 | 0 | 0 | 0 | 416 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 767 opgehaald, 55 nog te gaan (217 deze run, 492 calls, 113 mislukte calls, 55 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

