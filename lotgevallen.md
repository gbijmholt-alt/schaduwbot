# Wat is er van de tokens geworden? — 2026-09-13 18:18 UTC

44777 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 44777 | 3.8% (1710) | 19.3% (8655) | 76.8% (34412) | 4.4% (1979) |
| gescreend (ongeacht uitkomst) | 6138 | 20.6% (1267) | 10.7% (656) | 68.7% (4215) | 32.2% (1979) |
| gescreend, houdercheck ok | 4584 | 17.6% (805) | 13.7% (627) | 68.8% (3152) | 34.3% (1571) |
| gescreend, houdercheck gezakt | 1554 | 29.7% (462) | 1.9% (29) | 68.4% (1063) | 26.2% (408) |
| volledige screening gehaald | 697 | 8.9% (62) | 21.1% (147) | 70.0% (488) | 31.4% (219) |
| volledige screening gezakt | 5441 | 22.1% (1205) | 9.3% (509) | 68.5% (3727) | 32.4% (1760) |
| volledige screening + X-link | 441 | 5.2% (23) | 20.9% (92) | 73.9% (326) | 22.7% (100) |

## Controle op de koers uit de keten

**IJking mislukt** (335 punten): startwaarde varieert (24.1%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (24.1%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 6019 | 0 | 0 | 0 | 6019 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 6019 | 0 | 0 | 0 | 6019 | – | – | – | – |
| gescreend, houdercheck ok | 4476 | 0 | 0 | 0 | 4476 | – | – | – | – |
| gescreend, houdercheck gezakt | 1543 | 0 | 0 | 0 | 1543 | – | – | – | – |
| volledige screening gehaald | 671 | 0 | 0 | 0 | 671 | – | – | – | – |
| volledige screening gezakt | 5348 | 0 | 0 | 0 | 5348 | – | – | – | – |
| volledige screening + X-link | 425 | 0 | 0 | 0 | 425 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 899 opgehaald, 0 nog te gaan (132 deze run, 264 calls, 0 mislukte calls, 0 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

