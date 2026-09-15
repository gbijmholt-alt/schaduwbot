# Wat is er van de tokens geworden? — 2026-09-15 00:15 UTC

82241 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 82241 | 3.5% (2892) | 16.9% (13872) | 79.6% (65477) | 4.4% (3583) |
| gescreend (ongeacht uitkomst) | 10595 | 20.0% (2118) | 9.1% (964) | 70.9% (7513) | 33.3% (3526) |
| gescreend, houdercheck ok | 8591 | 17.2% (1479) | 10.1% (867) | 72.7% (6245) | 34.9% (2996) |
| gescreend, houdercheck gezakt | 2004 | 31.9% (639) | 4.8% (97) | 63.3% (1268) | 26.5% (530) |
| volledige screening gehaald | 1206 | 9.3% (112) | 2.6% (31) | 88.1% (1063) | 38.2% (461) |
| volledige screening gezakt | 9389 | 21.4% (2006) | 9.9% (933) | 68.7% (6450) | 32.6% (3065) |
| volledige screening + X-link | 693 | 7.1% (49) | 2.5% (17) | 90.5% (627) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (3612 punten): startwaarde varieert (26.0%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (26.0%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 10797 | 0 | 0 | 0 | 10797 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 10595 | 0 | 0 | 0 | 10595 | – | – | – | – |
| gescreend, houdercheck ok | 8591 | 0 | 0 | 0 | 8591 | – | – | – | – |
| gescreend, houdercheck gezakt | 2004 | 0 | 0 | 0 | 2004 | – | – | – | – |
| volledige screening gehaald | 1206 | 0 | 0 | 0 | 1206 | – | – | – | – |
| volledige screening gezakt | 9389 | 0 | 0 | 0 | 9389 | – | – | – | – |
| volledige screening + X-link | 693 | 0 | 0 | 0 | 693 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 4637 opgehaald, 125 nog te gaan (400 deze run, 860 calls, 110 mislukte calls, 50 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

