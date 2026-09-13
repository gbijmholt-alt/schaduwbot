# Wat is er van de tokens geworden? — 2026-09-13 12:23 UTC

38436 tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades meer sinds ≥ 6 uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het token handelt verder op een AMM — dat is wat de video als doel beschrijft.

## Afloop per screeningniveau

| niveau | tokens | gemigreerd | nog actief | dood op curve | gerugd |
|---|---|---|---|---|---|
| alle tokens | 38436 | 3.9% (1482) | 14.3% (5502) | 77.6% (29847) | 4.2% (1605) |
| gescreend (ongeacht uitkomst) | 5414 | 20.4% (1105) | 4.3% (233) | 45.6% (2471) | 29.6% (1605) |
| gescreend, houdercheck ok | 3912 | 17.1% (668) | 5.7% (223) | 46.1% (1802) | 31.2% (1219) |
| gescreend, houdercheck gezakt | 1502 | 29.1% (437) | 0.7% (10) | 44.5% (669) | 25.7% (386) |
| volledige screening gehaald | 577 | 8.7% (50) | 9.7% (56) | 55.8% (322) | 25.8% (149) |
| volledige screening gezakt | 4837 | 21.8% (1055) | 3.7% (177) | 44.4% (2149) | 30.1% (1456) |
| volledige screening + X-link | 375 | 5.1% (19) | 10.4% (39) | 64.0% (240) | 20.5% (77) |

## Controle op de koers uit de keten

**IJking geslaagd.** Bij 127 dode curve-tokens is gemeten hoeveel virtuele SOL de curve bij de start meetelt: **30.00 SOL**, met een spreiding van 0.0% tussen tokens. Die waarde is dus niet aangenomen maar gemeten, en omdat hij bij alle tokens hetzelfde uitkomt klopt het model.

Bij 127 dode curve-tokens — waar de koers sinds onze laatste waarneming niet meer bewogen kán zijn — wijkt de uit de keten afgeleide koers mediaan **16.2%** af. Binnen de marge van 25%, dus de koers wordt gebruikt.

## Wat had kopen-en-vasthouden opgeleverd?

Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.

**Gemigreerde tokens zitten er niet in.** Hun curve is leeg en hun koers staat in een AMM-pool die we nog niet betrouwbaar uitlezen. Dat is juist de groep die het goed deed, dus deze cijfers zijn een ondergrens en geen schatting van wat vasthouden opbrengt.

| niveau | tokens met top | koers bekend | gemigreerd (geen koers) | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |
|---|---|---|---|---|---|---|---|---|
| alle tokens | 5323 | 2625 | 1081 | 1617 | -31.5% | -62.3% | 35% | 0% |
| gescreend (ongeacht uitkomst) | 5323 | 2625 | 1081 | 1617 | -31.5% | -62.3% | 35% | 0% |
| gescreend, houdercheck ok | 3830 | 1941 | 651 | 1238 | -30.1% | -61.5% | 36% | 0% |
| gescreend, houdercheck gezakt | 1493 | 684 | 430 | 379 | -33.8% | -63.6% | 32% | 0% |
| volledige screening gehaald | 548 | 363 | 50 | 135 | -40.7% | -67.4% | 5% | 0% |
| volledige screening gezakt | 4775 | 2262 | 1031 | 1482 | -28.8% | -60.9% | 39% | 0% |
| volledige screening + X-link | 352 | 262 | 19 | 71 | -39.8% | -66.9% | 4% | 0% |

'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een hoogste koers alleen vast voor tokens die hij actief volgde.

Koersen uit de keten: 350 bruikbaar, 350 opgehaald, 0 nog te gaan (148 deze run, 296 calls, 35 fouten). De analyse draait elke 2 uur.

