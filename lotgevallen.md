# Wat is er van de tokens geworden? — 2026-09-13 13:32 UTC

39454 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.

| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |
|---|---|---|---|---|---|
| alle tokens | 39454 | 3.9% (1529) | 15.4% (6090) | 80.7% (31835) | 4.5% (1760) |
| gescreend (ongeacht uitkomst) | 5543 | 20.5% (1137) | 7.2% (401) | 72.2% (4005) | 31.8% (1760) |
| gescreend, houdercheck ok | 4028 | 17.2% (694) | 9.5% (384) | 73.2% (2950) | 33.6% (1355) |
| gescreend, houdercheck gezakt | 1515 | 29.2% (443) | 1.1% (17) | 69.6% (1055) | 26.7% (405) |
| volledige screening gehaald | 600 | 8.8% (53) | 15.0% (90) | 76.2% (457) | 29.0% (174) |
| volledige screening gezakt | 4943 | 21.9% (1084) | 6.3% (311) | 71.8% (3548) | 32.1% (1586) |
| volledige screening + X-link | 392 | 5.1% (20) | 15.0% (59) | 79.8% (313) | 22.2% (87) |

## Controle op de koers uit de keten

**IJking geslaagd.** Bij 125 dode curve-tokens is gemeten hoeveel virtuele SOL de curve bij de start meetelt: **30.00 SOL**, met een spreiding van 0.0% tussen tokens. Die waarde is dus niet aangenomen maar gemeten, en omdat hij bij alle tokens hetzelfde uitkomt klopt het model.

Bij 125 dode curve-tokens — waar de koers sinds onze laatste waarneming niet meer bewogen kán zijn — wijkt de uit de keten afgeleide koers mediaan **16.2%** af. Binnen de marge van 25%, dus de koers wordt gebruikt.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

**Gemigreerde tokens zitten er niet in.** Hun curve is leeg en hun koers staat in een AMM-pool die we nog niet betrouwbaar uitlezen. Dat is juist de groep die het goed deed, dus deze cijfers zijn een ondergrens en geen schatting van wat vasthouden opbrengt.

| niveau | tokens met top | koers bekend | gemigreerd (geen koers) | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|
| alle tokens | 5438 | 4322 | 1114 | 2 | -50.4% | -72.8% | 21% | 20% |
| gescreend (ongeacht uitkomst) | 5438 | 4322 | 1114 | 2 | -50.4% | -72.8% | 21% | 20% |
| gescreend, houdercheck ok | 3933 | 3256 | 675 | 2 | -50.7% | -72.9% | 21% | 20% |
| gescreend, houdercheck gezakt | 1505 | 1066 | 439 | 0 | -49.3% | -72.1% | 20% | 17% |
| volledige screening gehaald | 582 | 530 | 52 | 0 | -49.3% | -72.1% | 4% | 9% |
| volledige screening gezakt | 4856 | 3792 | 1062 | 2 | -50.6% | -72.9% | 24% | 21% |
| volledige screening + X-link | 380 | 360 | 20 | 0 | -46.0% | -70.3% | 3% | 1% |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 442 bruikbaar, 442 opgehaald, 2 nog te gaan (128 deze run, 260 calls, 6 mislukte calls, 2 tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.

