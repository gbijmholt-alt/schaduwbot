# Videostrategie op alle trades — 2026-09-15 19:05 UTC

Tokens sinds 2026-09-13 07:05 UTC: 68842 geschikt (≥ 2 uur oud, geen herstart), 52628 met trades, 9302 haalden 2x de startkoers, 7138 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2165 tokens. Houdercheck echt uitgevoerd bij 95% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 387, winkans 12%, EV per trade -8.2% (95%-marge -10.2% tot -6.2%), mediaan -10.4%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 5793, winkans 22%, EV -7.3% (95%-marge -8.7% tot -5.9%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 195, winkans 18%, EV -9.8% (95%-marge -13.0% tot -6.7%).
- **H4** (2026-09-14 22:00 UTC): instap na een dip van 65% vanaf de top; stop op 75% onder de top zolang de winst onder +15% blijft; vanaf +15% een meelopende stop op 10% onder de hoogste koers; schone grafiek en houdercheck in orde. Aanleiding: voorstel van Gerben, 14 sept. Combineert de twee hefbomen die los gemeten het minst slecht waren: dieper instappen (d65-d70 gaf -3,8% tot -4,7% tegen -6,9% bij d45) en eerder winst vastleggen (+10% gaf -5,4% tegen -6,9% bij +45%), maar dan met een meelopende stop zodat een uitschieter niet wordt afgekapt. Filter is 'schoon+houders_ok' en niet de volledige screening, omdat die screening in drie onafhankelijke metingen averechts werkt. Verwachting vooraf, zodat die toetsbaar is: rond -3%, dus nog steeds negatief.. Resultaat: n = 3, winkans 33%, EV -4.2% (95%-marge -9.9% tot +1.6%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 7138 | 38% | 78% | 34% |
| schoon | 5793 | 39% | 79% | 36% |
| bundelgrafiek | 1345 | 34% | 78% | 25% |
| schoon+houders_ok | 387 | 27% | 82% | 6% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -5.7% (7611, 25% win) | -6.4% (7436, 24% win) | -6.6% (7283, 23% win) | -6.1% (7138, 22% win) | -6.1% (6995, 22% win) | -6.3% (6695, 21% win) | -6.2% (6137, 21% win) | -5.5% (5469, 23% win) | -5.7% (4783, 24% win) | -6.0% (4203, 24% win) | -6.1% (3638, 27% win) | -5.9% (5714, 26% win) |
| schoon | -6.4% (6149, 25% win) | -7.0% (6016, 24% win) | -7.0% (5905, 23% win) | -6.2% (5793, 23% win) | -6.1% (5666, 23% win) | -6.3% (5406, 22% win) | -6.2% (4920, 22% win) | -5.9% (4378, 24% win) | -5.7% (3838, 25% win) | -5.9% (3371, 26% win) | -6.3% (2964, 29% win) | -6.2% (4770, 26% win) |
| bundelgrafiek | -2.4% (1462, 27% win) | -3.8% (1420, 26% win) | -5.1% (1378, 22% win) | -5.3% (1345, 20% win) | -6.3% (1329, 18% win) | -6.6% (1289, 17% win) | -6.1% (1217, 16% win) | -3.6% (1091, 18% win) | -5.6% (945, 17% win) | -6.5% (832, 17% win) | -5.5% (674, 21% win) | -4.5% (944, 25% win) |
| schoon+houders_ok | -7.2% (242, 16% win) | -8.8% (285, 14% win) | -8.6% (349, 14% win) | -8.2% (387, 12% win) | -8.8% (430, 11% win) | -8.2% (486, 11% win) | -6.9% (529, 10% win) | -7.3% (488, 10% win) | -6.2% (432, 12% win) | -5.9% (358, 12% win) | -6.3% (280, 12% win) | -4.8% (278, 18% win) |
| schoon+houders_ok+final_stretch | -5.8% (122, 16% win) | -9.6% (148, 11% win) | -8.0% (189, 13% win) | -6.9% (213, 13% win) | -8.8% (246, 9% win) | -8.1% (278, 9% win) | -8.0% (295, 8% win) | -8.3% (241, 6% win) | -5.7% (209, 10% win) | -6.3% (159, 8% win) | -6.0% (111, 8% win) | -4.7% (154, 16% win) |
| volledige_screening+schoon | -4.6% (101, 18% win) | -10.2% (120, 10% win) | -9.4% (145, 10% win) | -8.5% (161, 11% win) | -9.9% (183, 7% win) | -9.6% (195, 7% win) | -8.2% (196, 6% win) | -8.2% (151, 7% win) | -6.4% (121, 8% win) | -6.3% (103, 7% win) | -5.6% (69, 7% win) | -7.2% (114, 11% win) |
| volledige_screening+schoon+x_link | -4.1% (74, 20% win) | -10.5% (84, 12% win) | -9.5% (94, 11% win) | -8.6% (99, 11% win) | -9.8% (109, 10% win) | -9.7% (115, 10% win) | -8.5% (119, 8% win) | -8.8% (105, 8% win) | -7.4% (85, 8% win) | -6.7% (73, 7% win) | -6.9% (50, 4% win) | -7.9% (70, 10% win) |

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
| alle | -6.4% (7611, 30% win) | -7.2% (7436, 28% win) | -7.1% (7283, 27% win) | -6.6% (7138, 27% win) | -6.8% (6995, 26% win) | -7.0% (6695, 26% win) | -7.0% (6137, 26% win) | -6.4% (5469, 27% win) | -6.4% (4783, 29% win) | -7.0% (4203, 31% win) | -7.5% (3638, 33% win) |
| schoon | -6.7% (6149, 29% win) | -7.5% (6016, 28% win) | -7.0% (5905, 28% win) | -6.5% (5793, 28% win) | -6.7% (5666, 28% win) | -6.8% (5406, 28% win) | -7.0% (4920, 28% win) | -6.5% (4378, 29% win) | -6.1% (3838, 31% win) | -6.7% (3371, 33% win) | -7.4% (2964, 35% win) |
| bundelgrafiek | -5.1% (1462, 31% win) | -6.2% (1420, 28% win) | -7.4% (1378, 24% win) | -6.8% (1345, 23% win) | -7.5% (1329, 21% win) | -7.8% (1289, 20% win) | -6.7% (1217, 20% win) | -5.9% (1091, 21% win) | -7.5% (945, 21% win) | -8.4% (832, 22% win) | -8.3% (674, 25% win) |
| schoon+houders_ok | -7.0% (242, 24% win) | -8.4% (285, 23% win) | -8.0% (349, 22% win) | -8.7% (387, 22% win) | -9.9% (430, 19% win) | -8.2% (486, 20% win) | -8.2% (529, 18% win) | -8.6% (488, 20% win) | -7.9% (432, 22% win) | -7.6% (358, 25% win) | -7.1% (280, 26% win) |
| schoon+houders_ok+final_stretch | -6.4% (122, 25% win) | -9.8% (148, 22% win) | -8.7% (189, 22% win) | -10.6% (213, 20% win) | -11.0% (246, 18% win) | -8.6% (278, 20% win) | -10.0% (295, 15% win) | -11.1% (241, 16% win) | -7.6% (209, 22% win) | -7.8% (159, 23% win) | -7.2% (111, 23% win) |
| volledige_screening+schoon | -7.1% (101, 25% win) | -9.8% (120, 20% win) | -10.1% (145, 20% win) | -12.2% (161, 17% win) | -12.4% (183, 15% win) | -9.8% (195, 18% win) | -9.9% (196, 15% win) | -10.1% (151, 17% win) | -8.4% (121, 21% win) | -7.7% (103, 20% win) | -5.5% (69, 25% win) |
| volledige_screening+schoon+x_link | -7.5% (74, 24% win) | -9.6% (84, 19% win) | -11.6% (94, 18% win) | -12.4% (99, 17% win) | -11.3% (109, 17% win) | -8.2% (115, 23% win) | -8.3% (119, 19% win) | -9.4% (105, 19% win) | -9.0% (85, 19% win) | -6.2% (73, 22% win) | -5.1% (50, 26% win) |


## Regel H4: dip 65%, trailing stop vanaf +15% op 10% onder de piek

Tot +15% ligt de stop op hetzelfde niveau als bij de vorige regel — 10%-punt dieper dan de instap — zodat de positie eerst nog kan zakken. Vanaf +15% loopt de stop mee op 10% onder de hoogste koers, en ligt daarmee altijd boven de instapprijs. Geen vaste winstgrens: een uitschieter wordt niet afgekapt.

**Vooraf vastgelegd als H4 op d65 met filter schoon+houders_ok; de rest van deze regel is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.5% (7611, 28% win) | -7.3% (7436, 27% win) | -7.1% (7283, 26% win) | -7.1% (7138, 25% win) | -7.4% (6995, 25% win) | -7.0% (6695, 24% win) | -6.7% (6137, 24% win) | -6.1% (5469, 26% win) | -5.1% (4783, 27% win) | -6.6% (4203, 28% win) | -8.0% (3638, 29% win) |
| schoon | -7.0% (6149, 28% win) | -7.6% (6016, 27% win) | -7.1% (5905, 26% win) | -7.0% (5793, 26% win) | -7.2% (5666, 26% win) | -6.9% (5406, 26% win) | -6.5% (4920, 25% win) | -6.1% (4378, 27% win) | -4.5% (3838, 29% win) | -6.1% (3371, 30% win) | -7.8% (2964, 31% win) |
| bundelgrafiek | -3.9% (1462, 30% win) | -6.0% (1420, 28% win) | -7.4% (1378, 24% win) | -7.7% (1345, 22% win) | -8.2% (1329, 20% win) | -7.5% (1289, 19% win) | -7.7% (1217, 18% win) | -6.2% (1091, 19% win) | -7.6% (945, 19% win) | -8.5% (832, 20% win) | -8.6% (674, 22% win) |
| schoon+houders_ok | -6.4% (242, 26% win) | -8.2% (285, 23% win) | -8.3% (349, 24% win) | -7.9% (387, 23% win) | -9.8% (430, 19% win) | -9.6% (486, 20% win) | -9.1% (529, 18% win) | -7.3% (488, 22% win) | -6.7% (432, 22% win) | -7.5% (358, 23% win) | -8.6% (280, 22% win) |
| schoon+houders_ok+final_stretch | -4.9% (122, 28% win) | -9.2% (148, 22% win) | -8.5% (189, 25% win) | -8.5% (213, 23% win) | -9.9% (246, 20% win) | -10.1% (278, 19% win) | -10.5% (295, 16% win) | -9.9% (241, 20% win) | -8.3% (209, 21% win) | -8.9% (159, 22% win) | -8.9% (111, 21% win) |
| volledige_screening+schoon | -5.4% (101, 27% win) | -8.8% (120, 19% win) | -9.6% (145, 23% win) | -11.6% (161, 20% win) | -12.5% (183, 17% win) | -11.4% (195, 18% win) | -10.2% (196, 16% win) | -9.9% (151, 20% win) | -9.1% (121, 21% win) | -10.3% (103, 19% win) | -7.8% (69, 20% win) |
| volledige_screening+schoon+x_link | -6.2% (74, 26% win) | -8.4% (84, 18% win) | -10.8% (94, 19% win) | -10.6% (99, 21% win) | -11.0% (109, 20% win) | -10.9% (115, 20% win) | -9.6% (119, 20% win) | -9.5% (105, 19% win) | -10.4% (85, 19% win) | -11.5% (73, 18% win) | -6.3% (50, 18% win) |


## Verkennend: winstgrens tegen dipdiepte

Elke winstgrens bij elke instapdiepte, filter `schoon+houders_ok`, stop als in de video. Dit is het raster waar 8 grenzen x 11 dieptes = 88 cellen uit komen. Bij zoveel cellen zit er door toeval altijd een goede tussen, dus **hier telt geen enkele cel als bewijs** — het is bedoeld om te zien of er ergens een gebied is dat consequent beter is, niet om de beste cel te kiezen.

| winstgrens | d30 | d35 | d40 | d45 | d50 | d55 | d60 | d65 | d70 | d75 | d80 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +10% | -8.0% (242) | -8.3% (285) | -8.7% (349) | -7.6% (387) | -7.9% (430) | -7.3% (486) | -5.9% (529) | -6.4% (488) | -6.8% (432) | -6.2% (358) | -6.6% (280) |
| +15% | -8.3% (242) | -8.6% (285) | -8.2% (349) | -7.4% (387) | -8.1% (430) | -7.2% (486) | -5.9% (529) | -6.8% (488) | -6.8% (432) | -6.1% (358) | -6.4% (280) |
| +20% | -8.0% (242) | -8.6% (285) | -8.2% (349) | -7.6% (387) | -8.2% (430) | -7.3% (486) | -6.4% (529) | -7.5% (488) | -7.0% (432) | -6.3% (358) | -6.2% (280) |
| +25% | -7.4% (242) | -8.2% (285) | -8.3% (349) | -7.5% (387) | -8.2% (430) | -7.3% (486) | -6.3% (529) | -7.5% (488) | -7.0% (432) | -6.2% (358) | -6.6% (280) |
| +30% | -6.7% (242) | -8.0% (285) | -8.1% (349) | -7.7% (387) | -8.8% (430) | -7.3% (486) | -6.5% (529) | -7.4% (488) | -7.3% (432) | -6.8% (358) | -6.8% (280) |
| +35% | -7.1% (242) | -8.9% (285) | -8.1% (349) | -7.6% (387) | -8.8% (430) | -7.4% (486) | -6.7% (529) | -7.0% (488) | -6.8% (432) | -6.3% (358) | -6.7% (280) |
| +45% | -7.2% (242) | -8.8% (285) | -8.6% (349) | -8.2% (387) | -8.8% (430) | -8.2% (486) | -6.9% (529) | -7.3% (488) | -6.2% (432) | -5.9% (358) | -6.3% (280) |
| +60% | -7.5% (242) | -9.0% (285) | -8.2% (349) | -7.9% (387) | -8.4% (430) | -8.8% (486) | -7.0% (529) | -6.5% (488) | -6.0% (432) | -6.2% (358) | -6.6% (280) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 161 instappen, mediane hoogste stijging +9.0%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 49% | 26% | -7.4% | 25% |
| +15% | 46% | 24% | -7.1% | 23% |
| +20% | 40% | 20% | -7.1% | 20% |
| +25% | 35% | 17% | -7.6% | 17% |
| +30% | 32% | 14% | -7.6% | 16% |
| +35% | 30% | 14% | -7.2% | 15% |
| +45% | 22% | 9% | -8.5% | 11% |
| +60% | 16% | 6% | -8.8% | 8% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 387 instappen, mediane hoogste stijging +9.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 50% | 25% | -7.6% | 25% |
| +15% | 47% | 21% | -7.4% | 23% |
| +20% | 42% | 18% | -7.6% | 20% |
| +25% | 39% | 16% | -7.5% | 19% |
| +30% | 36% | 14% | -7.7% | 17% |
| +35% | 34% | 12% | -7.6% | 16% |
| +45% | 28% | 9% | -8.2% | 12% |
| +60% | 24% | 8% | -7.9% | 11% |

**filter `alle`** — variant `d45_direct`, 7138 instappen, mediane hoogste stijging +20.1%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.7% | 30% |
| +15% | 54% | 28% | -5.6% | 28% |
| +20% | 50% | 25% | -5.6% | 27% |
| +25% | 47% | 22% | -5.8% | 26% |
| +30% | 44% | 20% | -5.8% | 25% |
| +35% | 42% | 18% | -5.9% | 24% |
| +45% | 38% | 15% | -6.1% | 22% |
| +60% | 33% | 12% | -6.2% | 21% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -7.6% (101, 18% win) | -7.0% (101, 18% win) | -5.2% (101, 18% win) | -4.6% (101, 18% win) | -7.5% (101, 18% win) | -6.9% (101, 18% win) |
| d35_direct | -13.2% (120, 10% win) | -12.6% (120, 10% win) | -10.8% (120, 10% win) | -10.2% (120, 10% win) | -13.0% (120, 10% win) | -12.3% (120, 10% win) |
| d40_direct | -12.4% (145, 9% win) | -11.8% (145, 10% win) | -10.1% (145, 10% win) | -9.4% (145, 10% win) | -12.4% (145, 9% win) | -11.7% (145, 10% win) |
| d45_direct | -11.6% (161, 9% win) | -10.9% (161, 10% win) | -9.2% (161, 10% win) | -8.5% (161, 11% win) | -11.7% (161, 9% win) | -11.1% (161, 10% win) |
| d50_direct | -12.9% (183, 7% win) | -12.3% (183, 7% win) | -10.6% (183, 7% win) | -9.9% (183, 7% win) | -13.2% (183, 7% win) | -12.6% (183, 7% win) |
| d55_direct | -12.5% (195, 7% win) | -11.9% (195, 7% win) | -10.2% (195, 7% win) | -9.6% (195, 7% win) | -13.1% (195, 7% win) | -12.4% (195, 7% win) |
| d60_direct | -11.2% (196, 6% win) | -10.5% (196, 6% win) | -8.9% (196, 6% win) | -8.2% (196, 6% win) | -11.9% (196, 6% win) | -11.3% (196, 6% win) |
| d65_direct | -11.2% (151, 7% win) | -10.5% (151, 7% win) | -8.9% (151, 7% win) | -8.2% (151, 7% win) | -11.9% (151, 6% win) | -11.2% (151, 7% win) |
| d70_direct | -9.3% (121, 7% win) | -8.7% (121, 7% win) | -7.1% (121, 8% win) | -6.4% (121, 8% win) | -10.2% (121, 7% win) | -9.5% (121, 7% win) |
| d75_direct | -9.2% (103, 7% win) | -8.6% (103, 7% win) | -7.0% (103, 7% win) | -6.3% (103, 7% win) | -10.2% (103, 7% win) | -9.5% (103, 7% win) |
| d80_direct | -8.5% (69, 6% win) | -7.8% (69, 6% win) | -6.3% (69, 6% win) | -5.6% (69, 7% win) | -9.6% (69, 6% win) | -9.0% (69, 6% win) |
| d45_herstel5 | -10.3% (114, 11% win) | -9.6% (114, 11% win) | -7.9% (114, 11% win) | -7.2% (114, 11% win) | -10.3% (114, 11% win) | -9.6% (114, 11% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.3% (242, 16% win) | -9.6% (242, 16% win) | -7.9% (242, 16% win) | -7.2% (242, 16% win) | -10.0% (242, 16% win) | -9.4% (242, 16% win) |
| d35_direct | -11.9% (285, 13% win) | -11.2% (285, 13% win) | -9.5% (285, 14% win) | -8.8% (285, 14% win) | -11.7% (285, 13% win) | -11.1% (285, 14% win) |
| d40_direct | -11.6% (349, 12% win) | -10.9% (349, 13% win) | -9.2% (349, 14% win) | -8.6% (349, 14% win) | -11.6% (349, 12% win) | -10.9% (349, 13% win) |
| d45_direct | -11.2% (387, 11% win) | -10.6% (387, 11% win) | -8.9% (387, 12% win) | -8.2% (387, 12% win) | -11.3% (387, 11% win) | -10.7% (387, 12% win) |
| d50_direct | -11.8% (430, 10% win) | -11.1% (430, 10% win) | -9.4% (430, 10% win) | -8.8% (430, 11% win) | -12.0% (430, 10% win) | -11.4% (430, 10% win) |
| d55_direct | -11.2% (486, 10% win) | -10.5% (486, 10% win) | -8.9% (486, 11% win) | -8.2% (486, 11% win) | -11.6% (486, 10% win) | -11.0% (486, 10% win) |
| d60_direct | -9.8% (529, 10% win) | -9.1% (529, 10% win) | -7.6% (529, 10% win) | -6.9% (529, 10% win) | -10.5% (529, 9% win) | -9.9% (529, 10% win) |
| d65_direct | -10.2% (488, 10% win) | -9.5% (488, 10% win) | -7.9% (488, 10% win) | -7.3% (488, 10% win) | -10.9% (488, 9% win) | -10.2% (488, 10% win) |
| d70_direct | -9.1% (432, 11% win) | -8.4% (432, 11% win) | -6.9% (432, 12% win) | -6.2% (432, 12% win) | -10.0% (432, 11% win) | -9.4% (432, 11% win) |
| d75_direct | -8.8% (358, 12% win) | -8.1% (358, 12% win) | -6.6% (358, 12% win) | -5.9% (358, 12% win) | -9.9% (358, 12% win) | -9.2% (358, 12% win) |
| d80_direct | -9.1% (280, 11% win) | -8.5% (280, 11% win) | -7.0% (280, 12% win) | -6.3% (280, 12% win) | -10.7% (280, 11% win) | -10.0% (280, 11% win) |
| d45_herstel5 | -7.9% (278, 17% win) | -7.2% (278, 18% win) | -5.5% (278, 18% win) | -4.8% (278, 18% win) | -7.8% (278, 17% win) | -7.2% (278, 18% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -8.6% (7611, 24% win) | -8.0% (7611, 24% win) | -6.3% (7611, 25% win) | -5.7% (7611, 25% win) | -9.0% (7611, 23% win) | -8.3% (7611, 24% win) |
| d35_direct | -9.4% (7436, 22% win) | -8.7% (7436, 23% win) | -7.1% (7436, 24% win) | -6.4% (7436, 24% win) | -9.8% (7436, 22% win) | -9.2% (7436, 22% win) |
| d40_direct | -9.5% (7283, 21% win) | -8.9% (7283, 22% win) | -7.3% (7283, 22% win) | -6.6% (7283, 23% win) | -10.2% (7283, 21% win) | -9.6% (7283, 21% win) |
| d45_direct | -8.9% (7138, 21% win) | -8.3% (7138, 21% win) | -6.7% (7138, 22% win) | -6.1% (7138, 22% win) | -9.8% (7138, 20% win) | -9.2% (7138, 21% win) |
| d50_direct | -9.0% (6995, 21% win) | -8.3% (6995, 21% win) | -6.8% (6995, 22% win) | -6.1% (6995, 22% win) | -10.1% (6995, 20% win) | -9.5% (6995, 20% win) |
| d55_direct | -9.1% (6695, 20% win) | -8.4% (6695, 20% win) | -7.0% (6695, 21% win) | -6.3% (6695, 21% win) | -10.6% (6695, 19% win) | -9.9% (6695, 19% win) |
| d60_direct | -8.9% (6137, 20% win) | -8.2% (6137, 20% win) | -6.9% (6137, 21% win) | -6.2% (6137, 21% win) | -10.7% (6137, 19% win) | -10.1% (6137, 19% win) |
| d65_direct | -8.1% (5469, 21% win) | -7.4% (5469, 22% win) | -6.1% (5469, 22% win) | -5.5% (5469, 23% win) | -10.4% (5469, 20% win) | -9.8% (5469, 20% win) |
| d70_direct | -8.1% (4783, 23% win) | -7.4% (4783, 23% win) | -6.3% (4783, 23% win) | -5.7% (4783, 24% win) | -11.2% (4783, 20% win) | -10.6% (4783, 21% win) |
| d75_direct | -8.3% (4203, 24% win) | -7.6% (4203, 24% win) | -6.7% (4203, 24% win) | -6.0% (4203, 24% win) | -12.3% (4203, 21% win) | -11.7% (4203, 21% win) |
| d80_direct | -8.1% (3638, 26% win) | -7.4% (3638, 26% win) | -6.8% (3638, 27% win) | -6.1% (3638, 27% win) | -13.7% (3638, 23% win) | -13.1% (3638, 23% win) |
| d45_herstel5 | -8.8% (5714, 25% win) | -8.1% (5714, 25% win) | -6.6% (5714, 26% win) | -5.9% (5714, 26% win) | -9.8% (5714, 24% win) | -9.2% (5714, 24% win) |


## Wat kost de uitvoering echt?

Wij rekenen met 0.001 SOL vaste kosten per transactie. De video van 14 sept gebruikt een tip van 0,02 SOL plus 0,001 prioriteitsfee — twintig keer zoveel. Een vaste fee werkt lineair door: elke extra T SOL per kant verlaagt het rendement met 2T gedeeld door de inzet. Onderstaande EV's zijn daarmee exact doorgerekend, niet opnieuw gesimuleerd. Filter `schoon+houders_ok`, videoregel, PumpPortal.

| extra vaste fee per transactie | inzet 0.05 SOL | inzet 0.2 SOL | inzet 1.0 SOL |
|---|---|---|---|
| +0.0 SOL | -10.6% | -8.2% | -10.7% |
| +0.005 SOL | -30.6% | -13.2% | -11.7% |
| +0.01 SOL | -50.6% | -18.2% | -12.7% |
| +0.02 SOL | -90.6% | -28.2% | -14.7% |

Bij 0,05 SOL inzet eet een tip van 0,02 SOL per kant 84% van de positie op. Een strategie met een randje van een paar procent bestaat bij die instellingen simpelweg niet; bij 1 SOL kost hij 4,2%. Dit verandert onze conclusie niet — de EV was al negatief — maar het laat zien dat kleine inzetten bij deze uitvoering sowieso kansloos zijn, en dat onze eigen cijfers aan de gunstige kant staan.



## Uitstapregels vergeleken (dip 45%, direct)

'Gespreid' is vier gelijke plakjes op +10%, +20%, +30% en +45%, allemaal met dezelfde stop — het advies uit de KOL-video om niet in één keer te verkopen. Dat is rekenkundig het gewogen gemiddelde van de vier losse grenzen, dus het kan de verwachting niet redden; het verandert alleen de spreiding.

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) | gespreid |
|---|---|---|---|---|
| alle | -6.1% (7138, 22% win) | -5.9% (7138, 22% win) | -7.6% (7138, 21% win) | -5.8% (7138, 25% win) |
| schoon | -6.2% (5793, 23% win) | -6.0% (5793, 23% win) | -7.3% (5793, 22% win) | -5.9% (5793, 26% win) |
| bundelgrafiek | -5.3% (1345, 20% win) | -5.3% (1345, 20% win) | -8.8% (1345, 18% win) | -5.3% (1345, 22% win) |
| schoon+houders_ok | -8.2% (387, 12% win) | -7.8% (387, 10% win) | -10.7% (387, 13% win) | -7.8% (387, 19% win) |
| schoon+houders_ok+final_stretch | -6.9% (213, 13% win) | -7.0% (213, 9% win) | -12.0% (213, 14% win) | -6.9% (213, 20% win) |
| volledige_screening+schoon | -8.5% (161, 11% win) | -9.0% (161, 6% win) | -15.4% (161, 11% win) | -7.7% (161, 19% win) |
| volledige_screening+schoon+x_link | -8.6% (99, 11% win) | -9.1% (99, 7% win) | -14.9% (99, 9% win) | -8.2% (99, 18% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.6% (2892, 28% win); 1,3–2x: -6.9% (2900, 19% win); ≥ 2x (bundelgrafiek): -5.3% (1346, 20% win)

**aandeel supply gekocht in creatieblok:** < 5%: -4.6% (4151, 30% win); 5–20%: -8.3% (1191, 13% win); ≥ 20%: -8.0% (1796, 13% win)

**top t.o.v. start:** 2–3x: -5.8% (4092, 21% win); 3–6x: -6.6% (2354, 24% win); ≥ 6x: -5.9% (692, 25% win)

**unieke kopers tot de top:** < 30: -5.0% (4235, 29% win); 30–100: -6.9% (1639, 13% win); ≥ 100: -8.7% (1264, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -5.9% (1823, 16% win); 1–2: -6.6% (3427, 24% win); ≥ 3 (trap): -5.3% (1888, 27% win)

**grootste koper, aandeel koopvolume:** < 10%: -7.8% (1908, 15% win); 10–25%: -8.9% (1324, 10% win); ≥ 25%: -4.3% (3906, 31% win)

**duur van top naar dip:** < 30 s (crash): -5.6% (5479, 26% win); 30 s–3 min: -7.2% (1309, 13% win); ≥ 3 min (langzaam): -8.4% (350, 10% win)

**tijd van start tot top:** < 2 min: -5.7% (5753, 25% win); 2–10 min: -8.1% (1115, 14% win); ≥ 10 min: -5.4% (270, 13% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
