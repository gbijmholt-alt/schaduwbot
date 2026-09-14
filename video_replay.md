# Videostrategie op alle trades — 2026-09-14 05:20 UTC

Tokens sinds 2026-09-11 08:47 UTC: 56770 geschikt (≥ 2 uur oud, geen herstart), 44305 met trades, 7965 haalden 2x de startkoers, 6105 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1873 tokens. Houdercheck echt uitgevoerd bij 92% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1485, winkans 19%, EV per trade -7.2% (95%-marge -8.8% tot -5.6%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 4409, winkans 23%, EV -6.7% (95%-marge -8.4% tot -5.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 131, winkans 17%, EV -9.9% (95%-marge -13.5% tot -6.3%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 6105 | 40% | 77% | 37% |
| schoon | 4898 | 42% | 77% | 40% |
| bundelgrafiek | 1207 | 31% | 77% | 25% |
| schoon+houders_ok | 1485 | 36% | 80% | 23% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.3% (6532, 25% win) | -6.4% (6391, 24% win) | -6.8% (6252, 23% win) | -6.4% (6105, 23% win) | -6.9% (5973, 22% win) | -6.8% (5761, 22% win) | -6.2% (5351, 22% win) | -6.2% (4778, 24% win) | -5.6% (4223, 25% win) | -6.2% (3727, 25% win) | -6.8% (3233, 28% win) | -5.9% (5025, 27% win) |
| schoon | -6.3% (5232, 25% win) | -6.2% (5133, 25% win) | -6.6% (5024, 24% win) | -6.2% (4898, 24% win) | -6.4% (4792, 24% win) | -6.5% (4614, 23% win) | -5.8% (4252, 24% win) | -5.5% (3787, 26% win) | -5.1% (3374, 27% win) | -5.7% (2990, 27% win) | -6.5% (2638, 29% win) | -5.7% (4206, 27% win) |
| bundelgrafiek | -6.0% (1300, 24% win) | -7.3% (1258, 22% win) | -7.6% (1228, 19% win) | -7.2% (1207, 18% win) | -9.1% (1181, 16% win) | -7.8% (1147, 15% win) | -7.9% (1099, 16% win) | -8.6% (991, 16% win) | -7.7% (849, 18% win) | -8.3% (737, 18% win) | -7.8% (595, 20% win) | -6.9% (819, 24% win) |
| schoon+houders_ok | -6.5% (1147, 20% win) | -7.1% (1265, 20% win) | -7.4% (1394, 19% win) | -7.2% (1485, 19% win) | -7.0% (1590, 19% win) | -5.8% (1699, 19% win) | -5.2% (1753, 19% win) | -5.0% (1602, 21% win) | -4.5% (1448, 23% win) | -5.0% (1268, 24% win) | -5.5% (1104, 26% win) | -4.1% (1211, 23% win) |
| schoon+houders_ok+final_stretch | -7.2% (489, 16% win) | -7.4% (542, 14% win) | -8.1% (598, 12% win) | -8.6% (635, 12% win) | -8.5% (676, 10% win) | -7.4% (712, 10% win) | -7.0% (710, 10% win) | -6.7% (560, 10% win) | -7.0% (433, 9% win) | -6.9% (297, 9% win) | -5.1% (189, 12% win) | -5.7% (488, 15% win) |
| volledige_screening+schoon | -7.0% (344, 16% win) | -7.0% (368, 15% win) | -8.4% (390, 13% win) | -9.4% (414, 11% win) | -9.2% (434, 9% win) | -8.5% (440, 8% win) | -7.2% (428, 8% win) | -7.2% (337, 9% win) | -8.1% (254, 6% win) | -8.0% (182, 7% win) | -7.6% (114, 5% win) | -7.3% (302, 14% win) |
| volledige_screening+schoon+x_link | -7.4% (262, 17% win) | -6.0% (278, 18% win) | -8.2% (287, 15% win) | -9.3% (295, 12% win) | -9.2% (299, 10% win) | -8.8% (301, 9% win) | -8.2% (293, 8% win) | -8.3% (239, 7% win) | -8.0% (181, 6% win) | -8.3% (132, 6% win) | -8.1% (84, 2% win) | -7.2% (212, 14% win) |

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
| alle | -6.2% (6532, 30% win) | -6.5% (6391, 29% win) | -6.6% (6252, 28% win) | -6.4% (6105, 28% win) | -7.2% (5973, 26% win) | -6.7% (5761, 26% win) | -6.6% (5351, 27% win) | -6.3% (4778, 28% win) | -6.4% (4223, 31% win) | -6.5% (3727, 32% win) | -7.1% (3233, 33% win) |
| schoon | -6.3% (5232, 30% win) | -6.3% (5133, 30% win) | -6.6% (5024, 29% win) | -6.4% (4898, 29% win) | -7.1% (4792, 28% win) | -6.7% (4614, 28% win) | -6.4% (4252, 29% win) | -5.7% (3787, 31% win) | -5.8% (3374, 33% win) | -6.0% (2990, 34% win) | -6.6% (2638, 35% win) |
| bundelgrafiek | -5.9% (1300, 28% win) | -7.0% (1258, 25% win) | -6.6% (1228, 23% win) | -6.5% (1207, 22% win) | -7.7% (1181, 21% win) | -6.7% (1147, 20% win) | -7.2% (1099, 19% win) | -8.5% (991, 18% win) | -8.8% (849, 21% win) | -8.8% (737, 23% win) | -9.2% (595, 24% win) |
| schoon+houders_ok | -6.6% (1147, 27% win) | -6.8% (1265, 27% win) | -6.6% (1394, 27% win) | -7.1% (1485, 27% win) | -7.4% (1590, 26% win) | -6.1% (1699, 26% win) | -5.6% (1753, 26% win) | -5.3% (1602, 29% win) | -4.6% (1448, 32% win) | -4.8% (1268, 33% win) | -6.7% (1104, 33% win) |
| schoon+houders_ok+final_stretch | -7.1% (489, 24% win) | -7.4% (542, 24% win) | -7.4% (598, 23% win) | -9.2% (635, 21% win) | -10.3% (676, 18% win) | -9.1% (712, 18% win) | -7.4% (710, 20% win) | -7.5% (560, 21% win) | -7.7% (433, 24% win) | -7.1% (297, 26% win) | -5.9% (189, 26% win) |
| volledige_screening+schoon | -7.2% (344, 25% win) | -7.4% (368, 23% win) | -8.0% (390, 24% win) | -10.5% (414, 20% win) | -11.4% (434, 16% win) | -10.5% (440, 17% win) | -8.1% (428, 18% win) | -8.2% (337, 19% win) | -10.0% (254, 19% win) | -9.4% (182, 20% win) | -8.8% (114, 18% win) |
| volledige_screening+schoon+x_link | -7.1% (262, 25% win) | -6.6% (278, 24% win) | -7.9% (287, 24% win) | -10.8% (295, 19% win) | -11.7% (299, 15% win) | -10.2% (301, 16% win) | -7.9% (293, 18% win) | -8.1% (239, 18% win) | -9.0% (181, 20% win) | -9.2% (132, 20% win) | -8.8% (84, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 414 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -7.9% | 25% |
| +15% | 42% | 20% | -8.0% | 21% |
| +20% | 39% | 17% | -7.9% | 19% |
| +25% | 34% | 14% | -8.3% | 17% |
| +30% | 31% | 13% | -8.4% | 15% |
| +35% | 29% | 12% | -8.4% | 14% |
| +45% | 24% | 8% | -9.4% | 11% |
| +60% | 20% | 6% | -9.3% | 9% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1485 instappen, mediane hoogste stijging +20.0%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 58% | 32% | -5.8% | 30% |
| +15% | 53% | 26% | -5.9% | 27% |
| +20% | 50% | 23% | -6.0% | 25% |
| +25% | 47% | 20% | -6.2% | 24% |
| +30% | 44% | 19% | -6.3% | 23% |
| +35% | 41% | 16% | -6.5% | 21% |
| +45% | 36% | 13% | -7.2% | 19% |
| +60% | 31% | 10% | -7.1% | 18% |

**filter `alle`** — variant `d45_direct`, 6105 instappen, mediane hoogste stijging +22.9%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.7% | 30% |
| +15% | 55% | 30% | -5.8% | 28% |
| +20% | 52% | 26% | -5.9% | 27% |
| +25% | 49% | 23% | -6.0% | 26% |
| +30% | 46% | 21% | -6.1% | 25% |
| +35% | 44% | 19% | -6.2% | 24% |
| +45% | 40% | 16% | -6.4% | 23% |
| +60% | 35% | 13% | -6.3% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.0% (344, 15% win) | -9.3% (344, 15% win) | -7.6% (344, 15% win) | -7.0% (344, 16% win) | -10.0% (344, 15% win) | -9.4% (344, 15% win) |
| d35_direct | -10.1% (368, 14% win) | -9.4% (368, 14% win) | -7.7% (368, 15% win) | -7.0% (368, 15% win) | -10.1% (368, 14% win) | -9.5% (368, 14% win) |
| d40_direct | -11.5% (390, 12% win) | -10.8% (390, 13% win) | -9.1% (390, 13% win) | -8.4% (390, 13% win) | -11.5% (390, 12% win) | -10.9% (390, 12% win) |
| d45_direct | -12.4% (414, 10% win) | -11.8% (414, 10% win) | -10.1% (414, 11% win) | -9.4% (414, 11% win) | -12.6% (414, 10% win) | -12.0% (414, 10% win) |
| d50_direct | -12.2% (434, 8% win) | -11.5% (434, 8% win) | -9.8% (434, 9% win) | -9.2% (434, 9% win) | -12.6% (434, 8% win) | -11.9% (434, 8% win) |
| d55_direct | -11.4% (440, 8% win) | -10.7% (440, 8% win) | -9.1% (440, 8% win) | -8.5% (440, 8% win) | -12.0% (440, 7% win) | -11.4% (440, 8% win) |
| d60_direct | -10.1% (428, 8% win) | -9.4% (428, 8% win) | -7.8% (428, 8% win) | -7.2% (428, 8% win) | -11.0% (428, 7% win) | -10.3% (428, 8% win) |
| d65_direct | -10.1% (337, 9% win) | -9.4% (337, 9% win) | -7.9% (337, 9% win) | -7.2% (337, 9% win) | -11.0% (337, 8% win) | -10.4% (337, 9% win) |
| d70_direct | -10.9% (254, 6% win) | -10.2% (254, 6% win) | -8.7% (254, 6% win) | -8.1% (254, 6% win) | -11.9% (254, 5% win) | -11.2% (254, 6% win) |
| d75_direct | -10.8% (182, 6% win) | -10.2% (182, 6% win) | -8.7% (182, 7% win) | -8.0% (182, 7% win) | -11.9% (182, 6% win) | -11.3% (182, 6% win) |
| d80_direct | -10.3% (114, 5% win) | -9.7% (114, 5% win) | -8.3% (114, 5% win) | -7.6% (114, 5% win) | -11.9% (114, 4% win) | -11.3% (114, 4% win) |
| d45_herstel5 | -10.3% (302, 14% win) | -9.7% (302, 14% win) | -8.0% (302, 14% win) | -7.3% (302, 14% win) | -10.4% (302, 14% win) | -9.8% (302, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (1147, 19% win) | -9.0% (1147, 19% win) | -7.2% (1147, 20% win) | -6.5% (1147, 20% win) | -9.3% (1147, 19% win) | -8.6% (1147, 20% win) |
| d35_direct | -10.2% (1265, 18% win) | -9.5% (1265, 18% win) | -7.8% (1265, 19% win) | -7.1% (1265, 20% win) | -10.0% (1265, 18% win) | -9.3% (1265, 19% win) |
| d40_direct | -10.4% (1394, 17% win) | -9.8% (1394, 18% win) | -8.0% (1394, 19% win) | -7.4% (1394, 19% win) | -10.3% (1394, 17% win) | -9.7% (1394, 18% win) |
| d45_direct | -10.3% (1485, 17% win) | -9.6% (1485, 17% win) | -7.9% (1485, 19% win) | -7.2% (1485, 19% win) | -10.3% (1485, 17% win) | -9.7% (1485, 18% win) |
| d50_direct | -10.0% (1590, 17% win) | -9.3% (1590, 18% win) | -7.6% (1590, 19% win) | -7.0% (1590, 19% win) | -10.2% (1590, 17% win) | -9.6% (1590, 18% win) |
| d55_direct | -8.8% (1699, 18% win) | -8.1% (1699, 18% win) | -6.5% (1699, 19% win) | -5.8% (1699, 19% win) | -9.3% (1699, 17% win) | -8.7% (1699, 17% win) |
| d60_direct | -8.1% (1753, 18% win) | -7.4% (1753, 18% win) | -5.9% (1753, 19% win) | -5.2% (1753, 19% win) | -9.0% (1753, 18% win) | -8.3% (1753, 18% win) |
| d65_direct | -7.9% (1602, 19% win) | -7.2% (1602, 20% win) | -5.7% (1602, 20% win) | -5.0% (1602, 21% win) | -9.0% (1602, 19% win) | -8.4% (1602, 19% win) |
| d70_direct | -7.3% (1448, 21% win) | -6.6% (1448, 22% win) | -5.2% (1448, 23% win) | -4.5% (1448, 23% win) | -8.9% (1448, 21% win) | -8.3% (1448, 21% win) |
| d75_direct | -7.7% (1268, 23% win) | -7.0% (1268, 23% win) | -5.7% (1268, 24% win) | -5.0% (1268, 24% win) | -10.0% (1268, 21% win) | -9.4% (1268, 22% win) |
| d80_direct | -7.9% (1104, 25% win) | -7.2% (1104, 26% win) | -6.2% (1104, 26% win) | -5.5% (1104, 26% win) | -11.6% (1104, 23% win) | -10.9% (1104, 23% win) |
| d45_herstel5 | -7.2% (1211, 22% win) | -6.5% (1211, 22% win) | -4.8% (1211, 23% win) | -4.1% (1211, 23% win) | -7.3% (1211, 22% win) | -6.6% (1211, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.3% (6532, 24% win) | -8.6% (6532, 24% win) | -7.0% (6532, 25% win) | -6.3% (6532, 25% win) | -9.5% (6532, 23% win) | -8.9% (6532, 24% win) |
| d35_direct | -9.4% (6391, 22% win) | -8.7% (6391, 23% win) | -7.1% (6391, 24% win) | -6.4% (6391, 24% win) | -9.8% (6391, 22% win) | -9.1% (6391, 23% win) |
| d40_direct | -9.7% (6252, 22% win) | -9.0% (6252, 22% win) | -7.4% (6252, 23% win) | -6.8% (6252, 23% win) | -10.3% (6252, 21% win) | -9.7% (6252, 21% win) |
| d45_direct | -9.3% (6105, 21% win) | -8.6% (6105, 22% win) | -7.1% (6105, 22% win) | -6.4% (6105, 23% win) | -10.1% (6105, 21% win) | -9.5% (6105, 21% win) |
| d50_direct | -9.8% (5973, 20% win) | -9.1% (5973, 21% win) | -7.6% (5973, 22% win) | -6.9% (5973, 22% win) | -10.8% (5973, 20% win) | -10.2% (5973, 20% win) |
| d55_direct | -9.6% (5761, 20% win) | -8.9% (5761, 20% win) | -7.5% (5761, 21% win) | -6.8% (5761, 22% win) | -10.9% (5761, 19% win) | -10.3% (5761, 19% win) |
| d60_direct | -8.9% (5351, 21% win) | -8.3% (5351, 21% win) | -6.9% (5351, 22% win) | -6.2% (5351, 22% win) | -10.7% (5351, 20% win) | -10.1% (5351, 20% win) |
| d65_direct | -8.8% (4778, 22% win) | -8.1% (4778, 22% win) | -6.8% (4778, 23% win) | -6.2% (4778, 24% win) | -11.0% (4778, 20% win) | -10.4% (4778, 21% win) |
| d70_direct | -8.1% (4223, 24% win) | -7.4% (4223, 24% win) | -6.3% (4223, 25% win) | -5.6% (4223, 25% win) | -11.2% (4223, 22% win) | -10.5% (4223, 23% win) |
| d75_direct | -8.5% (3727, 24% win) | -7.8% (3727, 25% win) | -6.9% (3727, 25% win) | -6.2% (3727, 25% win) | -12.5% (3727, 22% win) | -11.9% (3727, 22% win) |
| d80_direct | -8.7% (3233, 27% win) | -8.0% (3233, 27% win) | -7.4% (3233, 27% win) | -6.8% (3233, 28% win) | -14.5% (3233, 23% win) | -13.9% (3233, 23% win) |
| d45_herstel5 | -8.8% (5025, 25% win) | -8.1% (5025, 26% win) | -6.6% (5025, 26% win) | -5.9% (5025, 27% win) | -9.8% (5025, 24% win) | -9.2% (5025, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.4% (6105, 23% win) | -6.1% (6105, 22% win) | -6.5% (6105, 22% win) |
| schoon | -6.2% (4898, 24% win) | -5.9% (4898, 24% win) | -6.3% (4898, 23% win) |
| bundelgrafiek | -7.2% (1207, 18% win) | -6.5% (1207, 18% win) | -7.4% (1207, 16% win) |
| schoon+houders_ok | -7.2% (1485, 19% win) | -6.7% (1485, 18% win) | -6.6% (1485, 20% win) |
| schoon+houders_ok+final_stretch | -8.6% (635, 12% win) | -7.3% (635, 11% win) | -9.9% (635, 14% win) |
| volledige_screening+schoon | -9.4% (414, 11% win) | -8.3% (414, 9% win) | -11.5% (414, 14% win) |
| volledige_screening+schoon+x_link | -9.3% (295, 12% win) | -8.3% (295, 10% win) | -11.4% (295, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.5% (2611, 28% win); 1,3–2x: -7.0% (2286, 19% win); ≥ 2x (bundelgrafiek): -7.2% (1208, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.5% (3859, 29% win); 5–20%: -8.3% (1056, 14% win); ≥ 20%: -7.4% (1190, 12% win)

**top t.o.v. start:** 2–3x: -6.5% (3437, 22% win); 3–6x: -6.0% (2092, 24% win); ≥ 6x: -7.3% (576, 25% win)

**unieke kopers tot de top:** < 30: -5.5% (3849, 29% win); 30–100: -7.2% (1285, 12% win); ≥ 100: -8.7% (971, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.9% (1484, 16% win); 1–2: -6.0% (2932, 24% win); ≥ 3 (trap): -6.7% (1689, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.4% (1508, 13% win); 10–25%: -7.9% (988, 12% win); ≥ 25%: -5.1% (3609, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.7% (4801, 26% win); 30 s–3 min: -8.7% (1037, 14% win); ≥ 3 min (langzaam): -10.3% (267, 7% win)

**tijd van start tot top:** < 2 min: -6.0% (5012, 24% win); 2–10 min: -7.7% (872, 16% win); ≥ 10 min: -10.7% (221, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
