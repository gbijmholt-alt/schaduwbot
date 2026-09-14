# Videostrategie op alle trades — 2026-09-14 16:29 UTC

Tokens sinds 2026-09-11 08:47 UTC: 66057 geschikt (≥ 2 uur oud, geen herstart), 51638 met trades, 9421 haalden 2x de startkoers, 7223 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2202 tokens. Houdercheck echt uitgevoerd bij 92% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1621, winkans 19%, EV per trade -7.1% (95%-marge -8.6% tot -5.7%), mediaan -10.4%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 5338, winkans 23%, EV -7.0% (95%-marge -8.4% tot -5.5%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 192, winkans 18%, EV -9.4% (95%-marge -12.5% tot -6.3%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 7223 | 40% | 77% | 37% |
| schoon | 5827 | 42% | 77% | 39% |
| bundelgrafiek | 1396 | 31% | 77% | 26% |
| schoon+houders_ok | 1621 | 36% | 80% | 22% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.2% (7723, 25% win) | -6.6% (7551, 24% win) | -6.9% (7392, 23% win) | -6.4% (7223, 23% win) | -6.8% (7070, 22% win) | -6.9% (6802, 21% win) | -6.4% (6327, 22% win) | -6.4% (5626, 23% win) | -5.9% (4978, 25% win) | -6.5% (4409, 25% win) | -7.3% (3842, 27% win) | -6.0% (5925, 27% win) |
| schoon | -6.3% (6223, 26% win) | -6.4% (6098, 25% win) | -6.8% (5971, 24% win) | -6.3% (5827, 24% win) | -6.5% (5703, 24% win) | -6.8% (5475, 23% win) | -6.1% (5054, 24% win) | -5.9% (4487, 25% win) | -5.5% (3997, 27% win) | -6.0% (3551, 27% win) | -7.0% (3141, 29% win) | -6.0% (4972, 27% win) |
| bundelgrafiek | -5.7% (1500, 24% win) | -7.3% (1453, 22% win) | -7.7% (1421, 19% win) | -7.0% (1396, 18% win) | -8.2% (1367, 17% win) | -7.2% (1327, 16% win) | -7.7% (1273, 16% win) | -8.3% (1139, 17% win) | -7.5% (981, 19% win) | -8.5% (858, 18% win) | -8.9% (701, 19% win) | -5.7% (953, 25% win) |
| schoon+houders_ok | -6.6% (1227, 20% win) | -7.1% (1364, 19% win) | -7.4% (1514, 19% win) | -7.1% (1621, 19% win) | -7.1% (1743, 18% win) | -6.1% (1868, 18% win) | -5.4% (1935, 18% win) | -5.1% (1753, 20% win) | -4.5% (1581, 22% win) | -5.1% (1378, 23% win) | -5.4% (1191, 25% win) | -4.1% (1309, 23% win) |
| schoon+houders_ok+final_stretch | -7.1% (531, 16% win) | -7.5% (594, 14% win) | -7.9% (660, 13% win) | -8.1% (707, 12% win) | -8.5% (758, 10% win) | -7.5% (807, 10% win) | -7.0% (808, 9% win) | -6.9% (631, 9% win) | -7.0% (495, 9% win) | -7.0% (347, 8% win) | -5.5% (223, 10% win) | -5.4% (537, 16% win) |
| volledige_screening+schoon | -6.7% (380, 16% win) | -7.2% (410, 15% win) | -8.7% (435, 12% win) | -9.2% (463, 11% win) | -9.6% (489, 9% win) | -8.7% (501, 8% win) | -7.2% (491, 8% win) | -7.6% (381, 8% win) | -8.1% (292, 6% win) | -7.8% (216, 7% win) | -7.5% (138, 5% win) | -7.1% (336, 13% win) |
| volledige_screening+schoon+x_link | -6.9% (293, 17% win) | -6.3% (312, 18% win) | -8.8% (320, 13% win) | -9.3% (329, 11% win) | -9.7% (336, 10% win) | -9.1% (342, 8% win) | -8.1% (339, 7% win) | -8.6% (274, 6% win) | -8.3% (212, 6% win) | -8.1% (160, 6% win) | -7.9% (104, 3% win) | -7.6% (232, 12% win) |

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
| alle | -6.1% (7723, 30% win) | -6.6% (7551, 29% win) | -6.7% (7392, 28% win) | -6.4% (7223, 28% win) | -7.0% (7070, 27% win) | -6.7% (6802, 26% win) | -6.7% (6327, 27% win) | -6.4% (5626, 28% win) | -6.5% (4978, 31% win) | -7.2% (4409, 31% win) | -7.9% (3842, 33% win) |
| schoon | -6.2% (6223, 30% win) | -6.5% (6098, 30% win) | -6.7% (5971, 29% win) | -6.4% (5827, 29% win) | -7.0% (5703, 28% win) | -6.8% (5475, 28% win) | -6.6% (5054, 29% win) | -5.9% (4487, 31% win) | -6.0% (3997, 33% win) | -6.8% (3551, 34% win) | -7.3% (3141, 35% win) |
| bundelgrafiek | -5.7% (1500, 28% win) | -7.2% (1453, 25% win) | -6.9% (1421, 22% win) | -6.4% (1396, 22% win) | -6.7% (1367, 22% win) | -6.1% (1327, 21% win) | -7.1% (1273, 19% win) | -8.4% (1139, 19% win) | -8.5% (981, 21% win) | -8.9% (858, 22% win) | -10.8% (701, 24% win) |
| schoon+houders_ok | -6.5% (1227, 27% win) | -6.8% (1364, 27% win) | -6.8% (1514, 26% win) | -7.2% (1621, 27% win) | -7.5% (1743, 25% win) | -6.2% (1868, 26% win) | -5.7% (1935, 25% win) | -5.7% (1753, 28% win) | -4.9% (1581, 31% win) | -5.3% (1378, 32% win) | -6.9% (1191, 32% win) |
| schoon+houders_ok+final_stretch | -6.8% (531, 25% win) | -7.5% (594, 23% win) | -7.5% (660, 23% win) | -9.3% (707, 21% win) | -10.3% (758, 18% win) | -9.0% (807, 18% win) | -7.5% (808, 19% win) | -8.3% (631, 20% win) | -8.1% (495, 23% win) | -7.5% (347, 24% win) | -7.2% (223, 24% win) |
| volledige_screening+schoon | -6.9% (380, 25% win) | -7.5% (410, 23% win) | -8.5% (435, 23% win) | -10.7% (463, 20% win) | -11.6% (489, 16% win) | -10.2% (501, 17% win) | -8.3% (491, 17% win) | -9.1% (381, 17% win) | -10.4% (292, 18% win) | -9.6% (216, 18% win) | -9.7% (138, 17% win) |
| volledige_screening+schoon+x_link | -7.0% (293, 26% win) | -6.7% (312, 24% win) | -8.6% (320, 22% win) | -11.0% (329, 19% win) | -11.7% (336, 15% win) | -9.8% (342, 17% win) | -8.0% (339, 17% win) | -8.9% (274, 17% win) | -9.5% (212, 18% win) | -9.1% (160, 19% win) | -9.7% (104, 15% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 463 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 24% | -7.9% | 25% |
| +15% | 43% | 20% | -7.9% | 21% |
| +20% | 39% | 17% | -7.9% | 19% |
| +25% | 34% | 15% | -8.2% | 17% |
| +30% | 31% | 13% | -8.3% | 15% |
| +35% | 29% | 12% | -8.2% | 14% |
| +45% | 23% | 8% | -9.2% | 11% |
| +60% | 19% | 7% | -9.2% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1621 instappen, mediane hoogste stijging +18.9%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.9% | 30% |
| +15% | 52% | 26% | -6.0% | 27% |
| +20% | 49% | 23% | -6.0% | 25% |
| +25% | 46% | 20% | -6.2% | 23% |
| +30% | 44% | 19% | -6.3% | 22% |
| +35% | 40% | 16% | -6.5% | 21% |
| +45% | 36% | 13% | -7.1% | 19% |
| +60% | 31% | 10% | -6.9% | 18% |

**filter `alle`** — variant `d45_direct`, 7223 instappen, mediane hoogste stijging +22.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 58% | 34% | -5.9% | 30% |
| +15% | 55% | 30% | -5.9% | 28% |
| +20% | 52% | 26% | -6.0% | 27% |
| +25% | 49% | 23% | -6.1% | 26% |
| +30% | 46% | 21% | -6.2% | 25% |
| +35% | 44% | 19% | -6.3% | 24% |
| +45% | 39% | 16% | -6.4% | 23% |
| +60% | 35% | 13% | -6.4% | 21% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (380, 15% win) | -9.0% (380, 16% win) | -7.3% (380, 16% win) | -6.7% (380, 16% win) | -9.7% (380, 15% win) | -9.0% (380, 15% win) |
| d35_direct | -10.3% (410, 14% win) | -9.6% (410, 14% win) | -7.9% (410, 15% win) | -7.2% (410, 15% win) | -10.3% (410, 14% win) | -9.6% (410, 14% win) |
| d40_direct | -11.7% (435, 12% win) | -11.0% (435, 12% win) | -9.3% (435, 12% win) | -8.7% (435, 12% win) | -11.8% (435, 11% win) | -11.1% (435, 12% win) |
| d45_direct | -12.2% (463, 10% win) | -11.5% (463, 10% win) | -9.8% (463, 11% win) | -9.2% (463, 11% win) | -12.4% (463, 10% win) | -11.7% (463, 10% win) |
| d50_direct | -12.6% (489, 8% win) | -11.9% (489, 8% win) | -10.2% (489, 9% win) | -9.6% (489, 9% win) | -12.9% (489, 8% win) | -12.3% (489, 8% win) |
| d55_direct | -11.6% (501, 8% win) | -10.9% (501, 8% win) | -9.3% (501, 8% win) | -8.7% (501, 8% win) | -12.2% (501, 7% win) | -11.6% (501, 8% win) |
| d60_direct | -10.1% (491, 8% win) | -9.4% (491, 8% win) | -7.9% (491, 8% win) | -7.2% (491, 8% win) | -11.0% (491, 7% win) | -10.4% (491, 8% win) |
| d65_direct | -10.5% (381, 8% win) | -9.8% (381, 8% win) | -8.3% (381, 8% win) | -7.6% (381, 8% win) | -11.4% (381, 7% win) | -10.8% (381, 8% win) |
| d70_direct | -11.0% (292, 6% win) | -10.3% (292, 6% win) | -8.8% (292, 6% win) | -8.1% (292, 6% win) | -11.9% (292, 5% win) | -11.3% (292, 6% win) |
| d75_direct | -10.7% (216, 6% win) | -10.0% (216, 6% win) | -8.5% (216, 7% win) | -7.8% (216, 7% win) | -11.8% (216, 6% win) | -11.2% (216, 6% win) |
| d80_direct | -10.3% (138, 5% win) | -9.6% (138, 5% win) | -8.2% (138, 5% win) | -7.5% (138, 5% win) | -11.8% (138, 4% win) | -11.2% (138, 4% win) |
| d45_herstel5 | -10.2% (336, 13% win) | -9.5% (336, 13% win) | -7.8% (336, 13% win) | -7.1% (336, 13% win) | -10.2% (336, 13% win) | -9.6% (336, 13% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.8% (1227, 19% win) | -9.1% (1227, 19% win) | -7.3% (1227, 20% win) | -6.6% (1227, 20% win) | -9.4% (1227, 19% win) | -8.8% (1227, 19% win) |
| d35_direct | -10.2% (1364, 18% win) | -9.6% (1364, 18% win) | -7.8% (1364, 19% win) | -7.1% (1364, 19% win) | -10.0% (1364, 18% win) | -9.4% (1364, 19% win) |
| d40_direct | -10.4% (1514, 17% win) | -9.8% (1514, 18% win) | -8.1% (1514, 18% win) | -7.4% (1514, 19% win) | -10.4% (1514, 17% win) | -9.7% (1514, 18% win) |
| d45_direct | -10.2% (1621, 17% win) | -9.5% (1621, 17% win) | -7.8% (1621, 18% win) | -7.1% (1621, 19% win) | -10.3% (1621, 17% win) | -9.6% (1621, 17% win) |
| d50_direct | -10.1% (1743, 17% win) | -9.4% (1743, 17% win) | -7.8% (1743, 18% win) | -7.1% (1743, 18% win) | -10.4% (1743, 17% win) | -9.7% (1743, 17% win) |
| d55_direct | -9.0% (1868, 17% win) | -8.3% (1868, 17% win) | -6.8% (1868, 18% win) | -6.1% (1868, 18% win) | -9.6% (1868, 16% win) | -8.9% (1868, 17% win) |
| d60_direct | -8.3% (1935, 17% win) | -7.6% (1935, 18% win) | -6.1% (1935, 18% win) | -5.4% (1935, 18% win) | -9.2% (1935, 17% win) | -8.5% (1935, 17% win) |
| d65_direct | -8.0% (1753, 18% win) | -7.3% (1753, 19% win) | -5.8% (1753, 19% win) | -5.1% (1753, 20% win) | -9.0% (1753, 18% win) | -8.4% (1753, 18% win) |
| d70_direct | -7.3% (1581, 21% win) | -6.6% (1581, 21% win) | -5.2% (1581, 22% win) | -4.5% (1581, 22% win) | -8.9% (1581, 20% win) | -8.2% (1581, 20% win) |
| d75_direct | -7.8% (1378, 22% win) | -7.1% (1378, 22% win) | -5.8% (1378, 23% win) | -5.1% (1378, 23% win) | -10.0% (1378, 20% win) | -9.4% (1378, 21% win) |
| d80_direct | -7.8% (1191, 24% win) | -7.2% (1191, 24% win) | -6.1% (1191, 25% win) | -5.4% (1191, 25% win) | -11.3% (1191, 22% win) | -10.7% (1191, 22% win) |
| d45_herstel5 | -7.1% (1309, 22% win) | -6.4% (1309, 22% win) | -4.8% (1309, 23% win) | -4.1% (1309, 23% win) | -7.2% (1309, 22% win) | -6.5% (1309, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.2% (7723, 24% win) | -8.5% (7723, 24% win) | -6.9% (7723, 25% win) | -6.2% (7723, 25% win) | -9.4% (7723, 24% win) | -8.8% (7723, 24% win) |
| d35_direct | -9.5% (7551, 23% win) | -8.8% (7551, 23% win) | -7.2% (7551, 24% win) | -6.6% (7551, 24% win) | -9.9% (7551, 22% win) | -9.3% (7551, 23% win) |
| d40_direct | -9.9% (7392, 21% win) | -9.2% (7392, 22% win) | -7.6% (7392, 23% win) | -6.9% (7392, 23% win) | -10.5% (7392, 21% win) | -9.8% (7392, 21% win) |
| d45_direct | -9.3% (7223, 21% win) | -8.6% (7223, 22% win) | -7.1% (7223, 22% win) | -6.4% (7223, 23% win) | -10.2% (7223, 20% win) | -9.5% (7223, 21% win) |
| d50_direct | -9.6% (7070, 21% win) | -8.9% (7070, 21% win) | -7.4% (7070, 22% win) | -6.8% (7070, 22% win) | -10.7% (7070, 20% win) | -10.1% (7070, 20% win) |
| d55_direct | -9.7% (6802, 20% win) | -9.0% (6802, 20% win) | -7.6% (6802, 21% win) | -6.9% (6802, 21% win) | -11.1% (6802, 19% win) | -10.4% (6802, 19% win) |
| d60_direct | -9.2% (6327, 20% win) | -8.5% (6327, 21% win) | -7.1% (6327, 22% win) | -6.4% (6327, 22% win) | -10.9% (6327, 19% win) | -10.3% (6327, 20% win) |
| d65_direct | -9.0% (5626, 22% win) | -8.3% (5626, 22% win) | -7.0% (5626, 23% win) | -6.4% (5626, 23% win) | -11.2% (5626, 20% win) | -10.6% (5626, 21% win) |
| d70_direct | -8.4% (4978, 24% win) | -7.7% (4978, 24% win) | -6.6% (4978, 25% win) | -5.9% (4978, 25% win) | -11.4% (4978, 22% win) | -10.8% (4978, 22% win) |
| d75_direct | -8.8% (4409, 24% win) | -8.1% (4409, 24% win) | -7.2% (4409, 25% win) | -6.5% (4409, 25% win) | -12.8% (4409, 21% win) | -12.2% (4409, 22% win) |
| d80_direct | -9.3% (3842, 26% win) | -8.6% (3842, 27% win) | -8.0% (3842, 27% win) | -7.3% (3842, 27% win) | -14.9% (3842, 22% win) | -14.4% (3842, 22% win) |
| d45_herstel5 | -8.8% (5925, 25% win) | -8.2% (5925, 25% win) | -6.7% (5925, 26% win) | -6.0% (5925, 27% win) | -9.9% (5925, 24% win) | -9.3% (5925, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.4% (7223, 23% win) | -6.1% (7223, 22% win) | -6.9% (7223, 22% win) |
| schoon | -6.3% (5827, 24% win) | -6.0% (5827, 24% win) | -6.6% (5827, 23% win) |
| bundelgrafiek | -7.0% (1396, 18% win) | -6.4% (1396, 18% win) | -8.0% (1396, 16% win) |
| schoon+houders_ok | -7.1% (1621, 19% win) | -6.7% (1621, 18% win) | -7.1% (1621, 19% win) |
| schoon+houders_ok+final_stretch | -8.1% (707, 12% win) | -7.2% (707, 11% win) | -10.1% (707, 14% win) |
| volledige_screening+schoon | -9.2% (463, 11% win) | -8.6% (463, 8% win) | -12.1% (463, 13% win) |
| volledige_screening+schoon+x_link | -9.3% (329, 11% win) | -8.6% (329, 8% win) | -12.0% (329, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (3092, 28% win); 1,3–2x: -7.0% (2734, 19% win); ≥ 2x (bundelgrafiek): -7.0% (1397, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.5% (4552, 29% win); 5–20%: -8.4% (1230, 13% win); ≥ 20%: -7.9% (1441, 11% win)

**top t.o.v. start:** 2–3x: -6.3% (4081, 22% win); 3–6x: -6.5% (2453, 24% win); ≥ 6x: -7.4% (689, 24% win)

**unieke kopers tot de top:** < 30: -5.5% (4556, 29% win); 30–100: -7.1% (1513, 12% win); ≥ 100: -9.0% (1154, 13% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.5% (1717, 16% win); 1–2: -6.3% (3492, 24% win); ≥ 3 (trap): -6.6% (2014, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.5% (1781, 13% win); 10–25%: -8.0% (1167, 12% win); ≥ 25%: -5.1% (4275, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.7% (5661, 26% win); 30 s–3 min: -8.8% (1246, 14% win); ≥ 3 min (langzaam): -9.7% (316, 8% win)

**tijd van start tot top:** < 2 min: -6.0% (5912, 24% win); 2–10 min: -7.9% (1050, 16% win); ≥ 10 min: -11.2% (261, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
