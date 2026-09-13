# Videostrategie op alle trades — 2026-09-13 18:21 UTC

Tokens sinds 2026-09-11 08:47 UTC: 42541 geschikt (≥ 2 uur oud, geen herstart), 33546 met trades, 6232 haalden 2x de startkoers, 4753 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1475 tokens. Houdercheck echt uitgevoerd bij 90% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1346, winkans 20%, EV per trade -7.2% (95%-marge -8.9% tot -5.5%), mediaan -10.6%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 3317, winkans 23%, EV -7.2% (95%-marge -9.0% tot -5.5%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 56, winkans 21%, EV -9.4% (95%-marge -14.9% tot -3.9%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4753 | 40% | 77% | 37% |
| schoon | 3806 | 42% | 76% | 40% |
| bundelgrafiek | 947 | 29% | 79% | 24% |
| schoon+houders_ok | 1346 | 37% | 79% | 25% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.4% (5086, 25% win) | -6.7% (4981, 24% win) | -6.9% (4871, 23% win) | -6.6% (4753, 23% win) | -6.9% (4652, 22% win) | -6.9% (4484, 21% win) | -6.4% (4170, 22% win) | -6.3% (3726, 24% win) | -5.8% (3295, 25% win) | -6.5% (2905, 25% win) | -6.9% (2528, 27% win) | -6.4% (3892, 27% win) |
| schoon | -6.3% (4075, 26% win) | -6.3% (3999, 25% win) | -6.6% (3909, 24% win) | -6.4% (3806, 24% win) | -6.5% (3728, 24% win) | -6.9% (3587, 23% win) | -6.1% (3306, 24% win) | -5.6% (2950, 26% win) | -5.2% (2635, 27% win) | -6.1% (2337, 27% win) | -6.7% (2064, 29% win) | -6.1% (3267, 27% win) |
| bundelgrafiek | -6.7% (1011, 22% win) | -8.1% (982, 19% win) | -7.8% (962, 18% win) | -7.4% (947, 17% win) | -8.8% (924, 15% win) | -7.1% (897, 15% win) | -7.4% (864, 16% win) | -9.2% (776, 15% win) | -7.8% (660, 17% win) | -8.2% (568, 18% win) | -7.9% (464, 19% win) | -8.3% (625, 23% win) |
| schoon+houders_ok | -6.5% (1075, 21% win) | -6.8% (1176, 20% win) | -7.2% (1276, 20% win) | -7.2% (1346, 20% win) | -6.8% (1437, 20% win) | -5.6% (1524, 20% win) | -5.2% (1557, 20% win) | -4.7% (1417, 22% win) | -4.2% (1279, 24% win) | -5.3% (1125, 25% win) | -5.3% (989, 28% win) | -4.4% (1115, 23% win) |
| schoon+houders_ok+final_stretch | -7.1% (455, 17% win) | -7.2% (495, 15% win) | -8.0% (532, 13% win) | -8.9% (557, 12% win) | -8.4% (582, 10% win) | -7.6% (607, 10% win) | -6.8% (595, 10% win) | -6.3% (465, 11% win) | -7.8% (347, 8% win) | -8.0% (233, 8% win) | -5.2% (143, 12% win) | -6.0% (435, 15% win) |
| volledige_screening+schoon | -7.0% (317, 16% win) | -6.8% (330, 16% win) | -8.6% (338, 13% win) | -9.9% (351, 11% win) | -9.3% (361, 10% win) | -8.5% (365, 8% win) | -7.2% (353, 8% win) | -7.2% (278, 9% win) | -8.8% (207, 6% win) | -9.2% (144, 6% win) | -8.1% (91, 6% win) | -7.3% (261, 14% win) |
| volledige_screening+schoon+x_link | -7.6% (246, 17% win) | -5.8% (256, 19% win) | -8.8% (258, 14% win) | -10.0% (262, 11% win) | -9.7% (262, 9% win) | -9.3% (265, 8% win) | -8.6% (260, 7% win) | -8.3% (206, 7% win) | -8.8% (155, 5% win) | -9.0% (112, 5% win) | -9.1% (71, 1% win) | -7.6% (189, 14% win) |

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
| alle | -5.9% (5086, 30% win) | -6.2% (4981, 29% win) | -6.2% (4871, 28% win) | -6.4% (4753, 28% win) | -7.2% (4652, 26% win) | -6.9% (4484, 26% win) | -6.6% (4170, 27% win) | -6.9% (3726, 28% win) | -6.6% (3295, 31% win) | -6.6% (2905, 32% win) | -7.7% (2528, 33% win) |
| schoon | -5.8% (4075, 31% win) | -5.9% (3999, 30% win) | -6.2% (3909, 30% win) | -6.3% (3806, 29% win) | -7.1% (3728, 28% win) | -7.1% (3587, 27% win) | -6.6% (3306, 29% win) | -6.4% (2950, 31% win) | -6.2% (2635, 33% win) | -6.1% (2337, 34% win) | -7.1% (2064, 35% win) |
| bundelgrafiek | -6.5% (1011, 26% win) | -7.5% (982, 24% win) | -6.6% (962, 22% win) | -6.9% (947, 20% win) | -7.4% (924, 20% win) | -6.2% (897, 20% win) | -6.9% (864, 18% win) | -8.6% (776, 17% win) | -8.4% (660, 20% win) | -8.5% (568, 22% win) | -10.3% (464, 23% win) |
| schoon+houders_ok | -6.3% (1075, 28% win) | -6.4% (1176, 28% win) | -6.5% (1276, 28% win) | -6.9% (1346, 28% win) | -7.2% (1437, 27% win) | -5.9% (1524, 27% win) | -5.1% (1557, 28% win) | -5.1% (1417, 30% win) | -4.3% (1279, 33% win) | -4.8% (1125, 34% win) | -6.6% (989, 34% win) |
| schoon+houders_ok+final_stretch | -6.7% (455, 25% win) | -6.7% (495, 24% win) | -6.9% (532, 24% win) | -8.9% (557, 21% win) | -10.2% (582, 18% win) | -9.4% (607, 18% win) | -6.7% (595, 21% win) | -7.2% (465, 22% win) | -9.0% (347, 22% win) | -7.2% (233, 25% win) | -5.4% (143, 27% win) |
| volledige_screening+schoon | -6.8% (317, 26% win) | -6.9% (330, 24% win) | -7.6% (338, 25% win) | -10.2% (351, 21% win) | -11.3% (361, 17% win) | -10.5% (365, 18% win) | -7.7% (353, 19% win) | -8.4% (278, 19% win) | -11.8% (207, 16% win) | -10.0% (144, 18% win) | -9.1% (91, 18% win) |
| volledige_screening+schoon+x_link | -7.0% (246, 26% win) | -6.3% (256, 25% win) | -7.6% (258, 24% win) | -10.6% (262, 20% win) | -12.1% (262, 14% win) | -10.9% (265, 16% win) | -7.8% (260, 18% win) | -8.2% (206, 18% win) | -10.3% (155, 17% win) | -9.8% (112, 19% win) | -10.0% (71, 14% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 351 instappen, mediane hoogste stijging +8.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -7.9% | 26% |
| +15% | 43% | 20% | -8.0% | 22% |
| +20% | 40% | 18% | -8.0% | 20% |
| +25% | 34% | 15% | -8.5% | 17% |
| +30% | 32% | 13% | -8.6% | 16% |
| +35% | 29% | 12% | -8.7% | 14% |
| +45% | 24% | 8% | -9.9% | 11% |
| +60% | 20% | 7% | -9.8% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1346 instappen, mediane hoogste stijging +20.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 33% | -5.5% | 31% |
| +15% | 54% | 27% | -5.6% | 28% |
| +20% | 51% | 24% | -5.8% | 26% |
| +25% | 47% | 21% | -6.0% | 24% |
| +30% | 45% | 20% | -6.2% | 24% |
| +35% | 42% | 17% | -6.4% | 22% |
| +45% | 37% | 13% | -7.2% | 20% |
| +60% | 32% | 11% | -7.1% | 18% |

**filter `alle`** — variant `d45_direct`, 4753 instappen, mediane hoogste stijging +22.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.9% | 30% |
| +15% | 55% | 30% | -6.1% | 28% |
| +20% | 52% | 27% | -6.2% | 27% |
| +25% | 48% | 24% | -6.2% | 26% |
| +30% | 46% | 21% | -6.4% | 25% |
| +35% | 43% | 19% | -6.5% | 24% |
| +45% | 39% | 15% | -6.6% | 23% |
| +60% | 35% | 13% | -6.5% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.1% (317, 15% win) | -9.4% (317, 16% win) | -7.7% (317, 16% win) | -7.0% (317, 16% win) | -10.1% (317, 15% win) | -9.5% (317, 15% win) |
| d35_direct | -9.9% (330, 15% win) | -9.2% (330, 15% win) | -7.5% (330, 16% win) | -6.8% (330, 16% win) | -9.9% (330, 15% win) | -9.3% (330, 15% win) |
| d40_direct | -11.6% (338, 13% win) | -10.9% (338, 13% win) | -9.2% (338, 13% win) | -8.6% (338, 13% win) | -11.7% (338, 12% win) | -11.1% (338, 12% win) |
| d45_direct | -12.9% (351, 10% win) | -12.2% (351, 10% win) | -10.5% (351, 11% win) | -9.9% (351, 11% win) | -13.0% (351, 10% win) | -12.4% (351, 10% win) |
| d50_direct | -12.3% (361, 9% win) | -11.7% (361, 9% win) | -10.0% (361, 9% win) | -9.3% (361, 10% win) | -12.7% (361, 8% win) | -12.1% (361, 9% win) |
| d55_direct | -11.5% (365, 8% win) | -10.8% (365, 8% win) | -9.2% (365, 8% win) | -8.5% (365, 8% win) | -12.0% (365, 7% win) | -11.4% (365, 8% win) |
| d60_direct | -10.1% (353, 8% win) | -9.4% (353, 8% win) | -7.9% (353, 8% win) | -7.2% (353, 8% win) | -11.0% (353, 7% win) | -10.4% (353, 8% win) |
| d65_direct | -10.1% (278, 9% win) | -9.4% (278, 9% win) | -7.9% (278, 9% win) | -7.2% (278, 9% win) | -11.0% (278, 8% win) | -10.4% (278, 9% win) |
| d70_direct | -11.6% (207, 5% win) | -11.0% (207, 5% win) | -9.4% (207, 6% win) | -8.8% (207, 6% win) | -12.6% (207, 4% win) | -11.9% (207, 5% win) |
| d75_direct | -12.0% (144, 5% win) | -11.3% (144, 5% win) | -9.8% (144, 6% win) | -9.2% (144, 6% win) | -13.1% (144, 4% win) | -12.5% (144, 4% win) |
| d80_direct | -10.8% (91, 6% win) | -10.1% (91, 6% win) | -8.7% (91, 6% win) | -8.1% (91, 6% win) | -12.5% (91, 4% win) | -11.9% (91, 4% win) |
| d45_herstel5 | -10.3% (261, 14% win) | -9.6% (261, 14% win) | -8.0% (261, 14% win) | -7.3% (261, 14% win) | -10.4% (261, 14% win) | -9.7% (261, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (1075, 19% win) | -8.9% (1075, 20% win) | -7.1% (1075, 21% win) | -6.5% (1075, 21% win) | -9.2% (1075, 20% win) | -8.6% (1075, 20% win) |
| d35_direct | -9.9% (1176, 19% win) | -9.2% (1176, 19% win) | -7.5% (1176, 20% win) | -6.8% (1176, 20% win) | -9.7% (1176, 19% win) | -9.1% (1176, 20% win) |
| d40_direct | -10.2% (1276, 18% win) | -9.6% (1276, 18% win) | -7.8% (1276, 20% win) | -7.2% (1276, 20% win) | -10.2% (1276, 18% win) | -9.5% (1276, 19% win) |
| d45_direct | -10.2% (1346, 18% win) | -9.5% (1346, 18% win) | -7.9% (1346, 19% win) | -7.2% (1346, 20% win) | -10.3% (1346, 18% win) | -9.7% (1346, 18% win) |
| d50_direct | -9.8% (1437, 18% win) | -9.1% (1437, 18% win) | -7.5% (1437, 20% win) | -6.8% (1437, 20% win) | -10.1% (1437, 18% win) | -9.4% (1437, 18% win) |
| d55_direct | -8.6% (1524, 18% win) | -7.9% (1524, 19% win) | -6.3% (1524, 20% win) | -5.6% (1524, 20% win) | -9.1% (1524, 18% win) | -8.5% (1524, 18% win) |
| d60_direct | -8.1% (1557, 19% win) | -7.4% (1557, 19% win) | -5.9% (1557, 20% win) | -5.2% (1557, 20% win) | -9.0% (1557, 18% win) | -8.3% (1557, 19% win) |
| d65_direct | -7.5% (1417, 20% win) | -6.8% (1417, 21% win) | -5.4% (1417, 22% win) | -4.7% (1417, 22% win) | -8.7% (1417, 20% win) | -8.1% (1417, 20% win) |
| d70_direct | -7.0% (1279, 23% win) | -6.2% (1279, 23% win) | -4.9% (1279, 24% win) | -4.2% (1279, 24% win) | -8.7% (1279, 22% win) | -8.1% (1279, 22% win) |
| d75_direct | -7.9% (1125, 24% win) | -7.2% (1125, 24% win) | -5.9% (1125, 25% win) | -5.3% (1125, 25% win) | -10.3% (1125, 22% win) | -9.7% (1125, 22% win) |
| d80_direct | -7.7% (989, 26% win) | -7.0% (989, 27% win) | -6.0% (989, 27% win) | -5.3% (989, 28% win) | -11.6% (989, 24% win) | -11.0% (989, 24% win) |
| d45_herstel5 | -7.5% (1115, 22% win) | -6.8% (1115, 22% win) | -5.1% (1115, 23% win) | -4.4% (1115, 23% win) | -7.6% (1115, 22% win) | -6.9% (1115, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.4% (5086, 23% win) | -8.7% (5086, 24% win) | -7.1% (5086, 25% win) | -6.4% (5086, 25% win) | -9.6% (5086, 23% win) | -9.0% (5086, 24% win) |
| d35_direct | -9.7% (4981, 22% win) | -9.0% (4981, 23% win) | -7.4% (4981, 24% win) | -6.7% (4981, 24% win) | -10.1% (4981, 22% win) | -9.4% (4981, 22% win) |
| d40_direct | -9.8% (4871, 22% win) | -9.1% (4871, 22% win) | -7.5% (4871, 23% win) | -6.9% (4871, 23% win) | -10.4% (4871, 21% win) | -9.8% (4871, 22% win) |
| d45_direct | -9.5% (4753, 21% win) | -8.8% (4753, 22% win) | -7.3% (4753, 22% win) | -6.6% (4753, 23% win) | -10.3% (4753, 20% win) | -9.7% (4753, 21% win) |
| d50_direct | -9.8% (4652, 20% win) | -9.1% (4652, 21% win) | -7.6% (4652, 22% win) | -6.9% (4652, 22% win) | -10.8% (4652, 20% win) | -10.2% (4652, 20% win) |
| d55_direct | -9.7% (4484, 20% win) | -9.1% (4484, 20% win) | -7.6% (4484, 21% win) | -6.9% (4484, 21% win) | -11.1% (4484, 19% win) | -10.4% (4484, 19% win) |
| d60_direct | -9.1% (4170, 21% win) | -8.4% (4170, 21% win) | -7.1% (4170, 22% win) | -6.4% (4170, 22% win) | -10.8% (4170, 20% win) | -10.2% (4170, 20% win) |
| d65_direct | -9.0% (3726, 22% win) | -8.3% (3726, 22% win) | -7.0% (3726, 23% win) | -6.3% (3726, 24% win) | -11.2% (3726, 20% win) | -10.6% (3726, 21% win) |
| d70_direct | -8.3% (3295, 24% win) | -7.6% (3295, 25% win) | -6.4% (3295, 25% win) | -5.8% (3295, 25% win) | -11.3% (3295, 22% win) | -10.7% (3295, 23% win) |
| d75_direct | -8.8% (2905, 24% win) | -8.1% (2905, 24% win) | -7.1% (2905, 25% win) | -6.5% (2905, 25% win) | -12.8% (2905, 21% win) | -12.2% (2905, 22% win) |
| d80_direct | -8.9% (2528, 26% win) | -8.2% (2528, 27% win) | -7.6% (2528, 27% win) | -6.9% (2528, 27% win) | -14.7% (2528, 22% win) | -14.1% (2528, 22% win) |
| d45_herstel5 | -9.3% (3892, 25% win) | -8.6% (3892, 26% win) | -7.1% (3892, 26% win) | -6.4% (3892, 27% win) | -10.4% (3892, 24% win) | -9.8% (3892, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.6% (4753, 23% win) | -6.3% (4753, 22% win) | -6.8% (4753, 22% win) |
| schoon | -6.4% (3806, 24% win) | -6.3% (3806, 24% win) | -6.7% (3806, 24% win) |
| bundelgrafiek | -7.4% (947, 17% win) | -6.4% (947, 17% win) | -7.3% (947, 15% win) |
| schoon+houders_ok | -7.2% (1346, 20% win) | -6.7% (1346, 19% win) | -6.5% (1346, 20% win) |
| schoon+houders_ok+final_stretch | -8.9% (557, 12% win) | -7.7% (557, 11% win) | -9.8% (557, 14% win) |
| volledige_screening+schoon | -9.9% (351, 11% win) | -8.9% (351, 9% win) | -10.9% (351, 14% win) |
| volledige_screening+schoon+x_link | -10.0% (262, 11% win) | -9.0% (262, 9% win) | -11.1% (262, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.1% (2032, 29% win); 1,3–2x: -8.0% (1774, 18% win); ≥ 2x (bundelgrafiek): -7.4% (947, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.7% (3033, 29% win); 5–20%: -8.7% (839, 13% win); ≥ 20%: -7.9% (881, 10% win)

**top t.o.v. start:** 2–3x: -6.4% (2651, 22% win); 3–6x: -6.6% (1641, 24% win); ≥ 6x: -7.8% (461, 23% win)

**unieke kopers tot de top:** < 30: -5.7% (3037, 29% win); 30–100: -7.5% (955, 11% win); ≥ 100: -9.4% (761, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.6% (1175, 16% win); 1–2: -6.1% (2253, 25% win); ≥ 3 (trap): -6.7% (1325, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.0% (1161, 12% win); 10–25%: -7.4% (755, 12% win); ≥ 25%: -5.5% (2837, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (3759, 25% win); 30 s–3 min: -8.4% (785, 15% win); ≥ 3 min (langzaam): -10.3% (209, 8% win)

**tijd van start tot top:** < 2 min: -6.4% (3922, 24% win); 2–10 min: -7.2% (664, 16% win); ≥ 10 min: -9.6% (167, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
