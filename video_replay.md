# Videostrategie op alle trades — 2026-09-15 22:11 UTC

Tokens sinds 2026-09-13 10:11 UTC: 72419 geschikt (≥ 2 uur oud, geen herstart), 55545 met trades, 9902 haalden 2x de startkoers, 7649 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2275 tokens. Houdercheck echt uitgevoerd bij 95% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 363, winkans 13%, EV per trade -8.0% (95%-marge -10.1% tot -5.9%), mediaan -10.0%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 6203, winkans 21%, EV -7.3% (95%-marge -8.7% tot -6.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 185, winkans 18%, EV -9.9% (95%-marge -13.1% tot -6.6%).
- **H4** (2026-09-14 22:00 UTC): instap na een dip van 65% vanaf de top; stop op 75% onder de top zolang de winst onder +15% blijft; vanaf +15% een meelopende stop op 10% onder de hoogste koers; schone grafiek en houdercheck in orde. Aanleiding: voorstel van Gerben, 14 sept. Combineert de twee hefbomen die los gemeten het minst slecht waren: dieper instappen (d65-d70 gaf -3,8% tot -4,7% tegen -6,9% bij d45) en eerder winst vastleggen (+10% gaf -5,4% tegen -6,9% bij +45%), maar dan met een meelopende stop zodat een uitschieter niet wordt afgekapt. Filter is 'schoon+houders_ok' en niet de volledige screening, omdat die screening in drie onafhankelijke metingen averechts werkt. Verwachting vooraf, zodat die toetsbaar is: rond -3%, dus nog steeds negatief.. Resultaat: n = 3, winkans 33%, EV -4.2% (95%-marge -9.9% tot +1.6%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 7649 | 38% | 79% | 33% |
| schoon | 6203 | 39% | 79% | 35% |
| bundelgrafiek | 1446 | 33% | 78% | 24% |
| schoon+houders_ok | 363 | 26% | 82% | 7% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -5.7% (8145, 25% win) | -6.4% (7965, 24% win) | -6.7% (7803, 23% win) | -6.3% (7649, 22% win) | -6.4% (7499, 21% win) | -6.5% (7180, 21% win) | -6.4% (6578, 21% win) | -5.4% (5837, 22% win) | -5.8% (5102, 23% win) | -6.0% (4470, 24% win) | -6.1% (3860, 27% win) | -6.1% (6096, 26% win) |
| schoon | -6.4% (6577, 25% win) | -6.9% (6441, 23% win) | -7.0% (6323, 23% win) | -6.4% (6203, 23% win) | -6.3% (6071, 22% win) | -6.4% (5795, 22% win) | -6.3% (5276, 22% win) | -5.8% (4671, 23% win) | -5.8% (4091, 24% win) | -5.8% (3586, 26% win) | -6.2% (3145, 29% win) | -6.3% (5078, 26% win) |
| bundelgrafiek | -2.7% (1568, 27% win) | -4.0% (1524, 25% win) | -5.3% (1480, 22% win) | -6.0% (1446, 20% win) | -6.9% (1428, 17% win) | -6.9% (1385, 16% win) | -6.9% (1302, 16% win) | -4.1% (1166, 17% win) | -5.6% (1011, 17% win) | -6.8% (884, 17% win) | -5.9% (715, 21% win) | -5.2% (1018, 25% win) |
| schoon+houders_ok | -8.2% (218, 16% win) | -9.4% (262, 13% win) | -8.8% (324, 13% win) | -8.0% (363, 13% win) | -8.4% (406, 11% win) | -8.4% (460, 11% win) | -6.9% (502, 10% win) | -7.3% (464, 10% win) | -6.4% (410, 11% win) | -5.6% (345, 12% win) | -6.2% (270, 12% win) | -4.0% (258, 19% win) |
| schoon+houders_ok+final_stretch | -6.3% (109, 16% win) | -9.4% (135, 12% win) | -8.1% (174, 13% win) | -6.4% (200, 14% win) | -8.5% (233, 9% win) | -8.0% (264, 10% win) | -7.9% (282, 7% win) | -8.7% (231, 6% win) | -6.0% (200, 10% win) | -6.2% (155, 8% win) | -5.9% (109, 8% win) | -4.2% (144, 17% win) |
| volledige_screening+schoon | -4.3% (91, 19% win) | -10.0% (110, 11% win) | -9.8% (133, 10% win) | -8.0% (151, 11% win) | -9.6% (173, 8% win) | -9.4% (185, 8% win) | -8.1% (188, 6% win) | -8.8% (145, 6% win) | -7.1% (116, 8% win) | -6.3% (100, 7% win) | -5.6% (68, 7% win) | -6.7% (106, 12% win) |
| volledige_screening+schoon+x_link | -3.9% (69, 20% win) | -10.1% (79, 13% win) | -9.7% (89, 10% win) | -8.1% (94, 12% win) | -9.5% (104, 11% win) | -9.5% (110, 10% win) | -8.5% (114, 8% win) | -9.2% (101, 7% win) | -7.2% (82, 8% win) | -6.6% (70, 7% win) | -6.8% (49, 4% win) | -7.2% (65, 11% win) |

## Regel van Gerben: dip 55%, stop op 65% vanaf de top, winst op +30%, breakeven bij +20%

De stop is een koersniveau t.o.v. de top, niet een percentage onder de instap: altijd 10%-punt dieper dan de instap. Bij de 55%-instap is dat de 65% die Gerben noemde, ruim 22% onder de instapprijs — waar de videoregel maar 3% ruimte geeft. Zodra +20% is aangetikt schuift de stop naar de instapprijs, winst op +30%.

| instapdip | stop vanaf top | stop onder instap |
|---|---|---|
| 30% | 40% | -14% |
| 35% | 45% | -15% |
| 40% | 50% | -17% |
| 45% | 55% | -18% |
| 50% | 60% | -20% |
| 55% | 65% | -22% |
| 60% | 70% | -25% |
| 65% | 75% | -29% |
| 70% | 80% | -33% |
| 75% | 85% | -40% |
| 80% | 90% | -50% |

Dieper instappen betekent dus ook meer risico per trade; de EV's hieronder zijn niet één op één vergelijkbaar. **Vooraf vastgelegd als H3 op de 55%-variant met volledige screening; de rest is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.5% (8145, 29% win) | -7.2% (7965, 28% win) | -7.2% (7803, 27% win) | -6.8% (7649, 26% win) | -6.9% (7499, 26% win) | -7.1% (7180, 26% win) | -7.2% (6578, 26% win) | -6.4% (5837, 27% win) | -6.3% (5102, 29% win) | -7.0% (4470, 31% win) | -7.5% (3860, 33% win) |
| schoon | -6.8% (6577, 29% win) | -7.5% (6441, 28% win) | -7.1% (6323, 28% win) | -6.7% (6203, 27% win) | -6.7% (6071, 27% win) | -6.9% (5795, 27% win) | -7.1% (5276, 27% win) | -6.3% (4671, 29% win) | -6.1% (4091, 31% win) | -6.6% (3586, 33% win) | -7.3% (3145, 35% win) |
| bundelgrafiek | -5.2% (1568, 30% win) | -6.3% (1524, 28% win) | -7.6% (1480, 24% win) | -7.2% (1446, 22% win) | -7.9% (1428, 21% win) | -8.1% (1385, 20% win) | -7.6% (1302, 20% win) | -6.4% (1166, 20% win) | -7.4% (1011, 21% win) | -8.4% (884, 22% win) | -8.4% (715, 25% win) |
| schoon+houders_ok | -8.0% (218, 23% win) | -9.0% (262, 22% win) | -8.8% (324, 21% win) | -8.9% (363, 22% win) | -9.6% (406, 19% win) | -8.5% (460, 19% win) | -8.5% (502, 17% win) | -8.6% (464, 20% win) | -8.3% (410, 21% win) | -7.5% (345, 24% win) | -6.8% (270, 26% win) |
| schoon+houders_ok+final_stretch | -7.1% (109, 26% win) | -10.6% (135, 20% win) | -9.5% (174, 21% win) | -10.3% (200, 20% win) | -10.9% (233, 18% win) | -8.9% (264, 19% win) | -10.2% (282, 15% win) | -11.3% (231, 15% win) | -7.7% (200, 22% win) | -7.5% (155, 23% win) | -7.3% (109, 23% win) |
| volledige_screening+schoon | -7.2% (91, 25% win) | -10.8% (110, 18% win) | -11.2% (133, 18% win) | -12.0% (151, 18% win) | -12.4% (173, 16% win) | -9.9% (185, 18% win) | -10.1% (188, 15% win) | -10.7% (145, 16% win) | -8.7% (116, 20% win) | -7.6% (100, 21% win) | -6.0% (68, 24% win) |
| volledige_screening+schoon+x_link | -7.4% (69, 25% win) | -9.9% (79, 19% win) | -11.8% (89, 18% win) | -12.4% (94, 17% win) | -11.1% (104, 18% win) | -8.0% (110, 23% win) | -8.4% (114, 19% win) | -9.8% (101, 18% win) | -8.5% (82, 20% win) | -6.0% (70, 23% win) | -5.7% (49, 24% win) |


## Regel H4: dip 65%, trailing stop vanaf +15% op 10% onder de piek

Tot +15% ligt de stop op hetzelfde niveau als bij de vorige regel — 10%-punt dieper dan de instap — zodat de positie eerst nog kan zakken. Vanaf +15% loopt de stop mee op 10% onder de hoogste koers, en ligt daarmee altijd boven de instapprijs. Geen vaste winstgrens: een uitschieter wordt niet afgekapt.

**Vooraf vastgelegd als H4 op d65 met filter schoon+houders_ok; de rest van deze regel is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.5% (8145, 28% win) | -7.2% (7965, 27% win) | -7.2% (7803, 26% win) | -7.2% (7649, 25% win) | -7.4% (7499, 24% win) | -7.1% (7180, 24% win) | -6.9% (6578, 24% win) | -5.9% (5837, 26% win) | -4.9% (5102, 27% win) | -6.6% (4470, 28% win) | -7.9% (3860, 29% win) |
| schoon | -7.1% (6577, 28% win) | -7.4% (6441, 27% win) | -7.1% (6323, 26% win) | -7.0% (6203, 26% win) | -7.1% (6071, 26% win) | -7.0% (5795, 25% win) | -6.5% (5276, 25% win) | -5.7% (4671, 27% win) | -4.3% (4091, 29% win) | -6.1% (3586, 30% win) | -7.8% (3145, 31% win) |
| bundelgrafiek | -4.0% (1568, 30% win) | -6.0% (1524, 27% win) | -7.5% (1480, 23% win) | -8.0% (1446, 21% win) | -8.6% (1428, 20% win) | -7.6% (1385, 19% win) | -8.4% (1302, 18% win) | -6.5% (1166, 19% win) | -7.3% (1011, 19% win) | -8.4% (884, 20% win) | -8.6% (715, 22% win) |
| schoon+houders_ok | -7.2% (218, 25% win) | -8.6% (262, 22% win) | -8.5% (324, 23% win) | -7.6% (363, 23% win) | -9.4% (406, 19% win) | -9.8% (460, 20% win) | -9.2% (502, 18% win) | -7.1% (464, 22% win) | -7.5% (410, 21% win) | -7.4% (345, 23% win) | -8.1% (270, 23% win) |
| schoon+houders_ok+final_stretch | -5.4% (109, 29% win) | -9.5% (135, 21% win) | -8.8% (174, 25% win) | -8.1% (200, 24% win) | -9.7% (233, 19% win) | -10.4% (264, 19% win) | -10.7% (282, 16% win) | -10.2% (231, 19% win) | -8.5% (200, 20% win) | -8.7% (155, 22% win) | -8.9% (109, 20% win) |
| volledige_screening+schoon | -4.9% (91, 29% win) | -9.3% (110, 17% win) | -10.2% (133, 23% win) | -11.2% (151, 21% win) | -12.5% (173, 16% win) | -11.5% (185, 18% win) | -10.3% (188, 16% win) | -10.8% (145, 19% win) | -9.6% (116, 19% win) | -10.4% (100, 19% win) | -8.1% (68, 19% win) |
| volledige_screening+schoon+x_link | -6.0% (69, 26% win) | -8.7% (79, 16% win) | -10.8% (89, 20% win) | -10.3% (94, 21% win) | -11.0% (104, 19% win) | -10.7% (110, 20% win) | -9.6% (114, 20% win) | -10.4% (101, 18% win) | -10.1% (82, 18% win) | -11.8% (70, 17% win) | -6.8% (49, 16% win) |


## Verkennend: winstgrens tegen dipdiepte

Elke winstgrens bij elke instapdiepte, filter `schoon+houders_ok`, stop als in de video. Dit is het raster waar 8 grenzen x 11 dieptes = 88 cellen uit komen. Bij zoveel cellen zit er door toeval altijd een goede tussen, dus **hier telt geen enkele cel als bewijs** — het is bedoeld om te zien of er ergens een gebied is dat consequent beter is, niet om de beste cel te kiezen.

| winstgrens | d30 | d35 | d40 | d45 | d50 | d55 | d60 | d65 | d70 | d75 | d80 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +10% | -8.0% (218) | -8.8% (262) | -9.2% (324) | -7.6% (363) | -7.6% (406) | -7.4% (460) | -6.0% (502) | -6.7% (464) | -7.0% (410) | -5.9% (345) | -6.3% (270) |
| +15% | -8.3% (218) | -9.2% (262) | -8.9% (324) | -7.4% (363) | -7.7% (406) | -7.4% (460) | -5.9% (502) | -7.1% (464) | -7.1% (410) | -5.8% (345) | -6.0% (270) |
| +20% | -8.2% (218) | -9.3% (262) | -9.0% (324) | -7.6% (363) | -7.9% (406) | -7.5% (460) | -6.4% (502) | -7.6% (464) | -7.2% (410) | -6.0% (345) | -6.1% (270) |
| +25% | -8.0% (218) | -8.7% (262) | -9.0% (324) | -7.4% (363) | -7.9% (406) | -7.4% (460) | -6.4% (502) | -7.6% (464) | -7.1% (410) | -6.0% (345) | -6.5% (270) |
| +30% | -7.3% (218) | -8.4% (262) | -8.6% (324) | -7.6% (363) | -8.3% (406) | -7.5% (460) | -6.5% (502) | -7.5% (464) | -7.4% (410) | -6.7% (345) | -6.5% (270) |
| +35% | -7.7% (218) | -9.3% (262) | -8.5% (324) | -7.3% (363) | -8.4% (406) | -7.6% (460) | -6.8% (502) | -7.1% (464) | -6.9% (410) | -6.2% (345) | -6.4% (270) |
| +45% | -8.2% (218) | -9.4% (262) | -8.8% (324) | -8.0% (363) | -8.4% (406) | -8.4% (460) | -6.9% (502) | -7.3% (464) | -6.4% (410) | -5.6% (345) | -6.2% (270) |
| +60% | -8.4% (218) | -9.3% (262) | -8.1% (324) | -7.5% (363) | -8.2% (406) | -9.0% (460) | -6.9% (502) | -6.4% (464) | -6.1% (410) | -5.9% (345) | -6.5% (270) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 151 instappen, mediane hoogste stijging +8.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 26% | -7.4% | 24% |
| +15% | 45% | 23% | -7.0% | 22% |
| +20% | 39% | 20% | -7.0% | 20% |
| +25% | 34% | 17% | -7.1% | 18% |
| +30% | 31% | 15% | -7.3% | 16% |
| +35% | 29% | 15% | -6.6% | 16% |
| +45% | 20% | 9% | -8.0% | 11% |
| +60% | 16% | 7% | -8.3% | 9% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 363 instappen, mediane hoogste stijging +9.0%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 49% | 25% | -7.6% | 25% |
| +15% | 46% | 20% | -7.4% | 22% |
| +20% | 42% | 17% | -7.6% | 20% |
| +25% | 39% | 16% | -7.4% | 19% |
| +30% | 36% | 14% | -7.6% | 17% |
| +35% | 33% | 13% | -7.3% | 16% |
| +45% | 28% | 9% | -8.0% | 13% |
| +60% | 24% | 8% | -7.5% | 12% |

**filter `alle`** — variant `d45_direct`, 7649 instappen, mediane hoogste stijging +19.3%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 31% | -5.9% | 29% |
| +15% | 53% | 28% | -5.8% | 28% |
| +20% | 50% | 24% | -5.8% | 27% |
| +25% | 46% | 22% | -6.0% | 26% |
| +30% | 44% | 20% | -6.1% | 24% |
| +35% | 42% | 18% | -6.2% | 24% |
| +45% | 37% | 15% | -6.3% | 22% |
| +60% | 32% | 12% | -6.4% | 21% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -7.4% (91, 19% win) | -6.7% (91, 19% win) | -5.0% (91, 19% win) | -4.3% (91, 19% win) | -7.3% (91, 19% win) | -6.6% (91, 19% win) |
| d35_direct | -13.1% (110, 11% win) | -12.4% (110, 11% win) | -10.7% (110, 11% win) | -10.0% (110, 11% win) | -12.8% (110, 11% win) | -12.2% (110, 11% win) |
| d40_direct | -12.8% (133, 8% win) | -12.1% (133, 9% win) | -10.4% (133, 10% win) | -9.8% (133, 10% win) | -12.7% (133, 8% win) | -12.1% (133, 9% win) |
| d45_direct | -11.0% (151, 10% win) | -10.4% (151, 11% win) | -8.7% (151, 11% win) | -8.0% (151, 11% win) | -11.2% (151, 10% win) | -10.6% (151, 11% win) |
| d50_direct | -12.5% (173, 7% win) | -11.9% (173, 7% win) | -10.2% (173, 8% win) | -9.6% (173, 8% win) | -12.9% (173, 7% win) | -12.3% (173, 7% win) |
| d55_direct | -12.3% (185, 7% win) | -11.7% (185, 7% win) | -10.0% (185, 8% win) | -9.4% (185, 8% win) | -12.9% (185, 7% win) | -12.3% (185, 7% win) |
| d60_direct | -11.1% (188, 6% win) | -10.4% (188, 6% win) | -8.8% (188, 6% win) | -8.1% (188, 6% win) | -11.8% (188, 6% win) | -11.2% (188, 6% win) |
| d65_direct | -11.8% (145, 6% win) | -11.1% (145, 6% win) | -9.5% (145, 6% win) | -8.8% (145, 6% win) | -12.5% (145, 5% win) | -11.8% (145, 6% win) |
| d70_direct | -10.0% (116, 7% win) | -9.3% (116, 7% win) | -7.8% (116, 8% win) | -7.1% (116, 8% win) | -10.8% (116, 7% win) | -10.2% (116, 7% win) |
| d75_direct | -9.2% (100, 7% win) | -8.5% (100, 7% win) | -6.9% (100, 7% win) | -6.3% (100, 7% win) | -10.1% (100, 7% win) | -9.4% (100, 7% win) |
| d80_direct | -8.4% (68, 6% win) | -7.7% (68, 6% win) | -6.2% (68, 6% win) | -5.6% (68, 7% win) | -9.5% (68, 6% win) | -8.9% (68, 6% win) |
| d45_herstel5 | -9.8% (106, 12% win) | -9.1% (106, 12% win) | -7.4% (106, 12% win) | -6.7% (106, 12% win) | -9.8% (106, 12% win) | -9.1% (106, 12% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -11.2% (218, 15% win) | -10.6% (218, 15% win) | -8.8% (218, 16% win) | -8.2% (218, 16% win) | -11.0% (218, 15% win) | -10.3% (218, 16% win) |
| d35_direct | -12.5% (262, 13% win) | -11.8% (262, 13% win) | -10.1% (262, 13% win) | -9.4% (262, 13% win) | -12.3% (262, 13% win) | -11.7% (262, 13% win) |
| d40_direct | -11.8% (324, 12% win) | -11.2% (324, 13% win) | -9.4% (324, 13% win) | -8.8% (324, 13% win) | -11.7% (324, 12% win) | -11.1% (324, 13% win) |
| d45_direct | -11.0% (363, 11% win) | -10.4% (363, 12% win) | -8.7% (363, 12% win) | -8.0% (363, 13% win) | -11.2% (363, 11% win) | -10.5% (363, 12% win) |
| d50_direct | -11.4% (406, 10% win) | -10.7% (406, 10% win) | -9.1% (406, 11% win) | -8.4% (406, 11% win) | -11.7% (406, 10% win) | -11.1% (406, 10% win) |
| d55_direct | -11.4% (460, 10% win) | -10.7% (460, 10% win) | -9.1% (460, 11% win) | -8.4% (460, 11% win) | -11.8% (460, 10% win) | -11.2% (460, 10% win) |
| d60_direct | -9.8% (502, 10% win) | -9.1% (502, 10% win) | -7.6% (502, 10% win) | -6.9% (502, 10% win) | -10.5% (502, 9% win) | -9.9% (502, 10% win) |
| d65_direct | -10.3% (464, 10% win) | -9.6% (464, 10% win) | -8.0% (464, 10% win) | -7.3% (464, 10% win) | -10.9% (464, 9% win) | -10.3% (464, 10% win) |
| d70_direct | -9.3% (410, 11% win) | -8.6% (410, 11% win) | -7.1% (410, 11% win) | -6.4% (410, 11% win) | -10.2% (410, 10% win) | -9.6% (410, 11% win) |
| d75_direct | -8.5% (345, 11% win) | -7.8% (345, 11% win) | -6.3% (345, 12% win) | -5.6% (345, 12% win) | -9.5% (345, 11% win) | -8.9% (345, 11% win) |
| d80_direct | -9.0% (270, 11% win) | -8.3% (270, 12% win) | -6.8% (270, 12% win) | -6.2% (270, 12% win) | -10.4% (270, 12% win) | -9.8% (270, 12% win) |
| d45_herstel5 | -7.1% (258, 18% win) | -6.4% (258, 19% win) | -4.7% (258, 19% win) | -4.0% (258, 19% win) | -7.1% (258, 18% win) | -6.4% (258, 19% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -8.7% (8145, 24% win) | -8.0% (8145, 24% win) | -6.4% (8145, 25% win) | -5.7% (8145, 25% win) | -9.0% (8145, 23% win) | -8.4% (8145, 24% win) |
| d35_direct | -9.3% (7965, 22% win) | -8.7% (7965, 23% win) | -7.1% (7965, 23% win) | -6.4% (7965, 24% win) | -9.8% (7965, 22% win) | -9.2% (7965, 22% win) |
| d40_direct | -9.6% (7803, 21% win) | -8.9% (7803, 22% win) | -7.4% (7803, 22% win) | -6.7% (7803, 23% win) | -10.3% (7803, 21% win) | -9.6% (7803, 21% win) |
| d45_direct | -9.2% (7649, 21% win) | -8.5% (7649, 21% win) | -7.0% (7649, 22% win) | -6.3% (7649, 22% win) | -10.1% (7649, 20% win) | -9.5% (7649, 21% win) |
| d50_direct | -9.2% (7499, 20% win) | -8.6% (7499, 20% win) | -7.1% (7499, 21% win) | -6.4% (7499, 21% win) | -10.4% (7499, 19% win) | -9.8% (7499, 20% win) |
| d55_direct | -9.3% (7180, 19% win) | -8.6% (7180, 20% win) | -7.2% (7180, 20% win) | -6.5% (7180, 21% win) | -10.7% (7180, 19% win) | -10.1% (7180, 19% win) |
| d60_direct | -9.1% (6578, 19% win) | -8.4% (6578, 20% win) | -7.1% (6578, 20% win) | -6.4% (6578, 21% win) | -10.9% (6578, 18% win) | -10.3% (6578, 19% win) |
| d65_direct | -8.1% (5837, 21% win) | -7.4% (5837, 21% win) | -6.1% (5837, 22% win) | -5.4% (5837, 22% win) | -10.4% (5837, 20% win) | -9.8% (5837, 20% win) |
| d70_direct | -8.3% (5102, 22% win) | -7.6% (5102, 22% win) | -6.5% (5102, 22% win) | -5.8% (5102, 23% win) | -11.3% (5102, 20% win) | -10.7% (5102, 20% win) |
| d75_direct | -8.3% (4470, 24% win) | -7.6% (4470, 24% win) | -6.7% (4470, 24% win) | -6.0% (4470, 24% win) | -12.3% (4470, 21% win) | -11.7% (4470, 21% win) |
| d80_direct | -8.1% (3860, 26% win) | -7.4% (3860, 26% win) | -6.8% (3860, 27% win) | -6.1% (3860, 27% win) | -13.7% (3860, 23% win) | -13.1% (3860, 23% win) |
| d45_herstel5 | -9.0% (6096, 24% win) | -8.3% (6096, 25% win) | -6.8% (6096, 26% win) | -6.1% (6096, 26% win) | -10.0% (6096, 24% win) | -9.4% (6096, 24% win) |


## Wat kost de uitvoering echt?

Wij rekenen met 0.001 SOL vaste kosten per transactie. De video van 14 sept gebruikt een tip van 0,02 SOL plus 0,001 prioriteitsfee — twintig keer zoveel. Een vaste fee werkt lineair door: elke extra T SOL per kant verlaagt het rendement met 2T gedeeld door de inzet. Onderstaande EV's zijn daarmee exact doorgerekend, niet opnieuw gesimuleerd. Filter `schoon+houders_ok`, videoregel, PumpPortal.

| extra vaste fee per transactie | inzet 0.05 SOL | inzet 0.2 SOL | inzet 1.0 SOL |
|---|---|---|---|
| +0.0 SOL | -10.4% | -8.0% | -10.5% |
| +0.005 SOL | -30.4% | -13.0% | -11.5% |
| +0.01 SOL | -50.4% | -18.0% | -12.5% |
| +0.02 SOL | -90.4% | -28.0% | -14.5% |

Bij 0,05 SOL inzet eet een tip van 0,02 SOL per kant 84% van de positie op. Een strategie met een randje van een paar procent bestaat bij die instellingen simpelweg niet; bij 1 SOL kost hij 4,2%. Dit verandert onze conclusie niet — de EV was al negatief — maar het laat zien dat kleine inzetten bij deze uitvoering sowieso kansloos zijn, en dat onze eigen cijfers aan de gunstige kant staan.



## Uitstapregels vergeleken (dip 45%, direct)

'Gespreid' is vier gelijke plakjes op +10%, +20%, +30% en +45%, allemaal met dezelfde stop — het advies uit de KOL-video om niet in één keer te verkopen. Dat is rekenkundig het gewogen gemiddelde van de vier losse grenzen, dus het kan de verwachting niet redden; het verandert alleen de spreiding.

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) | gespreid |
|---|---|---|---|---|
| alle | -6.3% (7649, 22% win) | -6.1% (7649, 22% win) | -7.7% (7649, 21% win) | -6.0% (7649, 25% win) |
| schoon | -6.4% (6203, 23% win) | -6.1% (6203, 22% win) | -7.3% (6203, 21% win) | -6.1% (6203, 26% win) |
| bundelgrafiek | -6.0% (1446, 20% win) | -5.9% (1446, 19% win) | -9.0% (1446, 18% win) | -5.9% (1446, 22% win) |
| schoon+houders_ok | -8.0% (363, 13% win) | -7.6% (363, 10% win) | -10.5% (363, 14% win) | -7.7% (363, 19% win) |
| schoon+houders_ok+final_stretch | -6.4% (200, 14% win) | -6.7% (200, 10% win) | -11.7% (200, 14% win) | -6.5% (200, 20% win) |
| volledige_screening+schoon | -8.0% (151, 11% win) | -8.6% (151, 6% win) | -15.2% (151, 11% win) | -7.4% (151, 19% win) |
| volledige_screening+schoon+x_link | -8.1% (94, 12% win) | -8.8% (94, 7% win) | -14.9% (94, 10% win) | -8.1% (94, 18% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (3032, 27% win); 1,3–2x: -7.0% (3170, 18% win); ≥ 2x (bundelgrafiek): -6.0% (1447, 20% win)

**aandeel supply gekocht in creatieblok:** < 5%: -4.9% (4338, 29% win); 5–20%: -8.3% (1288, 13% win); ≥ 20%: -8.1% (2023, 12% win)

**top t.o.v. start:** 2–3x: -5.9% (4381, 21% win); 3–6x: -7.1% (2519, 24% win); ≥ 6x: -5.9% (749, 24% win)

**unieke kopers tot de top:** < 30: -5.3% (4471, 28% win); 30–100: -6.9% (1762, 13% win); ≥ 100: -8.8% (1416, 13% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.4% (1994, 16% win); 1–2: -6.6% (3663, 24% win); ≥ 3 (trap): -5.7% (1992, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -7.9% (2091, 14% win); 10–25%: -8.7% (1477, 11% win); ≥ 25%: -4.7% (4081, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (5899, 25% win); 30 s–3 min: -7.0% (1390, 13% win); ≥ 3 min (langzaam): -8.9% (360, 10% win)

**tijd van start tot top:** < 2 min: -5.9% (6175, 24% win); 2–10 min: -8.6% (1191, 13% win); ≥ 10 min: -6.2% (283, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
