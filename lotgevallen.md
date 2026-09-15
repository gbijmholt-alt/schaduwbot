# Wat is er van de tokens geworden? — 2026-09-15 08:12 UTC

91431 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 91431 | 3.5% (3204) | 11.1% (10160) | 85.4% (78067) | 4.3% (3930) |
| gescreend (ongeacht uitkomst) | 11927 | 19.9% (2378) | 5.8% (694) | 74.2% (8855) | 32.8% (3910) |
| gescreend, houdercheck ok | 9766 | 17.3% (1689) | 6.6% (643) | 76.1% (7434) | 34.1% (3333) |
| gescreend, houdercheck gezakt | 2161 | 31.9% (689) | 2.4% (51) | 65.8% (1421) | 26.7% (577) |
| volledige screening gehaald | 1206 | 9.3% (112) | 0.0% (0) | 90.7% (1094) | 38.2% (461) |
| volledige screening gezakt | 10721 | 21.1% (2266) | 6.5% (694) | 72.4% (7761) | 32.2% (3449) |
| volledige screening + X-link | 693 | 7.1% (49) | 0.0% (0) | 92.9% (644) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (4946 punten): startwaarde varieert (15.5%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (15.5%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 11991 | 0 | 0 | 0 | 11991 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 11927 | 0 | 0 | 0 | 11927 | – | – | – | – |
| gescreend, houdercheck ok | 9766 | 0 | 0 | 0 | 9766 | – | – | – | – |
| gescreend, houdercheck gezakt | 2161 | 0 | 0 | 0 | 2161 | – | – | – | – |
| volledige screening gehaald | 1206 | 0 | 0 | 0 | 1206 | – | – | – | – |
| volledige screening gezakt | 10721 | 0 | 0 | 0 | 10721 | – | – | – | – |
| volledige screening + X-link | 693 | 0 | 0 | 0 | 693 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 5625 opgehaald, 80 nog te gaan (295 deze run, 677 calls, 167 mislukte calls, 80 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

