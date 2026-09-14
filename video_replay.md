# Videostrategie op alle trades — 2026-09-14 01:15 UTC

Tokens sinds 2026-09-11 08:47 UTC: 51823 geschikt (≥ 2 uur oud, geen herstart), 40564 met trades, 7310 haalden 2x de startkoers, 5603 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1744 tokens. Houdercheck echt uitgevoerd bij 91% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1429, winkans 20%, EV per trade -7.1% (95%-marge -8.8% tot -5.5%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 3989, winkans 23%, EV -6.7% (95%-marge -8.4% tot -4.9%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 102, winkans 16%, EV -10.5% (95%-marge -14.5% tot -6.6%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 5603 | 40% | 76% | 37% |
| schoon | 4478 | 43% | 76% | 40% |
| bundelgrafiek | 1125 | 30% | 77% | 24% |
| schoon+houders_ok | 1429 | 37% | 79% | 24% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.5% (5988, 25% win) | -6.6% (5864, 24% win) | -6.9% (5737, 23% win) | -6.6% (5603, 23% win) | -7.0% (5476, 22% win) | -7.0% (5280, 21% win) | -6.5% (4905, 22% win) | -6.3% (4389, 24% win) | -5.8% (3890, 25% win) | -6.3% (3424, 25% win) | -7.0% (2975, 27% win) | -6.2% (4609, 27% win) |
| schoon | -6.5% (4781, 25% win) | -6.4% (4693, 25% win) | -6.7% (4595, 24% win) | -6.3% (4478, 24% win) | -6.4% (4376, 24% win) | -6.8% (4212, 23% win) | -6.1% (3882, 24% win) | -5.5% (3462, 26% win) | -5.2% (3097, 27% win) | -5.7% (2738, 27% win) | -6.7% (2420, 29% win) | -5.9% (3854, 27% win) |
| bundelgrafiek | -6.5% (1207, 24% win) | -7.7% (1171, 21% win) | -8.0% (1142, 19% win) | -7.4% (1125, 18% win) | -9.5% (1100, 15% win) | -8.0% (1068, 14% win) | -8.2% (1023, 15% win) | -9.3% (927, 14% win) | -8.1% (793, 17% win) | -8.5% (686, 17% win) | -8.4% (555, 19% win) | -7.8% (755, 24% win) |
| schoon+houders_ok | -6.5% (1114, 21% win) | -6.9% (1223, 20% win) | -7.2% (1344, 19% win) | -7.1% (1429, 20% win) | -6.9% (1528, 20% win) | -5.7% (1626, 20% win) | -5.1% (1673, 20% win) | -4.9% (1523, 21% win) | -4.4% (1383, 23% win) | -5.1% (1204, 24% win) | -5.5% (1052, 27% win) | -4.4% (1175, 23% win) |
| schoon+houders_ok+final_stretch | -7.1% (476, 17% win) | -7.3% (523, 15% win) | -8.0% (574, 12% win) | -8.8% (607, 12% win) | -8.6% (643, 10% win) | -7.7% (673, 10% win) | -6.8% (670, 10% win) | -6.6% (525, 10% win) | -7.5% (407, 9% win) | -7.6% (272, 8% win) | -5.8% (171, 10% win) | -6.0% (470, 15% win) |
| volledige_screening+schoon | -6.9% (334, 16% win) | -7.0% (352, 15% win) | -8.4% (369, 13% win) | -9.7% (390, 11% win) | -9.4% (406, 9% win) | -8.6% (411, 8% win) | -7.2% (400, 8% win) | -7.2% (313, 9% win) | -8.2% (239, 6% win) | -8.5% (169, 6% win) | -8.3% (107, 5% win) | -7.5% (286, 13% win) |
| volledige_screening+schoon+x_link | -7.3% (255, 17% win) | -6.1% (269, 18% win) | -8.5% (276, 14% win) | -9.8% (283, 11% win) | -9.6% (283, 9% win) | -9.2% (285, 8% win) | -8.4% (278, 7% win) | -8.5% (223, 7% win) | -8.2% (168, 6% win) | -9.1% (121, 5% win) | -9.2% (77, 1% win) | -7.5% (201, 13% win) |

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
| alle | -6.2% (5988, 30% win) | -6.5% (5864, 29% win) | -6.6% (5737, 28% win) | -6.4% (5603, 28% win) | -7.3% (5476, 26% win) | -6.9% (5280, 26% win) | -6.7% (4905, 27% win) | -6.5% (4389, 28% win) | -6.4% (3890, 30% win) | -6.5% (3424, 32% win) | -7.6% (2975, 33% win) |
| schoon | -6.2% (4781, 30% win) | -6.3% (4693, 30% win) | -6.5% (4595, 29% win) | -6.3% (4478, 29% win) | -7.1% (4376, 28% win) | -6.9% (4212, 27% win) | -6.5% (3882, 29% win) | -5.9% (3462, 31% win) | -5.8% (3097, 33% win) | -5.8% (2738, 34% win) | -7.0% (2420, 35% win) |
| bundelgrafiek | -6.3% (1207, 27% win) | -7.5% (1171, 25% win) | -7.1% (1142, 23% win) | -6.8% (1125, 21% win) | -7.9% (1100, 20% win) | -6.8% (1068, 20% win) | -7.5% (1023, 18% win) | -9.0% (927, 17% win) | -8.9% (793, 20% win) | -9.1% (686, 22% win) | -10.1% (555, 23% win) |
| schoon+houders_ok | -6.4% (1114, 28% win) | -6.5% (1223, 28% win) | -6.5% (1344, 27% win) | -6.8% (1429, 28% win) | -7.3% (1528, 26% win) | -6.0% (1626, 26% win) | -5.4% (1673, 27% win) | -5.2% (1523, 29% win) | -4.4% (1383, 32% win) | -4.9% (1204, 33% win) | -6.7% (1052, 34% win) |
| schoon+houders_ok+final_stretch | -6.7% (476, 25% win) | -7.1% (523, 24% win) | -7.4% (574, 23% win) | -9.2% (607, 21% win) | -10.4% (643, 17% win) | -9.4% (673, 18% win) | -7.2% (670, 20% win) | -7.5% (525, 22% win) | -8.3% (407, 23% win) | -7.3% (272, 26% win) | -6.0% (171, 26% win) |
| volledige_screening+schoon | -6.9% (334, 25% win) | -7.3% (352, 24% win) | -8.1% (369, 24% win) | -10.3% (390, 20% win) | -11.3% (406, 16% win) | -10.7% (411, 16% win) | -8.1% (400, 18% win) | -8.2% (313, 20% win) | -10.6% (239, 18% win) | -9.7% (169, 20% win) | -9.0% (107, 19% win) |
| volledige_screening+schoon+x_link | -6.9% (255, 26% win) | -6.5% (269, 25% win) | -8.3% (276, 23% win) | -10.9% (283, 19% win) | -12.0% (283, 14% win) | -10.5% (285, 15% win) | -7.8% (278, 18% win) | -8.2% (223, 18% win) | -9.7% (168, 18% win) | -9.6% (121, 19% win) | -9.1% (77, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 390 instappen, mediane hoogste stijging +8.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -7.8% | 26% |
| +15% | 43% | 20% | -7.9% | 22% |
| +20% | 40% | 18% | -7.9% | 20% |
| +25% | 34% | 15% | -8.4% | 17% |
| +30% | 32% | 13% | -8.5% | 15% |
| +35% | 29% | 12% | -8.5% | 14% |
| +45% | 24% | 8% | -9.7% | 11% |
| +60% | 20% | 6% | -9.5% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1429 instappen, mediane hoogste stijging +20.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 58% | 33% | -5.5% | 31% |
| +15% | 54% | 27% | -5.6% | 28% |
| +20% | 50% | 24% | -5.7% | 26% |
| +25% | 47% | 21% | -5.9% | 24% |
| +30% | 44% | 19% | -6.1% | 23% |
| +35% | 41% | 16% | -6.3% | 22% |
| +45% | 37% | 13% | -7.1% | 20% |
| +60% | 32% | 10% | -7.0% | 18% |

**filter `alle`** — variant `d45_direct`, 5603 instappen, mediane hoogste stijging +22.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.8% | 30% |
| +15% | 55% | 30% | -5.9% | 28% |
| +20% | 52% | 26% | -6.0% | 27% |
| +25% | 49% | 24% | -6.1% | 26% |
| +30% | 46% | 21% | -6.2% | 25% |
| +35% | 44% | 19% | -6.4% | 24% |
| +45% | 39% | 16% | -6.6% | 23% |
| +60% | 35% | 13% | -6.4% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.9% (334, 15% win) | -9.2% (334, 16% win) | -7.5% (334, 16% win) | -6.9% (334, 16% win) | -9.9% (334, 15% win) | -9.3% (334, 15% win) |
| d35_direct | -10.0% (352, 15% win) | -9.3% (352, 15% win) | -7.7% (352, 15% win) | -7.0% (352, 15% win) | -10.1% (352, 15% win) | -9.4% (352, 15% win) |
| d40_direct | -11.4% (369, 12% win) | -10.7% (369, 13% win) | -9.0% (369, 13% win) | -8.4% (369, 13% win) | -11.5% (369, 12% win) | -10.8% (369, 12% win) |
| d45_direct | -12.7% (390, 10% win) | -12.0% (390, 10% win) | -10.3% (390, 11% win) | -9.7% (390, 11% win) | -12.8% (390, 10% win) | -12.2% (390, 10% win) |
| d50_direct | -12.3% (406, 8% win) | -11.7% (406, 8% win) | -10.0% (406, 9% win) | -9.4% (406, 9% win) | -12.7% (406, 8% win) | -12.1% (406, 8% win) |
| d55_direct | -11.5% (411, 8% win) | -10.9% (411, 8% win) | -9.2% (411, 8% win) | -8.6% (411, 8% win) | -12.1% (411, 7% win) | -11.5% (411, 8% win) |
| d60_direct | -10.1% (400, 8% win) | -9.4% (400, 8% win) | -7.8% (400, 8% win) | -7.2% (400, 8% win) | -10.9% (400, 7% win) | -10.3% (400, 8% win) |
| d65_direct | -10.1% (313, 9% win) | -9.4% (313, 9% win) | -7.9% (313, 9% win) | -7.2% (313, 9% win) | -11.0% (313, 8% win) | -10.4% (313, 9% win) |
| d70_direct | -11.0% (239, 6% win) | -10.3% (239, 6% win) | -8.8% (239, 6% win) | -8.2% (239, 6% win) | -12.0% (239, 5% win) | -11.3% (239, 5% win) |
| d75_direct | -11.3% (169, 5% win) | -10.6% (169, 5% win) | -9.1% (169, 6% win) | -8.5% (169, 6% win) | -12.4% (169, 5% win) | -11.8% (169, 5% win) |
| d80_direct | -11.1% (107, 5% win) | -10.4% (107, 5% win) | -9.0% (107, 5% win) | -8.3% (107, 5% win) | -12.6% (107, 4% win) | -12.0% (107, 4% win) |
| d45_herstel5 | -10.5% (286, 13% win) | -9.9% (286, 13% win) | -8.2% (286, 13% win) | -7.5% (286, 13% win) | -10.6% (286, 13% win) | -9.9% (286, 13% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (1114, 19% win) | -8.9% (1114, 19% win) | -7.2% (1114, 20% win) | -6.5% (1114, 21% win) | -9.2% (1114, 20% win) | -8.6% (1114, 20% win) |
| d35_direct | -10.0% (1223, 18% win) | -9.3% (1223, 19% win) | -7.6% (1223, 20% win) | -6.9% (1223, 20% win) | -9.8% (1223, 18% win) | -9.2% (1223, 19% win) |
| d40_direct | -10.3% (1344, 18% win) | -9.6% (1344, 18% win) | -7.9% (1344, 19% win) | -7.2% (1344, 19% win) | -10.2% (1344, 18% win) | -9.6% (1344, 18% win) |
| d45_direct | -10.2% (1429, 17% win) | -9.5% (1429, 18% win) | -7.8% (1429, 19% win) | -7.1% (1429, 20% win) | -10.2% (1429, 17% win) | -9.6% (1429, 18% win) |
| d50_direct | -10.0% (1528, 18% win) | -9.3% (1528, 18% win) | -7.6% (1528, 19% win) | -6.9% (1528, 20% win) | -10.2% (1528, 17% win) | -9.6% (1528, 18% win) |
| d55_direct | -8.7% (1626, 18% win) | -8.0% (1626, 18% win) | -6.4% (1626, 19% win) | -5.7% (1626, 20% win) | -9.2% (1626, 17% win) | -8.6% (1626, 18% win) |
| d60_direct | -8.1% (1673, 18% win) | -7.3% (1673, 19% win) | -5.8% (1673, 20% win) | -5.1% (1673, 20% win) | -8.9% (1673, 18% win) | -8.3% (1673, 18% win) |
| d65_direct | -7.8% (1523, 20% win) | -7.1% (1523, 20% win) | -5.6% (1523, 21% win) | -4.9% (1523, 21% win) | -8.9% (1523, 19% win) | -8.3% (1523, 20% win) |
| d70_direct | -7.1% (1383, 22% win) | -6.4% (1383, 22% win) | -5.1% (1383, 23% win) | -4.4% (1383, 23% win) | -8.8% (1383, 21% win) | -8.2% (1383, 22% win) |
| d75_direct | -7.8% (1204, 23% win) | -7.1% (1204, 23% win) | -5.8% (1204, 24% win) | -5.1% (1204, 24% win) | -10.2% (1204, 21% win) | -9.5% (1204, 22% win) |
| d80_direct | -7.9% (1052, 25% win) | -7.2% (1052, 26% win) | -6.2% (1052, 26% win) | -5.5% (1052, 27% win) | -11.6% (1052, 23% win) | -11.0% (1052, 23% win) |
| d45_herstel5 | -7.4% (1175, 22% win) | -6.7% (1175, 22% win) | -5.1% (1175, 23% win) | -4.4% (1175, 23% win) | -7.5% (1175, 22% win) | -6.9% (1175, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.5% (5988, 23% win) | -8.8% (5988, 24% win) | -7.2% (5988, 25% win) | -6.5% (5988, 25% win) | -9.7% (5988, 23% win) | -9.1% (5988, 24% win) |
| d35_direct | -9.6% (5864, 22% win) | -8.9% (5864, 23% win) | -7.3% (5864, 24% win) | -6.6% (5864, 24% win) | -10.0% (5864, 22% win) | -9.3% (5864, 22% win) |
| d40_direct | -9.9% (5737, 22% win) | -9.2% (5737, 22% win) | -7.6% (5737, 23% win) | -6.9% (5737, 23% win) | -10.4% (5737, 21% win) | -9.8% (5737, 21% win) |
| d45_direct | -9.4% (5603, 21% win) | -8.8% (5603, 22% win) | -7.2% (5603, 22% win) | -6.6% (5603, 23% win) | -10.3% (5603, 21% win) | -9.6% (5603, 21% win) |
| d50_direct | -9.9% (5476, 20% win) | -9.2% (5476, 21% win) | -7.7% (5476, 22% win) | -7.0% (5476, 22% win) | -10.9% (5476, 20% win) | -10.3% (5476, 20% win) |
| d55_direct | -9.8% (5280, 20% win) | -9.1% (5280, 20% win) | -7.7% (5280, 21% win) | -7.0% (5280, 21% win) | -11.1% (5280, 18% win) | -10.5% (5280, 19% win) |
| d60_direct | -9.2% (4905, 21% win) | -8.6% (4905, 21% win) | -7.2% (4905, 22% win) | -6.5% (4905, 22% win) | -11.0% (4905, 19% win) | -10.3% (4905, 20% win) |
| d65_direct | -9.0% (4389, 22% win) | -8.3% (4389, 22% win) | -7.0% (4389, 23% win) | -6.3% (4389, 24% win) | -11.2% (4389, 20% win) | -10.5% (4389, 21% win) |
| d70_direct | -8.3% (3890, 24% win) | -7.6% (3890, 24% win) | -6.4% (3890, 25% win) | -5.8% (3890, 25% win) | -11.2% (3890, 22% win) | -10.6% (3890, 22% win) |
| d75_direct | -8.6% (3424, 24% win) | -7.9% (3424, 24% win) | -7.0% (3424, 25% win) | -6.3% (3424, 25% win) | -12.6% (3424, 21% win) | -12.0% (3424, 22% win) |
| d80_direct | -8.9% (2975, 26% win) | -8.3% (2975, 27% win) | -7.7% (2975, 27% win) | -7.0% (2975, 27% win) | -14.7% (2975, 22% win) | -14.1% (2975, 23% win) |
| d45_herstel5 | -9.1% (4609, 25% win) | -8.4% (4609, 25% win) | -6.9% (4609, 26% win) | -6.2% (4609, 27% win) | -10.2% (4609, 24% win) | -9.5% (4609, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.6% (5603, 23% win) | -6.2% (5603, 22% win) | -6.5% (5603, 22% win) |
| schoon | -6.3% (4478, 24% win) | -6.1% (4478, 24% win) | -6.2% (4478, 24% win) |
| bundelgrafiek | -7.4% (1125, 18% win) | -6.7% (1125, 18% win) | -7.6% (1125, 16% win) |
| schoon+houders_ok | -7.1% (1429, 20% win) | -6.7% (1429, 19% win) | -6.3% (1429, 20% win) |
| schoon+houders_ok+final_stretch | -8.8% (607, 12% win) | -7.5% (607, 11% win) | -9.7% (607, 14% win) |
| volledige_screening+schoon | -9.7% (390, 11% win) | -8.5% (390, 9% win) | -11.0% (390, 14% win) |
| volledige_screening+schoon+x_link | -9.8% (283, 11% win) | -8.6% (283, 9% win) | -11.1% (283, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.2% (2408, 28% win); 1,3–2x: -7.6% (2069, 19% win); ≥ 2x (bundelgrafiek): -7.5% (1126, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.7% (3560, 29% win); 5–20%: -8.4% (966, 13% win); ≥ 20%: -7.6% (1077, 12% win)

**top t.o.v. start:** 2–3x: -6.7% (3137, 22% win); 3–6x: -6.1% (1931, 24% win); ≥ 6x: -7.6% (535, 25% win)

**unieke kopers tot de top:** < 30: -5.8% (3547, 29% win); 30–100: -7.1% (1161, 12% win); ≥ 100: -8.7% (895, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.3% (1378, 16% win); 1–2: -6.2% (2673, 24% win); ≥ 3 (trap): -6.5% (1552, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.5% (1349, 13% win); 10–25%: -7.8% (922, 13% win); ≥ 25%: -5.4% (3332, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (4417, 25% win); 30 s–3 min: -8.3% (939, 15% win); ≥ 3 min (langzaam): -10.2% (247, 7% win)

**tijd van start tot top:** < 2 min: -6.3% (4610, 24% win); 2–10 min: -7.3% (793, 16% win); ≥ 10 min: -9.7% (200, 13% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
