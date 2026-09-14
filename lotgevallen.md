# Wat is er van de tokens geworden? — 2026-09-14 20:30 UTC

75565 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 75565 | 3.6% (2735) | 17.2% (12985) | 79.2% (59845) | 4.4% (3330) |
| gescreend (ongeacht uitkomst) | 9948 | 20.3% (2021) | 10.6% (1053) | 69.1% (6874) | 33.4% (3322) |
| gescreend, houdercheck ok | 8014 | 17.5% (1402) | 11.8% (950) | 70.7% (5662) | 35.1% (2812) |
| gescreend, houdercheck gezakt | 1934 | 32.0% (619) | 5.3% (103) | 62.7% (1212) | 26.4% (510) |
| volledige screening gehaald | 1206 | 9.3% (112) | 11.2% (135) | 79.5% (959) | 38.2% (461) |
| volledige screening gezakt | 8742 | 21.8% (1909) | 10.5% (918) | 67.7% (5915) | 32.7% (2861) |
| volledige screening + X-link | 693 | 7.1% (49) | 10.8% (75) | 82.1% (569) | 25.8% (179) |

## Controle op de koers uit de keten

**IJking mislukt** (2974 punten): startwaarde varieert (30.6%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (30.6%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 9981 | 0 | 0 | 0 | 9981 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 9948 | 0 | 0 | 0 | 9948 | – | – | – | – |
| gescreend, houdercheck ok | 8014 | 0 | 0 | 0 | 8014 | – | – | – | – |
| gescreend, houdercheck gezakt | 1934 | 0 | 0 | 0 | 1934 | – | – | – | – |
| volledige screening gehaald | 1206 | 0 | 0 | 0 | 1206 | – | – | – | – |
| volledige screening gezakt | 8742 | 0 | 0 | 0 | 8742 | – | – | – | – |
| volledige screening + X-link | 693 | 0 | 0 | 0 | 693 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 3888 opgehaald, 175 nog te gaan (400 deze run, 855 calls, 103 mislukte calls, 48 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

