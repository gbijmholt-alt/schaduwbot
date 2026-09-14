# Wat is er van de tokens geworden? — 2026-09-14 14:15 UTC

65309 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 65309 | 3.8% (2462) | 12.5% (8172) | 83.7% (54675) | 4.5% (2914) |
| gescreend (ongeacht uitkomst) | 8814 | 20.7% (1824) | 8.5% (747) | 70.8% (6243) | 33.1% (2914) |
| gescreend, houdercheck ok | 7014 | 17.7% (1242) | 9.8% (689) | 72.5% (5083) | 34.9% (2449) |
| gescreend, houdercheck gezakt | 1800 | 32.3% (582) | 3.2% (58) | 64.4% (1160) | 25.8% (465) |
| volledige screening gehaald | 1106 | 9.2% (102) | 12.2% (135) | 78.6% (869) | 37.2% (412) |
| volledige screening gezakt | 7708 | 22.3% (1722) | 7.9% (612) | 69.7% (5374) | 32.5% (2502) |
| volledige screening + X-link | 639 | 6.6% (42) | 13.0% (83) | 80.4% (514) | 25.7% (164) |

## Controle op de koers uit de keten

**IJking mislukt** (2353 punten): startwaarde varieert (20.3%), model klopt niet. De koers van vandaag wordt daarom niet berekend.

**De koers uit de keten wordt niet gebruikt**: ijking mislukt: startwaarde varieert (20.3%), model klopt niet (0 controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

Gemigreerde tokens krijgen hun koers uit de AMM-pool, mits die pool bij de keten is opgevraagd en de prijs de controle haalde. Lukt dat nog niet, dan staat het token in de kolom 'gemigreerd zonder koers' — en omdat dat juist de groep is die het goed deed, is het cijfer dan een ondergrens.

| niveau | tokens met top | koers bekend | waarvan uit de pool | gemigreerd zonder koers | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|---|
| alle tokens | 8714 | 0 | 0 | 0 | 8714 | – | – | – | – |
| gescreend (ongeacht uitkomst) | 8714 | 0 | 0 | 0 | 8714 | – | – | – | – |
| gescreend, houdercheck ok | 6926 | 0 | 0 | 0 | 6926 | – | – | – | – |
| gescreend, houdercheck gezakt | 1788 | 0 | 0 | 0 | 1788 | – | – | – | – |
| volledige screening gehaald | 1088 | 0 | 0 | 0 | 1088 | – | – | – | – |
| volledige screening gezakt | 7626 | 0 | 0 | 0 | 7626 | – | – | – | – |
| volledige screening + X-link | 628 | 0 | 0 | 0 | 628 | – | – | – | – |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 0 bruikbaar, 2943 opgehaald, 78 nog te gaan (322 deze run, 732 calls, 166 mislukte calls, 78 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

