# Videostrategie op alle trades — 2026-09-14 14:22 UTC

Tokens sinds 2026-09-11 08:47 UTC: 63789 geschikt (≥ 2 uur oud, geen herstart), 49915 met trades, 8998 haalden 2x de startkoers, 6867 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2109 tokens. Houdercheck echt uitgevoerd bij 92% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1596, winkans 19%, EV per trade -7.1% (95%-marge -8.6% tot -5.6%), mediaan -10.4%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 5049, winkans 23%, EV -6.7% (95%-marge -8.2% tot -5.1%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 179, winkans 19%, EV -8.8% (95%-marge -11.9% tot -5.7%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 6867 | 40% | 77% | 37% |
| schoon | 5538 | 43% | 76% | 40% |
| bundelgrafiek | 1329 | 31% | 77% | 26% |
| schoon+houders_ok | 1596 | 36% | 80% | 22% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.1% (7347, 26% win) | -6.4% (7186, 24% win) | -6.8% (7030, 23% win) | -6.3% (6867, 23% win) | -6.7% (6717, 22% win) | -6.8% (6478, 22% win) | -6.3% (6024, 22% win) | -6.4% (5377, 24% win) | -5.8% (4763, 25% win) | -6.5% (4215, 25% win) | -7.1% (3669, 28% win) | -5.8% (5688, 27% win) |
| schoon | -6.3% (5917, 26% win) | -6.2% (5802, 25% win) | -6.6% (5678, 24% win) | -6.2% (5538, 24% win) | -6.4% (5417, 24% win) | -6.7% (5216, 23% win) | -6.0% (4812, 24% win) | -5.9% (4286, 25% win) | -5.4% (3824, 27% win) | -6.0% (3396, 27% win) | -6.8% (3002, 29% win) | -5.8% (4773, 27% win) |
| bundelgrafiek | -5.4% (1430, 25% win) | -7.0% (1384, 22% win) | -7.5% (1352, 20% win) | -6.8% (1329, 19% win) | -8.2% (1300, 17% win) | -7.1% (1262, 16% win) | -7.6% (1212, 17% win) | -8.3% (1091, 17% win) | -7.4% (939, 19% win) | -8.6% (819, 18% win) | -8.8% (667, 20% win) | -5.8% (915, 25% win) |
| schoon+houders_ok | -6.6% (1212, 20% win) | -7.1% (1344, 20% win) | -7.3% (1491, 19% win) | -7.1% (1596, 19% win) | -7.0% (1716, 19% win) | -6.0% (1837, 19% win) | -5.4% (1901, 19% win) | -5.1% (1729, 20% win) | -4.5% (1555, 22% win) | -5.2% (1355, 23% win) | -5.5% (1173, 25% win) | -4.0% (1294, 23% win) |
| schoon+houders_ok+final_stretch | -7.1% (525, 16% win) | -7.4% (584, 15% win) | -7.8% (649, 13% win) | -8.1% (695, 12% win) | -8.4% (745, 10% win) | -7.4% (790, 10% win) | -7.0% (789, 9% win) | -7.0% (620, 9% win) | -6.9% (483, 10% win) | -6.9% (335, 9% win) | -5.4% (216, 11% win) | -5.5% (529, 16% win) |
| volledige_screening+schoon | -6.7% (375, 16% win) | -7.0% (404, 15% win) | -8.5% (428, 13% win) | -9.0% (455, 11% win) | -9.4% (480, 9% win) | -8.5% (488, 8% win) | -7.3% (477, 8% win) | -7.6% (373, 8% win) | -8.1% (284, 6% win) | -7.8% (208, 7% win) | -7.5% (133, 5% win) | -7.0% (331, 14% win) |
| volledige_screening+schoon+x_link | -7.0% (288, 17% win) | -6.0% (306, 18% win) | -8.5% (314, 14% win) | -9.1% (323, 12% win) | -9.4% (330, 9% win) | -8.9% (333, 8% win) | -8.3% (328, 7% win) | -8.6% (267, 6% win) | -8.2% (205, 6% win) | -8.0% (153, 6% win) | -7.8% (100, 3% win) | -7.5% (229, 13% win) |

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
| alle | -6.0% (7347, 30% win) | -6.5% (7186, 29% win) | -6.7% (7030, 28% win) | -6.3% (6867, 28% win) | -7.0% (6717, 27% win) | -6.6% (6478, 27% win) | -6.7% (6024, 27% win) | -6.5% (5377, 28% win) | -6.3% (4763, 31% win) | -7.1% (4215, 32% win) | -7.7% (3669, 33% win) |
| schoon | -6.1% (5917, 31% win) | -6.4% (5802, 30% win) | -6.6% (5678, 29% win) | -6.3% (5538, 29% win) | -7.0% (5417, 28% win) | -6.7% (5216, 28% win) | -6.6% (4812, 29% win) | -6.0% (4286, 31% win) | -5.8% (3824, 33% win) | -6.6% (3396, 34% win) | -7.1% (3002, 35% win) |
| bundelgrafiek | -5.7% (1430, 28% win) | -7.2% (1384, 25% win) | -6.9% (1352, 23% win) | -6.3% (1329, 22% win) | -6.8% (1300, 22% win) | -6.2% (1262, 21% win) | -7.1% (1212, 20% win) | -8.4% (1091, 19% win) | -8.4% (939, 22% win) | -9.0% (819, 23% win) | -10.4% (667, 24% win) |
| schoon+houders_ok | -6.6% (1212, 27% win) | -6.8% (1344, 27% win) | -6.7% (1491, 27% win) | -7.1% (1596, 27% win) | -7.4% (1716, 26% win) | -6.1% (1837, 26% win) | -5.8% (1901, 25% win) | -5.7% (1729, 28% win) | -4.8% (1555, 31% win) | -5.3% (1355, 32% win) | -6.9% (1173, 33% win) |
| schoon+houders_ok+final_stretch | -6.8% (525, 25% win) | -7.5% (584, 24% win) | -7.4% (649, 23% win) | -9.2% (695, 21% win) | -10.1% (745, 18% win) | -8.9% (790, 18% win) | -7.7% (789, 19% win) | -8.3% (620, 20% win) | -8.0% (483, 23% win) | -7.5% (335, 25% win) | -6.9% (216, 24% win) |
| volledige_screening+schoon | -7.0% (375, 25% win) | -7.5% (404, 23% win) | -8.3% (428, 24% win) | -10.4% (455, 20% win) | -11.3% (480, 16% win) | -10.0% (488, 18% win) | -8.4% (477, 17% win) | -9.0% (373, 18% win) | -10.5% (284, 18% win) | -9.7% (208, 19% win) | -9.5% (133, 17% win) |
| volledige_screening+schoon+x_link | -7.1% (288, 25% win) | -6.7% (306, 24% win) | -8.5% (314, 23% win) | -10.9% (323, 19% win) | -11.5% (330, 15% win) | -9.6% (333, 17% win) | -8.1% (328, 17% win) | -8.8% (267, 17% win) | -9.6% (205, 18% win) | -9.3% (153, 19% win) | -9.4% (100, 16% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 455 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 24% | -7.8% | 25% |
| +15% | 43% | 20% | -7.8% | 22% |
| +20% | 39% | 17% | -7.6% | 19% |
| +25% | 34% | 15% | -7.9% | 17% |
| +30% | 31% | 13% | -8.1% | 16% |
| +35% | 29% | 12% | -8.0% | 15% |
| +45% | 23% | 9% | -9.0% | 11% |
| +60% | 19% | 7% | -8.9% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1596 instappen, mediane hoogste stijging +19.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.8% | 30% |
| +15% | 53% | 26% | -5.9% | 27% |
| +20% | 50% | 23% | -5.9% | 25% |
| +25% | 46% | 20% | -6.1% | 23% |
| +30% | 44% | 19% | -6.2% | 23% |
| +35% | 41% | 16% | -6.4% | 21% |
| +45% | 36% | 13% | -7.1% | 19% |
| +60% | 31% | 10% | -6.9% | 18% |

**filter `alle`** — variant `d45_direct`, 6867 instappen, mediane hoogste stijging +23.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.8% | 30% |
| +15% | 56% | 30% | -5.8% | 28% |
| +20% | 52% | 26% | -5.9% | 27% |
| +25% | 49% | 24% | -6.0% | 26% |
| +30% | 46% | 21% | -6.1% | 25% |
| +35% | 44% | 19% | -6.2% | 24% |
| +45% | 40% | 16% | -6.3% | 23% |
| +60% | 35% | 13% | -6.2% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (375, 15% win) | -9.0% (375, 16% win) | -7.3% (375, 16% win) | -6.7% (375, 16% win) | -9.7% (375, 15% win) | -9.1% (375, 15% win) |
| d35_direct | -10.1% (404, 15% win) | -9.4% (404, 15% win) | -7.7% (404, 15% win) | -7.0% (404, 15% win) | -10.1% (404, 15% win) | -9.4% (404, 15% win) |
| d40_direct | -11.5% (428, 12% win) | -10.8% (428, 12% win) | -9.1% (428, 13% win) | -8.5% (428, 13% win) | -11.6% (428, 11% win) | -10.9% (428, 12% win) |
| d45_direct | -12.0% (455, 10% win) | -11.3% (455, 10% win) | -9.7% (455, 11% win) | -9.0% (455, 11% win) | -12.2% (455, 10% win) | -11.6% (455, 10% win) |
| d50_direct | -12.3% (480, 8% win) | -11.7% (480, 8% win) | -10.1% (480, 8% win) | -9.4% (480, 9% win) | -12.8% (480, 8% win) | -12.1% (480, 8% win) |
| d55_direct | -11.4% (488, 8% win) | -10.7% (488, 8% win) | -9.1% (488, 8% win) | -8.5% (488, 8% win) | -12.0% (488, 7% win) | -11.4% (488, 8% win) |
| d60_direct | -10.2% (477, 8% win) | -9.5% (477, 8% win) | -8.0% (477, 8% win) | -7.3% (477, 8% win) | -11.1% (477, 7% win) | -10.4% (477, 8% win) |
| d65_direct | -10.5% (373, 8% win) | -9.8% (373, 8% win) | -8.3% (373, 8% win) | -7.6% (373, 8% win) | -11.4% (373, 7% win) | -10.8% (373, 8% win) |
| d70_direct | -10.9% (284, 6% win) | -10.3% (284, 6% win) | -8.7% (284, 6% win) | -8.1% (284, 6% win) | -11.9% (284, 5% win) | -11.2% (284, 6% win) |
| d75_direct | -10.7% (208, 6% win) | -10.0% (208, 6% win) | -8.5% (208, 7% win) | -7.8% (208, 7% win) | -11.8% (208, 6% win) | -11.1% (208, 6% win) |
| d80_direct | -10.2% (133, 5% win) | -9.6% (133, 5% win) | -8.1% (133, 5% win) | -7.5% (133, 5% win) | -11.8% (133, 4% win) | -11.1% (133, 4% win) |
| d45_herstel5 | -10.1% (331, 14% win) | -9.4% (331, 14% win) | -7.7% (331, 14% win) | -7.0% (331, 14% win) | -10.1% (331, 14% win) | -9.5% (331, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (1212, 19% win) | -9.0% (1212, 19% win) | -7.2% (1212, 20% win) | -6.6% (1212, 20% win) | -9.3% (1212, 19% win) | -8.7% (1212, 20% win) |
| d35_direct | -10.2% (1344, 18% win) | -9.5% (1344, 18% win) | -7.8% (1344, 20% win) | -7.1% (1344, 20% win) | -10.0% (1344, 18% win) | -9.3% (1344, 19% win) |
| d40_direct | -10.3% (1491, 17% win) | -9.7% (1491, 18% win) | -8.0% (1491, 19% win) | -7.3% (1491, 19% win) | -10.3% (1491, 17% win) | -9.6% (1491, 18% win) |
| d45_direct | -10.1% (1596, 17% win) | -9.4% (1596, 17% win) | -7.8% (1596, 18% win) | -7.1% (1596, 19% win) | -10.2% (1596, 17% win) | -9.6% (1596, 18% win) |
| d50_direct | -10.0% (1716, 17% win) | -9.3% (1716, 17% win) | -7.7% (1716, 18% win) | -7.0% (1716, 19% win) | -10.3% (1716, 17% win) | -9.6% (1716, 17% win) |
| d55_direct | -8.9% (1837, 17% win) | -8.2% (1837, 17% win) | -6.6% (1837, 18% win) | -6.0% (1837, 19% win) | -9.5% (1837, 17% win) | -8.8% (1837, 17% win) |
| d60_direct | -8.3% (1901, 17% win) | -7.6% (1901, 18% win) | -6.1% (1901, 18% win) | -5.4% (1901, 19% win) | -9.2% (1901, 17% win) | -8.5% (1901, 17% win) |
| d65_direct | -8.0% (1729, 18% win) | -7.3% (1729, 19% win) | -5.8% (1729, 20% win) | -5.1% (1729, 20% win) | -9.1% (1729, 18% win) | -8.4% (1729, 19% win) |
| d70_direct | -7.3% (1555, 21% win) | -6.6% (1555, 22% win) | -5.2% (1555, 22% win) | -4.5% (1555, 22% win) | -8.9% (1555, 20% win) | -8.3% (1555, 21% win) |
| d75_direct | -7.9% (1355, 22% win) | -7.2% (1355, 22% win) | -5.9% (1355, 23% win) | -5.2% (1355, 23% win) | -10.1% (1355, 21% win) | -9.5% (1355, 21% win) |
| d80_direct | -8.0% (1173, 24% win) | -7.3% (1173, 25% win) | -6.2% (1173, 25% win) | -5.5% (1173, 25% win) | -11.5% (1173, 22% win) | -10.9% (1173, 22% win) |
| d45_herstel5 | -7.0% (1294, 22% win) | -6.3% (1294, 22% win) | -4.7% (1294, 23% win) | -4.0% (1294, 23% win) | -7.1% (1294, 22% win) | -6.5% (1294, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.1% (7347, 24% win) | -8.5% (7347, 24% win) | -6.8% (7347, 25% win) | -6.1% (7347, 26% win) | -9.4% (7347, 24% win) | -8.7% (7347, 24% win) |
| d35_direct | -9.4% (7186, 23% win) | -8.7% (7186, 23% win) | -7.1% (7186, 24% win) | -6.4% (7186, 24% win) | -9.8% (7186, 22% win) | -9.1% (7186, 23% win) |
| d40_direct | -9.8% (7030, 22% win) | -9.1% (7030, 22% win) | -7.5% (7030, 23% win) | -6.8% (7030, 23% win) | -10.3% (7030, 21% win) | -9.7% (7030, 22% win) |
| d45_direct | -9.2% (6867, 21% win) | -8.6% (6867, 22% win) | -7.0% (6867, 23% win) | -6.3% (6867, 23% win) | -10.1% (6867, 21% win) | -9.4% (6867, 21% win) |
| d50_direct | -9.6% (6717, 21% win) | -8.9% (6717, 21% win) | -7.4% (6717, 22% win) | -6.7% (6717, 22% win) | -10.6% (6717, 20% win) | -10.0% (6717, 20% win) |
| d55_direct | -9.6% (6478, 20% win) | -8.9% (6478, 20% win) | -7.4% (6478, 21% win) | -6.8% (6478, 22% win) | -10.9% (6478, 19% win) | -10.3% (6478, 19% win) |
| d60_direct | -9.0% (6024, 21% win) | -8.4% (6024, 21% win) | -7.0% (6024, 22% win) | -6.3% (6024, 22% win) | -10.8% (6024, 19% win) | -10.2% (6024, 20% win) |
| d65_direct | -9.0% (5377, 22% win) | -8.3% (5377, 22% win) | -7.0% (5377, 23% win) | -6.4% (5377, 24% win) | -11.2% (5377, 20% win) | -10.6% (5377, 21% win) |
| d70_direct | -8.3% (4763, 24% win) | -7.6% (4763, 24% win) | -6.5% (4763, 25% win) | -5.8% (4763, 25% win) | -11.3% (4763, 22% win) | -10.7% (4763, 22% win) |
| d75_direct | -8.8% (4215, 24% win) | -8.1% (4215, 24% win) | -7.1% (4215, 25% win) | -6.5% (4215, 25% win) | -12.7% (4215, 21% win) | -12.1% (4215, 22% win) |
| d80_direct | -9.1% (3669, 26% win) | -8.4% (3669, 27% win) | -7.8% (3669, 27% win) | -7.1% (3669, 28% win) | -14.8% (3669, 22% win) | -14.2% (3669, 23% win) |
| d45_herstel5 | -8.6% (5688, 25% win) | -7.9% (5688, 26% win) | -6.5% (5688, 26% win) | -5.8% (5688, 27% win) | -9.7% (5688, 24% win) | -9.1% (5688, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.3% (6867, 23% win) | -6.0% (6867, 23% win) | -6.6% (6867, 22% win) |
| schoon | -6.2% (5538, 24% win) | -6.0% (5538, 24% win) | -6.3% (5538, 23% win) |
| bundelgrafiek | -6.8% (1329, 19% win) | -6.1% (1329, 18% win) | -7.7% (1329, 16% win) |
| schoon+houders_ok | -7.1% (1596, 19% win) | -6.7% (1596, 18% win) | -6.9% (1596, 20% win) |
| schoon+houders_ok+final_stretch | -8.1% (695, 12% win) | -7.2% (695, 10% win) | -9.9% (695, 14% win) |
| volledige_screening+schoon | -9.0% (455, 11% win) | -8.4% (455, 8% win) | -11.8% (455, 13% win) |
| volledige_screening+schoon+x_link | -9.1% (323, 12% win) | -8.3% (323, 9% win) | -11.7% (323, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.5% (2969, 28% win); 1,3–2x: -7.0% (2568, 19% win); ≥ 2x (bundelgrafiek): -6.8% (1330, 19% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.4% (4375, 29% win); 5–20%: -8.2% (1154, 13% win); ≥ 20%: -7.6% (1338, 12% win)

**top t.o.v. start:** 2–3x: -6.2% (3868, 22% win); 3–6x: -6.2% (2347, 24% win); ≥ 6x: -7.3% (652, 25% win)

**unieke kopers tot de top:** < 30: -5.5% (4363, 29% win); 30–100: -7.1% (1430, 12% win); ≥ 100: -8.8% (1074, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.4% (1607, 17% win); 1–2: -6.2% (3325, 24% win); ≥ 3 (trap): -6.5% (1935, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.3% (1679, 13% win); 10–25%: -7.7% (1093, 12% win); ≥ 25%: -5.1% (4095, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.6% (5383, 26% win); 30 s–3 min: -8.6% (1183, 14% win); ≥ 3 min (langzaam): -9.5% (301, 8% win)

**tijd van start tot top:** < 2 min: -5.9% (5630, 25% win); 2–10 min: -7.5% (994, 16% win); ≥ 10 min: -10.9% (243, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
