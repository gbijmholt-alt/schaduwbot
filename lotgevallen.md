# Wat is er van de tokens geworden? — 2026-09-13 14:57 UTC

41138 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 41138 | 3.8% (1569) | 17.2% (7098) | 78.9% (32471) | 4.4% (1824) |
| gescreend (ongeacht uitkomst) | 5685 | 20.5% (1166) | 8.3% (474) | 71.2% (4045) | 32.1% (1824) |
| gescreend, houdercheck ok | 4158 | 17.3% (720) | 10.8% (450) | 71.9% (2988) | 34.1% (1417) |
| gescreend, houdercheck gezakt | 1527 | 29.2% (446) | 1.6% (24) | 69.2% (1057) | 26.7% (407) |
| volledige screening gehaald | 624 | 9.0% (56) | 17.5% (109) | 73.6% (459) | 30.6% (191) |
| volledige screening gezakt | 5061 | 21.9% (1110) | 7.2% (365) | 70.9% (3586) | 32.3% (1633) |
| volledige screening + X-link | 402 | 5.0% (20) | 16.7% (67) | 78.4% (315) | 22.9% (92) |

## Controle op de koers uit de keten

**IJking geslaagd.** Bij 165 dode curve-tokens is gemeten hoeveel virtuele SOL de curve bij de start meetelt: **30.00 SOL**, met een spreiding van 0.3% tussen tokens. Die waarde is dus niet aangenomen maar gemeten, en omdat hij bij alle tokens hetzelfde uitkomt klopt het model.

Bij 165 dode curve-tokens — waar de koers sinds onze laatste waarneming niet meer bewogen kán zijn — wijkt de uit de keten afgeleide koers mediaan **16.3%** af. Binnen de marge van 25%, dus de koers wordt gebruikt.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

**Gemigreerde tokens zitten er niet in.** Hun curve is leeg en hun koers staat in een AMM-pool die we nog niet betrouwbaar uitlezen. Dat is juist de groep die het goed deed, dus deze cijfers zijn een ondergrens en geen schatting van wat vasthouden opbrengt.

| niveau | tokens met top | koers bekend | gemigreerd (geen koers) | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|
| alle tokens | 5607 | 4443 | 1153 | 11 | -50.9% | -73.0% | 21% | 19% |
| gescreend (ongeacht uitkomst) | 5607 | 4443 | 1153 | 11 | -50.9% | -73.0% | 21% | 19% |
| gescreend, houdercheck ok | 4086 | 3366 | 709 | 11 | -51.2% | -73.2% | 21% | 20% |
| gescreend, houdercheck gezakt | 1521 | 1077 | 444 | 0 | -49.5% | -72.2% | 20% | 16% |
| volledige screening gehaald | 612 | 556 | 56 | 0 | -49.9% | -72.5% | 4% | 9% |
| volledige screening gezakt | 4995 | 3887 | 1097 | 11 | -51.1% | -73.1% | 23% | 21% |
| volledige screening + X-link | 396 | 376 | 20 | 0 | -46.7% | -70.7% | 3% | 1% |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 563 bruikbaar, 563 opgehaald, 11 nog te gaan (132 deze run, 277 calls, 24 mislukte calls, 11 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

