# Wat is er van de tokens geworden? — 2026-09-13 15:28 UTC

41658 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 41658 | 3.8% (1593) | 17.7% (7375) | 78.5% (32690) | 4.4% (1845) |
| gescreend (ongeacht uitkomst) | 5747 | 20.6% (1182) | 8.7% (500) | 70.7% (4065) | 32.1% (1845) |
| gescreend, houdercheck ok | 4215 | 17.4% (733) | 11.3% (476) | 71.3% (3006) | 34.1% (1437) |
| gescreend, houdercheck gezakt | 1532 | 29.3% (449) | 1.6% (24) | 69.1% (1059) | 26.6% (408) |
| volledige screening gehaald | 634 | 8.8% (56) | 18.1% (115) | 73.0% (463) | 30.6% (194) |
| volledige screening gezakt | 5113 | 22.0% (1126) | 7.5% (385) | 70.5% (3602) | 32.3% (1651) |
| volledige screening + X-link | 407 | 4.9% (20) | 17.7% (72) | 77.4% (315) | 23.1% (94) |

## Controle op de koers uit de keten

**IJking geslaagd.** Bij 185 dode curve-tokens is gemeten hoeveel virtuele SOL de curve bij de start meetelt: **30.00 SOL**, met een spreiding van 0.2% tussen tokens. Die waarde is dus niet aangenomen maar gemeten, en omdat hij bij alle tokens hetzelfde uitkomt klopt het model.

Bij 185 dode curve-tokens — waar de koers sinds onze laatste waarneming niet meer bewogen kán zijn — wijkt de uit de keten afgeleide koers mediaan **16.3%** af. Binnen de marge van 25%, dus de koers wordt gebruikt.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

**Gemigreerde tokens zitten er niet in.** Hun curve is leeg en hun koers staat in een AMM-pool die we nog niet betrouwbaar uitlezen. Dat is juist de groep die het goed deed, dus deze cijfers zijn een ondergrens en geen schatting van wat vasthouden opbrengt.

| niveau | tokens met top | koers bekend | gemigreerd (geen koers) | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|
| alle tokens | 5656 | 4485 | 1161 | 10 | -51.1% | -73.1% | 20% | 19% |
| gescreend (ongeacht uitkomst) | 5656 | 4485 | 1161 | 10 | -51.1% | -73.1% | 20% | 19% |
| gescreend, houdercheck ok | 4131 | 3406 | 715 | 10 | -51.5% | -73.3% | 20% | 20% |
| gescreend, houdercheck gezakt | 1525 | 1079 | 446 | 0 | -49.5% | -72.2% | 20% | 16% |
| volledige screening gehaald | 620 | 564 | 56 | 0 | -50.2% | -72.6% | 4% | 9% |
| volledige screening gezakt | 5036 | 3921 | 1105 | 10 | -51.2% | -73.2% | 23% | 20% |
| volledige screening + X-link | 400 | 380 | 20 | 0 | -46.9% | -70.8% | 3% | 2% |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 605 bruikbaar, 605 opgehaald, 10 nog te gaan (52 deze run, 114 calls, 20 mislukte calls, 10 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

