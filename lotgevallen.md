# Wat is er van de tokens geworden? — 2026-09-15 02:21 UTC

85106 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 85106 | 3.5% (2977) | 15.5% (13226) | 81.0% (68903) | 4.3% (3682) |
| gescreend (ongeacht uitkomst) | 10954 | 19.9% (2175) | 8.2% (896) | 72.0% (7883) | 33.2% (3638) |
| gescreend, houdercheck ok | 8892 | 17.1% (1523) | 9.1% (810) | 73.8% (6559) | 34.8% (3091) |
| gescreend, houdercheck gezakt | 2062 | 31.6% (652) | 4.2% (86) | 64.2% (1324) | 26.5% (547) |
| volledige screening gehaald | 1206 | 9.3% (112) | 1.1% (13) | 89.6% (1081) | 38.2% (461) |
| volledige screening gezakt | 9748 | 21.2% (2063) | 9.1% (883) | 69.8% (6802) | 32.6% (3177) |
| volledige screening + X-link | 693 | 7.1% (49) | 1.1% (8) | 91.8% (636) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (3982 punten): startwaarde varieert (19.7%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (19.7%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 11133 | 0 | 0 | 0 | 11133 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 10954 | 0 | 0 | 0 | 10954 | – | – | – | – |
| gescreend, houdercheck ok | 8892 | 0 | 0 | 0 | 8892 | – | – | – | – |
| gescreend, houdercheck gezakt | 2062 | 0 | 0 | 0 | 2062 | – | – | – | – |
| volledige screening gehaald | 1206 | 0 | 0 | 0 | 1206 | – | – | – | – |
| volledige screening gezakt | 9748 | 0 | 0 | 0 | 9748 | – | – | – | – |
| volledige screening + X-link | 693 | 0 | 0 | 0 | 693 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 4902 opgehaald, 131 nog te gaan (396 deze run, 932 calls, 271 mislukte calls, 131 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

