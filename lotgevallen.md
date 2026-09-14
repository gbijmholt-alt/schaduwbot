# Wat is er van de tokens geworden? — 2026-09-14 08:07 UTC

60009 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 60009 | 3.8% (2266) | 13.4% (8017) | 82.9% (49726) | 4.4% (2634) |
| gescreend (ongeacht uitkomst) | 7988 | 21.0% (1674) | 7.5% (600) | 71.5% (5714) | 33.0% (2634) |
| gescreend, houdercheck ok | 6290 | 18.2% (1145) | 9.1% (570) | 72.7% (4575) | 34.9% (2195) |
| gescreend, houdercheck gezakt | 1698 | 31.1% (529) | 1.8% (30) | 67.1% (1139) | 25.9% (439) |
| volledige screening gehaald | 982 | 9.3% (91) | 13.0% (128) | 77.7% (763) | 36.1% (355) |
| volledige screening gezakt | 7006 | 22.6% (1583) | 6.7% (472) | 70.7% (4951) | 32.5% (2279) |
| volledige screening + X-link | 563 | 6.2% (35) | 8.9% (50) | 84.9% (478) | 25.2% (142) |

## Controle op de koers uit de keten

**IJking mislukt** (1830 punten): startwaarde varieert (19.7%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (19.7%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 7931 | 0 | 0 | 0 | 7931 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 7931 | 0 | 0 | 0 | 7931 | – | – | – | – |
| gescreend, houdercheck ok | 6237 | 0 | 0 | 0 | 6237 | – | – | – | – |
| gescreend, houdercheck gezakt | 1694 | 0 | 0 | 0 | 1694 | – | – | – | – |
| volledige screening gehaald | 973 | 0 | 0 | 0 | 973 | – | – | – | – |
| volledige screening gezakt | 6958 | 0 | 0 | 0 | 6958 | – | – | – | – |
| volledige screening + X-link | 558 | 0 | 0 | 0 | 558 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 2389 opgehaald, 0 nog te gaan (171 deze run, 343 calls, 1 mislukte calls, 0 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

