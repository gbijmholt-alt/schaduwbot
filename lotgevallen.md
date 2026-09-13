# Wat is er van de tokens geworden? — 2026-09-13 13:06 UTC

39032 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 39032 | 3.9% (1513) | 15.1% (5879) | 81.1% (31640) | 4.5% (1755) |
| gescreend (ongeacht uitkomst) | 5485 | 20.5% (1124) | 6.7% (365) | 72.9% (3996) | 32.0% (1755) |
| gescreend, houdercheck ok | 3977 | 17.2% (683) | 8.9% (353) | 74.0% (2941) | 34.0% (1351) |
| gescreend, houdercheck gezakt | 1508 | 29.2% (441) | 0.8% (12) | 70.0% (1055) | 26.8% (404) |
| volledige screening gehaald | 591 | 8.8% (52) | 13.9% (82) | 77.3% (457) | 29.3% (173) |
| volledige screening gezakt | 4894 | 21.9% (1072) | 5.8% (283) | 72.3% (3539) | 32.3% (1582) |
| volledige screening + X-link | 387 | 5.2% (20) | 14.0% (54) | 80.9% (313) | 22.2% (86) |

## Controle op de koers uit de keten

**IJking geslaagd.** Bij 100 dode curve-tokens is gemeten hoeveel virtuele SOL de curve bij de start meetelt: **30.00 SOL**, met een spreiding van 0.0% tussen tokens. Die waarde is dus niet aangenomen maar gemeten, en omdat hij bij alle tokens hetzelfde uitkomt klopt het model.

Bij 100 dode curve-tokens — waar de koers sinds onze laatste waarneming niet meer bewogen kán zijn — wijkt de uit de keten afgeleide koers mediaan **16.2%** af. Binnen de marge van 25%, dus de koers wordt gebruikt.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

**Gemigreerde tokens zitten er niet in.** Hun curve is leeg en hun koers staat in een AMM-pool die we nog niet betrouwbaar uitlezen. Dat is juist de groep die het goed deed, dus deze cijfers zijn een ondergrens en geen schatting van wat vasthouden opbrengt.

| niveau | tokens met top | koers bekend | gemigreerd (geen koers) | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|
| alle tokens | 5392 | 4212 | 1100 | 80 | -49.8% | -72.4% | 22% | 20% |
| gescreend (ongeacht uitkomst) | 5392 | 4212 | 1100 | 80 | -49.8% | -72.4% | 22% | 20% |
| gescreend, houdercheck ok | 3893 | 3150 | 665 | 78 | -50.2% | -72.6% | 22% | 21% |
| gescreend, houdercheck gezakt | 1499 | 1062 | 435 | 2 | -49.3% | -72.1% | 21% | 17% |
| volledige screening gehaald | 568 | 508 | 51 | 9 | -49.1% | -72.0% | 4% | 10% |
| volledige screening gezakt | 4824 | 3704 | 1049 | 71 | -50.2% | -72.6% | 24% | 21% |
| volledige screening + X-link | 366 | 343 | 19 | 4 | -45.8% | -70.2% | 4% | 1% |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 316 bruikbaar, 316 opgehaald, 100 nog te gaan (400 deze run, 894 calls, 178 mislukte calls, 84 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

