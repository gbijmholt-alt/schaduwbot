# Videostrategie op alle trades — 2026-09-15 23:14 UTC

Tokens sinds 2026-09-13 11:14 UTC: 73409 geschikt (≥ 2 uur oud, geen herstart), 56398 met trades, 10106 haalden 2x de startkoers, 7827 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2304 tokens. Houdercheck echt uitgevoerd bij 95% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 354, winkans 13%, EV per trade -7.9% (95%-marge -10.1% tot -5.8%), mediaan -10.0%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 6350, winkans 21%, EV -7.4% (95%-marge -8.7% tot -6.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 181, winkans 19%, EV -9.9% (95%-marge -13.2% tot -6.5%).
- **H4** (2026-09-14 22:00 UTC): instap na een dip van 65% vanaf de top; stop op 75% onder de top zolang de winst onder +15% blijft; vanaf +15% een meelopende stop op 10% onder de hoogste koers; schone grafiek en houdercheck in orde. Aanleiding: voorstel van Gerben, 14 sept. Combineert de twee hefbomen die los gemeten het minst slecht waren: dieper instappen (d65-d70 gaf -3,8% tot -4,7% tegen -6,9% bij d45) en eerder winst vastleggen (+10% gaf -5,4% tegen -6,9% bij +45%), maar dan met een meelopende stop zodat een uitschieter niet wordt afgekapt. Filter is 'schoon+houders_ok' en niet de volledige screening, omdat die screening in drie onafhankelijke metingen averechts werkt. Verwachting vooraf, zodat die toetsbaar is: rond -3%, dus nog steeds negatief.. Resultaat: n = 3, winkans 33%, EV -4.2% (95%-marge -9.9% tot +1.6%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 7827 | 38% | 79% | 33% |
| schoon | 6350 | 39% | 79% | 35% |
| bundelgrafiek | 1477 | 34% | 78% | 24% |
| schoon+houders_ok | 354 | 27% | 81% | 7% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -5.9% (8322, 25% win) | -6.6% (8140, 24% win) | -6.8% (7975, 23% win) | -6.4% (7827, 22% win) | -6.4% (7674, 22% win) | -6.5% (7351, 21% win) | -6.4% (6736, 21% win) | -5.6% (5983, 22% win) | -5.9% (5229, 23% win) | -6.1% (4575, 24% win) | -6.0% (3951, 27% win) | -6.2% (6237, 26% win) |
| schoon | -6.6% (6724, 25% win) | -7.2% (6586, 23% win) | -7.2% (6466, 23% win) | -6.5% (6350, 23% win) | -6.3% (6215, 22% win) | -6.5% (5937, 22% win) | -6.3% (5406, 22% win) | -6.0% (4790, 23% win) | -6.0% (4192, 24% win) | -6.0% (3672, 26% win) | -6.0% (3220, 28% win) | -6.4% (5197, 26% win) |
| bundelgrafiek | -2.8% (1598, 27% win) | -4.2% (1554, 25% win) | -5.4% (1509, 22% win) | -6.0% (1477, 20% win) | -6.7% (1459, 18% win) | -6.6% (1414, 17% win) | -6.9% (1330, 16% win) | -4.0% (1193, 18% win) | -5.6% (1037, 17% win) | -6.6% (903, 17% win) | -5.6% (731, 20% win) | -5.2% (1040, 25% win) |
| schoon+houders_ok | -8.1% (212, 16% win) | -9.6% (255, 13% win) | -8.9% (316, 13% win) | -7.9% (354, 13% win) | -8.5% (396, 11% win) | -8.4% (448, 11% win) | -6.8% (486, 10% win) | -7.3% (446, 10% win) | -6.5% (396, 11% win) | -5.4% (335, 12% win) | -5.8% (262, 13% win) | -4.0% (253, 19% win) |
| schoon+houders_ok+final_stretch | -6.1% (105, 17% win) | -9.8% (131, 12% win) | -8.3% (169, 12% win) | -6.3% (195, 14% win) | -8.5% (228, 10% win) | -8.0% (259, 10% win) | -7.9% (274, 8% win) | -8.7% (223, 6% win) | -5.9% (194, 11% win) | -6.2% (152, 8% win) | -5.9% (107, 8% win) | -4.0% (142, 17% win) |
| volledige_screening+schoon | -4.0% (87, 20% win) | -10.5% (106, 10% win) | -10.0% (128, 9% win) | -7.9% (147, 12% win) | -9.5% (169, 8% win) | -9.3% (181, 8% win) | -8.1% (184, 6% win) | -8.8% (142, 6% win) | -7.0% (113, 8% win) | -6.2% (98, 7% win) | -5.5% (67, 8% win) | -6.6% (105, 12% win) |
| volledige_screening+schoon+x_link | -3.5% (65, 22% win) | -10.8% (75, 12% win) | -10.1% (84, 10% win) | -7.9% (90, 12% win) | -9.4% (100, 11% win) | -9.4% (106, 10% win) | -8.4% (110, 8% win) | -9.2% (98, 7% win) | -7.2% (79, 9% win) | -6.6% (68, 7% win) | -6.9% (48, 4% win) | -7.1% (64, 11% win) |

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
| alle | -6.7% (8322, 29% win) | -7.5% (8140, 28% win) | -7.4% (7975, 27% win) | -6.8% (7827, 26% win) | -6.9% (7674, 26% win) | -7.1% (7351, 26% win) | -7.2% (6736, 26% win) | -6.4% (5983, 27% win) | -6.3% (5229, 29% win) | -7.0% (4575, 31% win) | -7.4% (3951, 33% win) |
| schoon | -7.0% (6724, 29% win) | -7.7% (6586, 27% win) | -7.4% (6466, 27% win) | -6.7% (6350, 27% win) | -6.7% (6215, 27% win) | -7.0% (5937, 27% win) | -7.1% (5406, 27% win) | -6.4% (4790, 29% win) | -6.1% (4192, 31% win) | -6.7% (3672, 33% win) | -7.2% (3220, 35% win) |
| bundelgrafiek | -5.2% (1598, 30% win) | -6.4% (1554, 28% win) | -7.5% (1509, 24% win) | -7.3% (1477, 23% win) | -7.8% (1459, 21% win) | -7.8% (1414, 20% win) | -7.5% (1330, 20% win) | -6.3% (1193, 21% win) | -7.4% (1037, 21% win) | -8.2% (903, 22% win) | -8.0% (731, 25% win) |
| schoon+houders_ok | -7.9% (212, 24% win) | -9.2% (255, 22% win) | -8.8% (316, 22% win) | -8.9% (354, 22% win) | -9.7% (396, 19% win) | -8.5% (448, 20% win) | -8.4% (486, 18% win) | -8.7% (446, 20% win) | -8.2% (396, 21% win) | -7.2% (335, 24% win) | -6.8% (262, 27% win) |
| schoon+houders_ok+final_stretch | -7.0% (105, 27% win) | -11.0% (131, 20% win) | -9.7% (169, 21% win) | -10.2% (195, 21% win) | -10.8% (228, 19% win) | -8.8% (259, 20% win) | -10.2% (274, 15% win) | -11.3% (223, 15% win) | -7.4% (194, 22% win) | -7.2% (152, 24% win) | -7.3% (107, 23% win) |
| volledige_screening+schoon | -7.1% (87, 26% win) | -11.3% (106, 18% win) | -11.5% (128, 18% win) | -12.0% (147, 18% win) | -12.4% (169, 16% win) | -9.9% (181, 19% win) | -10.1% (184, 15% win) | -10.6% (142, 16% win) | -8.5% (113, 20% win) | -7.4% (98, 21% win) | -5.8% (67, 24% win) |
| volledige_screening+schoon+x_link | -7.2% (65, 26% win) | -10.5% (75, 19% win) | -12.3% (84, 18% win) | -12.5% (90, 18% win) | -11.2% (100, 19% win) | -7.8% (106, 24% win) | -8.3% (110, 20% win) | -9.7% (98, 18% win) | -8.3% (79, 20% win) | -5.7% (68, 24% win) | -5.5% (48, 25% win) |


## Regel H4: dip 65%, trailing stop vanaf +15% op 10% onder de piek

Tot +15% ligt de stop op hetzelfde niveau als bij de vorige regel — 10%-punt dieper dan de instap — zodat de positie eerst nog kan zakken. Vanaf +15% loopt de stop mee op 10% onder de hoogste koers, en ligt daarmee altijd boven de instapprijs. Geen vaste winstgrens: een uitschieter wordt niet afgekapt.

**Vooraf vastgelegd als H4 op d65 met filter schoon+houders_ok; de rest van deze regel is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.7% (8322, 28% win) | -7.4% (8140, 27% win) | -7.3% (7975, 26% win) | -7.1% (7827, 25% win) | -7.3% (7674, 25% win) | -7.1% (7351, 24% win) | -7.0% (6736, 24% win) | -6.0% (5983, 26% win) | -4.9% (5229, 27% win) | -6.6% (4575, 28% win) | -7.8% (3951, 29% win) |
| schoon | -7.3% (6724, 28% win) | -7.6% (6586, 26% win) | -7.2% (6466, 26% win) | -6.9% (6350, 26% win) | -7.0% (6215, 26% win) | -7.1% (5937, 25% win) | -6.6% (5406, 25% win) | -5.9% (4790, 27% win) | -4.3% (4192, 29% win) | -6.2% (3672, 30% win) | -7.7% (3220, 31% win) |
| bundelgrafiek | -4.0% (1598, 30% win) | -6.2% (1554, 27% win) | -7.5% (1509, 24% win) | -8.1% (1477, 21% win) | -8.5% (1459, 20% win) | -7.4% (1414, 20% win) | -8.4% (1330, 18% win) | -6.5% (1193, 19% win) | -7.4% (1037, 19% win) | -8.3% (903, 20% win) | -8.6% (731, 22% win) |
| schoon+houders_ok | -7.2% (212, 26% win) | -8.7% (255, 22% win) | -8.6% (316, 23% win) | -7.7% (354, 23% win) | -9.5% (396, 19% win) | -9.8% (448, 20% win) | -9.1% (486, 18% win) | -6.9% (446, 22% win) | -7.3% (396, 21% win) | -7.0% (335, 23% win) | -8.2% (262, 22% win) |
| schoon+houders_ok+final_stretch | -5.2% (105, 30% win) | -9.8% (131, 21% win) | -9.0% (169, 25% win) | -8.0% (195, 24% win) | -9.7% (228, 19% win) | -10.4% (259, 19% win) | -10.6% (274, 16% win) | -10.2% (223, 19% win) | -8.2% (194, 20% win) | -8.4% (152, 22% win) | -9.0% (107, 20% win) |
| volledige_screening+schoon | -4.7% (87, 30% win) | -9.8% (106, 17% win) | -10.5% (128, 23% win) | -11.2% (147, 22% win) | -12.5% (169, 17% win) | -11.5% (181, 18% win) | -10.3% (184, 16% win) | -10.7% (142, 19% win) | -9.4% (113, 20% win) | -10.3% (98, 19% win) | -7.9% (67, 19% win) |
| volledige_screening+schoon+x_link | -5.7% (65, 28% win) | -9.3% (75, 16% win) | -11.3% (84, 20% win) | -10.3% (90, 22% win) | -11.1% (100, 20% win) | -10.7% (106, 21% win) | -9.7% (110, 21% win) | -10.3% (98, 18% win) | -9.9% (79, 19% win) | -11.6% (68, 18% win) | -6.5% (48, 17% win) |


## Verkennend: winstgrens tegen dipdiepte

Elke winstgrens bij elke instapdiepte, filter `schoon+houders_ok`, stop als in de video. Dit is het raster waar 8 grenzen x 11 dieptes = 88 cellen uit komen. Bij zoveel cellen zit er door toeval altijd een goede tussen, dus **hier telt geen enkele cel als bewijs** — het is bedoeld om te zien of er ergens een gebied is dat consequent beter is, niet om de beste cel te kiezen.

| winstgrens | d30 | d35 | d40 | d45 | d50 | d55 | d60 | d65 | d70 | d75 | d80 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +10% | -8.1% (212) | -8.8% (255) | -9.2% (316) | -7.5% (354) | -7.6% (396) | -7.4% (448) | -5.8% (486) | -6.6% (446) | -7.0% (396) | -5.7% (335) | -6.0% (262) |
| +15% | -8.3% (212) | -9.3% (255) | -8.9% (316) | -7.4% (354) | -7.7% (396) | -7.4% (448) | -5.8% (486) | -7.0% (446) | -7.1% (396) | -5.6% (335) | -5.8% (262) |
| +20% | -8.2% (212) | -9.4% (255) | -9.0% (316) | -7.5% (354) | -7.9% (396) | -7.5% (448) | -6.2% (486) | -7.6% (446) | -7.2% (396) | -5.9% (335) | -5.9% (262) |
| +25% | -7.9% (212) | -8.8% (255) | -9.1% (316) | -7.3% (354) | -7.9% (396) | -7.4% (448) | -6.3% (486) | -7.6% (446) | -7.0% (396) | -5.9% (335) | -6.3% (262) |
| +30% | -7.2% (212) | -8.5% (255) | -8.7% (316) | -7.5% (354) | -8.4% (396) | -7.4% (448) | -6.4% (486) | -7.6% (446) | -7.4% (396) | -6.5% (335) | -6.1% (262) |
| +35% | -7.6% (212) | -9.5% (255) | -8.6% (316) | -7.2% (354) | -8.5% (396) | -7.5% (448) | -6.7% (486) | -7.2% (446) | -7.0% (396) | -6.0% (335) | -6.1% (262) |
| +45% | -8.1% (212) | -9.6% (255) | -8.9% (316) | -7.9% (354) | -8.5% (396) | -8.4% (448) | -6.8% (486) | -7.3% (446) | -6.5% (396) | -5.4% (335) | -5.8% (262) |
| +60% | -8.3% (212) | -9.3% (255) | -8.0% (316) | -7.4% (354) | -8.2% (396) | -9.0% (448) | -6.8% (486) | -6.4% (446) | -6.2% (396) | -5.8% (335) | -6.1% (262) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 147 instappen, mediane hoogste stijging +9.0%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 49% | 26% | -7.2% | 25% |
| +15% | 46% | 24% | -6.9% | 23% |
| +20% | 40% | 20% | -6.9% | 20% |
| +25% | 35% | 18% | -7.0% | 18% |
| +30% | 32% | 15% | -7.1% | 16% |
| +35% | 30% | 15% | -6.5% | 16% |
| +45% | 21% | 10% | -7.9% | 12% |
| +60% | 16% | 7% | -8.2% | 9% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 354 instappen, mediane hoogste stijging +9.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 50% | 25% | -7.5% | 26% |
| +15% | 47% | 21% | -7.4% | 23% |
| +20% | 42% | 18% | -7.5% | 20% |
| +25% | 39% | 16% | -7.3% | 19% |
| +30% | 36% | 14% | -7.5% | 18% |
| +35% | 34% | 13% | -7.2% | 16% |
| +45% | 28% | 9% | -7.9% | 13% |
| +60% | 25% | 8% | -7.4% | 12% |

**filter `alle`** — variant `d45_direct`, 7827 instappen, mediane hoogste stijging +19.3%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 56% | 31% | -6.0% | 29% |
| +15% | 53% | 28% | -5.9% | 28% |
| +20% | 50% | 24% | -6.0% | 26% |
| +25% | 46% | 22% | -6.1% | 25% |
| +30% | 44% | 20% | -6.2% | 24% |
| +35% | 42% | 18% | -6.2% | 24% |
| +45% | 38% | 15% | -6.4% | 22% |
| +60% | 32% | 12% | -6.5% | 20% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -7.1% (87, 20% win) | -6.4% (87, 20% win) | -4.7% (87, 20% win) | -4.0% (87, 20% win) | -7.0% (87, 20% win) | -6.3% (87, 20% win) |
| d35_direct | -13.6% (106, 10% win) | -12.9% (106, 10% win) | -11.1% (106, 10% win) | -10.5% (106, 10% win) | -13.2% (106, 10% win) | -12.6% (106, 10% win) |
| d40_direct | -13.1% (128, 8% win) | -12.4% (128, 9% win) | -10.7% (128, 9% win) | -10.0% (128, 9% win) | -13.0% (128, 8% win) | -12.3% (128, 9% win) |
| d45_direct | -10.9% (147, 10% win) | -10.2% (147, 11% win) | -8.6% (147, 11% win) | -7.9% (147, 12% win) | -11.1% (147, 10% win) | -10.4% (147, 11% win) |
| d50_direct | -12.5% (169, 7% win) | -11.8% (169, 7% win) | -10.2% (169, 8% win) | -9.5% (169, 8% win) | -12.8% (169, 7% win) | -12.2% (169, 7% win) |
| d55_direct | -12.3% (181, 7% win) | -11.6% (181, 7% win) | -10.0% (181, 8% win) | -9.3% (181, 8% win) | -12.8% (181, 7% win) | -12.2% (181, 7% win) |
| d60_direct | -11.0% (184, 6% win) | -10.3% (184, 6% win) | -8.8% (184, 6% win) | -8.1% (184, 6% win) | -11.8% (184, 6% win) | -11.2% (184, 6% win) |
| d65_direct | -11.8% (142, 6% win) | -11.1% (142, 6% win) | -9.5% (142, 6% win) | -8.8% (142, 6% win) | -12.4% (142, 5% win) | -11.8% (142, 6% win) |
| d70_direct | -10.0% (113, 7% win) | -9.3% (113, 7% win) | -7.7% (113, 8% win) | -7.0% (113, 8% win) | -10.8% (113, 7% win) | -10.1% (113, 7% win) |
| d75_direct | -9.1% (98, 7% win) | -8.4% (98, 7% win) | -6.9% (98, 7% win) | -6.2% (98, 7% win) | -10.0% (98, 7% win) | -9.4% (98, 7% win) |
| d80_direct | -8.4% (67, 6% win) | -7.7% (67, 6% win) | -6.2% (67, 6% win) | -5.5% (67, 8% win) | -9.5% (67, 6% win) | -8.9% (67, 6% win) |
| d45_herstel5 | -9.7% (105, 12% win) | -9.0% (105, 12% win) | -7.3% (105, 12% win) | -6.6% (105, 12% win) | -9.7% (105, 12% win) | -9.0% (105, 12% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -11.2% (212, 16% win) | -10.5% (212, 16% win) | -8.8% (212, 16% win) | -8.1% (212, 16% win) | -10.9% (212, 16% win) | -10.3% (212, 16% win) |
| d35_direct | -12.7% (255, 13% win) | -12.0% (255, 13% win) | -10.3% (255, 13% win) | -9.6% (255, 13% win) | -12.4% (255, 13% win) | -11.8% (255, 13% win) |
| d40_direct | -11.9% (316, 12% win) | -11.2% (316, 13% win) | -9.5% (316, 13% win) | -8.9% (316, 13% win) | -11.8% (316, 12% win) | -11.2% (316, 13% win) |
| d45_direct | -11.0% (354, 11% win) | -10.3% (354, 12% win) | -8.6% (354, 12% win) | -7.9% (354, 13% win) | -11.1% (354, 11% win) | -10.4% (354, 12% win) |
| d50_direct | -11.5% (396, 10% win) | -10.8% (396, 10% win) | -9.2% (396, 11% win) | -8.5% (396, 11% win) | -11.8% (396, 10% win) | -11.2% (396, 10% win) |
| d55_direct | -11.3% (448, 10% win) | -10.7% (448, 10% win) | -9.0% (448, 11% win) | -8.4% (448, 11% win) | -11.8% (448, 10% win) | -11.2% (448, 10% win) |
| d60_direct | -9.7% (486, 10% win) | -9.0% (486, 10% win) | -7.4% (486, 10% win) | -6.8% (486, 10% win) | -10.4% (486, 10% win) | -9.8% (486, 10% win) |
| d65_direct | -10.3% (446, 10% win) | -9.6% (446, 10% win) | -8.0% (446, 10% win) | -7.3% (446, 10% win) | -10.9% (446, 9% win) | -10.3% (446, 10% win) |
| d70_direct | -9.4% (396, 11% win) | -8.7% (396, 11% win) | -7.2% (396, 11% win) | -6.5% (396, 11% win) | -10.3% (396, 11% win) | -9.6% (396, 11% win) |
| d75_direct | -8.3% (335, 11% win) | -7.6% (335, 11% win) | -6.1% (335, 12% win) | -5.4% (335, 12% win) | -9.3% (335, 11% win) | -8.7% (335, 11% win) |
| d80_direct | -8.6% (262, 12% win) | -7.9% (262, 12% win) | -6.5% (262, 12% win) | -5.8% (262, 13% win) | -10.1% (262, 12% win) | -9.5% (262, 12% win) |
| d45_herstel5 | -7.1% (253, 18% win) | -6.4% (253, 19% win) | -4.7% (253, 19% win) | -4.0% (253, 19% win) | -7.0% (253, 18% win) | -6.4% (253, 19% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -8.9% (8322, 23% win) | -8.2% (8322, 24% win) | -6.6% (8322, 25% win) | -5.9% (8322, 25% win) | -9.2% (8322, 23% win) | -8.6% (8322, 24% win) |
| d35_direct | -9.6% (8140, 22% win) | -8.9% (8140, 22% win) | -7.3% (8140, 23% win) | -6.6% (8140, 24% win) | -10.1% (8140, 22% win) | -9.4% (8140, 22% win) |
| d40_direct | -9.8% (7975, 21% win) | -9.1% (7975, 21% win) | -7.5% (7975, 22% win) | -6.8% (7975, 23% win) | -10.4% (7975, 21% win) | -9.8% (7975, 21% win) |
| d45_direct | -9.3% (7827, 21% win) | -8.6% (7827, 21% win) | -7.0% (7827, 22% win) | -6.4% (7827, 22% win) | -10.2% (7827, 20% win) | -9.5% (7827, 21% win) |
| d50_direct | -9.2% (7674, 20% win) | -8.6% (7674, 20% win) | -7.1% (7674, 21% win) | -6.4% (7674, 22% win) | -10.4% (7674, 19% win) | -9.8% (7674, 20% win) |
| d55_direct | -9.3% (7351, 19% win) | -8.6% (7351, 20% win) | -7.2% (7351, 21% win) | -6.5% (7351, 21% win) | -10.8% (7351, 19% win) | -10.1% (7351, 19% win) |
| d60_direct | -9.1% (6736, 19% win) | -8.5% (6736, 20% win) | -7.1% (6736, 20% win) | -6.4% (6736, 21% win) | -10.9% (6736, 18% win) | -10.3% (6736, 19% win) |
| d65_direct | -8.2% (5983, 21% win) | -7.5% (5983, 21% win) | -6.3% (5983, 22% win) | -5.6% (5983, 22% win) | -10.5% (5983, 20% win) | -9.9% (5983, 20% win) |
| d70_direct | -8.4% (5229, 22% win) | -7.7% (5229, 22% win) | -6.6% (5229, 22% win) | -5.9% (5229, 23% win) | -11.5% (5229, 20% win) | -10.8% (5229, 20% win) |
| d75_direct | -8.4% (4575, 23% win) | -7.8% (4575, 24% win) | -6.8% (4575, 24% win) | -6.1% (4575, 24% win) | -12.4% (4575, 21% win) | -11.8% (4575, 21% win) |
| d80_direct | -7.9% (3951, 26% win) | -7.2% (3951, 26% win) | -6.7% (3951, 27% win) | -6.0% (3951, 27% win) | -13.6% (3951, 23% win) | -13.0% (3951, 23% win) |
| d45_herstel5 | -9.1% (6237, 24% win) | -8.4% (6237, 25% win) | -6.9% (6237, 25% win) | -6.2% (6237, 26% win) | -10.1% (6237, 23% win) | -9.5% (6237, 24% win) |


## Wat kost de uitvoering echt?

Wij rekenen met 0.001 SOL vaste kosten per transactie. De video van 14 sept gebruikt een tip van 0,02 SOL plus 0,001 prioriteitsfee — twintig keer zoveel. Een vaste fee werkt lineair door: elke extra T SOL per kant verlaagt het rendement met 2T gedeeld door de inzet. Onderstaande EV's zijn daarmee exact doorgerekend, niet opnieuw gesimuleerd. Filter `schoon+houders_ok`, videoregel, PumpPortal.

| extra vaste fee per transactie | inzet 0.05 SOL | inzet 0.2 SOL | inzet 1.0 SOL |
|---|---|---|---|
| +0.0 SOL | -10.3% | -7.9% | -10.4% |
| +0.005 SOL | -30.3% | -12.9% | -11.4% |
| +0.01 SOL | -50.3% | -17.9% | -12.4% |
| +0.02 SOL | -90.3% | -27.9% | -14.4% |

Bij 0,05 SOL inzet eet een tip van 0,02 SOL per kant 84% van de positie op. Een strategie met een randje van een paar procent bestaat bij die instellingen simpelweg niet; bij 1 SOL kost hij 4,2%. Dit verandert onze conclusie niet — de EV was al negatief — maar het laat zien dat kleine inzetten bij deze uitvoering sowieso kansloos zijn, en dat onze eigen cijfers aan de gunstige kant staan.



## Uitstapregels vergeleken (dip 45%, direct)

'Gespreid' is vier gelijke plakjes op +10%, +20%, +30% en +45%, allemaal met dezelfde stop — het advies uit de KOL-video om niet in één keer te verkopen. Dat is rekenkundig het gewogen gemiddelde van de vier losse grenzen, dus het kan de verwachting niet redden; het verandert alleen de spreiding.

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) | gespreid |
|---|---|---|---|---|
| alle | -6.4% (7827, 22% win) | -6.2% (7827, 22% win) | -7.7% (7827, 21% win) | -6.1% (7827, 25% win) |
| schoon | -6.5% (6350, 23% win) | -6.2% (6350, 22% win) | -7.4% (6350, 21% win) | -6.2% (6350, 26% win) |
| bundelgrafiek | -6.0% (1477, 20% win) | -5.9% (1477, 19% win) | -9.2% (1477, 18% win) | -5.9% (1477, 22% win) |
| schoon+houders_ok | -7.9% (354, 13% win) | -7.6% (354, 10% win) | -10.8% (354, 14% win) | -7.6% (354, 20% win) |
| schoon+houders_ok+final_stretch | -6.3% (195, 14% win) | -6.6% (195, 10% win) | -11.6% (195, 14% win) | -6.4% (195, 20% win) |
| volledige_screening+schoon | -7.9% (147, 12% win) | -8.6% (147, 6% win) | -15.2% (147, 12% win) | -7.3% (147, 20% win) |
| volledige_screening+schoon+x_link | -7.9% (90, 12% win) | -8.6% (90, 8% win) | -14.8% (90, 10% win) | -7.9% (90, 19% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.9% (3094, 27% win); 1,3–2x: -6.9% (3255, 18% win); ≥ 2x (bundelgrafiek): -6.0% (1478, 20% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.0% (4436, 29% win); 5–20%: -8.3% (1306, 13% win); ≥ 20%: -8.2% (2085, 12% win)

**top t.o.v. start:** 2–3x: -6.0% (4485, 21% win); 3–6x: -7.1% (2565, 24% win); ≥ 6x: -6.0% (777, 24% win)

**unieke kopers tot de top:** < 30: -5.4% (4560, 28% win); 30–100: -7.0% (1805, 13% win); ≥ 100: -8.8% (1462, 13% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.7% (2052, 15% win); 1–2: -6.5% (3748, 24% win); ≥ 3 (trap): -5.8% (2027, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -7.9% (2144, 14% win); 10–25%: -8.7% (1524, 11% win); ≥ 25%: -4.8% (4159, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.1% (6039, 25% win); 30 s–3 min: -7.0% (1422, 14% win); ≥ 3 min (langzaam): -8.7% (366, 10% win)

**tijd van start tot top:** < 2 min: -5.9% (6322, 24% win); 2–10 min: -8.8% (1210, 14% win); ≥ 10 min: -6.2% (295, 13% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
