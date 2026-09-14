# Videostrategie op alle trades — 2026-09-14 06:05 UTC

Tokens sinds 2026-09-11 08:47 UTC: 57450 geschikt (≥ 2 uur oud, geen herstart), 44802 met trades, 8047 haalden 2x de startkoers, 6167 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1889 tokens. Houdercheck echt uitgevoerd bij 92% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1493, winkans 19%, EV per trade -7.2% (95%-marge -8.8% tot -5.6%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 4465, winkans 23%, EV -6.7% (95%-marge -8.3% tot -5.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 134, winkans 16%, EV -10.2% (95%-marge -13.7% tot -6.7%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 6167 | 40% | 77% | 37% |
| schoon | 4954 | 42% | 76% | 40% |
| bundelgrafiek | 1213 | 31% | 77% | 25% |
| schoon+houders_ok | 1493 | 36% | 79% | 23% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.2% (6600, 25% win) | -6.3% (6457, 24% win) | -6.8% (6315, 23% win) | -6.4% (6167, 23% win) | -6.9% (6032, 22% win) | -6.8% (5814, 22% win) | -6.3% (5402, 22% win) | -6.2% (4823, 24% win) | -5.7% (4266, 25% win) | -6.3% (3768, 25% win) | -7.0% (3269, 27% win) | -5.9% (5081, 27% win) |
| schoon | -6.2% (5292, 26% win) | -6.1% (5192, 25% win) | -6.6% (5081, 24% win) | -6.2% (4954, 24% win) | -6.4% (4845, 24% win) | -6.5% (4661, 23% win) | -5.9% (4297, 24% win) | -5.6% (3827, 26% win) | -5.2% (3412, 27% win) | -5.9% (3026, 27% win) | -6.8% (2670, 29% win) | -5.7% (4257, 27% win) |
| bundelgrafiek | -5.9% (1308, 24% win) | -7.2% (1265, 22% win) | -7.6% (1234, 19% win) | -7.1% (1213, 18% win) | -9.0% (1187, 16% win) | -7.8% (1153, 15% win) | -7.8% (1105, 16% win) | -8.7% (996, 16% win) | -7.7% (854, 18% win) | -8.3% (742, 18% win) | -8.0% (599, 20% win) | -6.8% (824, 25% win) |
| schoon+houders_ok | -6.5% (1150, 20% win) | -7.1% (1270, 20% win) | -7.4% (1402, 19% win) | -7.2% (1493, 19% win) | -6.9% (1600, 19% win) | -5.8% (1709, 19% win) | -5.2% (1765, 19% win) | -4.9% (1611, 21% win) | -4.4% (1456, 23% win) | -4.9% (1274, 24% win) | -5.3% (1106, 26% win) | -4.1% (1217, 23% win) |
| schoon+houders_ok+final_stretch | -7.2% (490, 16% win) | -7.4% (545, 14% win) | -8.1% (602, 12% win) | -8.5% (639, 12% win) | -8.5% (682, 10% win) | -7.4% (719, 10% win) | -6.9% (717, 10% win) | -6.6% (564, 10% win) | -7.0% (436, 9% win) | -7.0% (300, 9% win) | -5.1% (189, 12% win) | -5.7% (491, 16% win) |
| volledige_screening+schoon | -7.0% (345, 16% win) | -7.1% (371, 15% win) | -8.5% (393, 13% win) | -9.3% (417, 11% win) | -9.2% (438, 9% win) | -8.5% (443, 8% win) | -7.2% (431, 8% win) | -7.2% (339, 9% win) | -8.1% (255, 6% win) | -8.0% (183, 7% win) | -7.6% (114, 5% win) | -7.1% (304, 14% win) |
| volledige_screening+schoon+x_link | -7.5% (263, 17% win) | -6.0% (279, 18% win) | -8.3% (288, 15% win) | -9.3% (296, 12% win) | -9.2% (300, 10% win) | -8.8% (301, 9% win) | -8.2% (293, 8% win) | -8.3% (239, 7% win) | -8.0% (181, 6% win) | -8.3% (132, 6% win) | -8.1% (84, 2% win) | -7.2% (212, 14% win) |

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
| alle | -6.1% (6600, 30% win) | -6.5% (6457, 29% win) | -6.6% (6315, 28% win) | -6.4% (6167, 28% win) | -7.2% (6032, 26% win) | -6.7% (5814, 26% win) | -6.6% (5402, 27% win) | -6.3% (4823, 28% win) | -6.5% (4266, 31% win) | -6.8% (3768, 32% win) | -7.4% (3269, 33% win) |
| schoon | -6.2% (5292, 30% win) | -6.3% (5192, 30% win) | -6.6% (5081, 29% win) | -6.4% (4954, 29% win) | -7.1% (4845, 28% win) | -6.7% (4661, 28% win) | -6.5% (4297, 29% win) | -5.8% (3827, 31% win) | -5.9% (3412, 33% win) | -6.2% (3026, 34% win) | -6.9% (2670, 35% win) |
| bundelgrafiek | -5.8% (1308, 28% win) | -7.0% (1265, 26% win) | -6.6% (1234, 23% win) | -6.3% (1213, 22% win) | -7.6% (1187, 21% win) | -6.6% (1153, 20% win) | -7.2% (1105, 19% win) | -8.6% (996, 18% win) | -8.8% (854, 21% win) | -8.9% (742, 22% win) | -9.5% (599, 24% win) |
| schoon+houders_ok | -6.6% (1150, 27% win) | -6.8% (1270, 27% win) | -6.6% (1402, 27% win) | -7.0% (1493, 27% win) | -7.4% (1600, 26% win) | -6.1% (1709, 26% win) | -5.5% (1765, 26% win) | -5.2% (1611, 29% win) | -4.5% (1456, 32% win) | -4.7% (1274, 33% win) | -6.6% (1106, 34% win) |
| schoon+houders_ok+final_stretch | -7.1% (490, 24% win) | -7.4% (545, 24% win) | -7.4% (602, 23% win) | -9.2% (639, 21% win) | -10.3% (682, 17% win) | -9.2% (719, 18% win) | -7.4% (717, 20% win) | -7.5% (564, 21% win) | -7.8% (436, 24% win) | -7.1% (300, 26% win) | -5.9% (189, 26% win) |
| volledige_screening+schoon | -7.2% (345, 25% win) | -7.5% (371, 23% win) | -7.9% (393, 24% win) | -10.4% (417, 20% win) | -11.3% (438, 16% win) | -10.6% (443, 17% win) | -8.2% (431, 18% win) | -8.3% (339, 19% win) | -10.1% (255, 19% win) | -9.4% (183, 20% win) | -8.8% (114, 18% win) |
| volledige_screening+schoon+x_link | -7.2% (263, 25% win) | -6.6% (279, 24% win) | -8.0% (288, 24% win) | -10.8% (296, 19% win) | -11.7% (300, 15% win) | -10.2% (301, 16% win) | -7.9% (293, 18% win) | -8.1% (239, 18% win) | -9.0% (181, 20% win) | -9.2% (132, 20% win) | -8.8% (84, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 417 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -7.9% | 25% |
| +15% | 42% | 20% | -7.9% | 21% |
| +20% | 39% | 18% | -7.8% | 19% |
| +25% | 34% | 15% | -8.2% | 17% |
| +30% | 31% | 13% | -8.3% | 15% |
| +35% | 29% | 12% | -8.3% | 14% |
| +45% | 24% | 8% | -9.3% | 11% |
| +60% | 20% | 7% | -9.2% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1493 instappen, mediane hoogste stijging +20.0%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 58% | 32% | -5.8% | 30% |
| +15% | 53% | 26% | -5.9% | 27% |
| +20% | 50% | 23% | -6.0% | 25% |
| +25% | 47% | 21% | -6.1% | 24% |
| +30% | 44% | 19% | -6.3% | 23% |
| +35% | 41% | 16% | -6.5% | 21% |
| +45% | 36% | 13% | -7.2% | 19% |
| +60% | 32% | 10% | -7.1% | 18% |

**filter `alle`** — variant `d45_direct`, 6167 instappen, mediane hoogste stijging +22.9%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.7% | 30% |
| +15% | 55% | 30% | -5.8% | 28% |
| +20% | 52% | 26% | -5.9% | 27% |
| +25% | 49% | 23% | -6.0% | 26% |
| +30% | 46% | 21% | -6.1% | 25% |
| +35% | 44% | 19% | -6.2% | 24% |
| +45% | 39% | 16% | -6.4% | 23% |
| +60% | 35% | 13% | -6.3% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.1% (345, 15% win) | -9.4% (345, 15% win) | -7.7% (345, 15% win) | -7.0% (345, 16% win) | -10.1% (345, 15% win) | -9.4% (345, 15% win) |
| d35_direct | -10.2% (371, 14% win) | -9.5% (371, 14% win) | -7.8% (371, 15% win) | -7.1% (371, 15% win) | -10.2% (371, 14% win) | -9.6% (371, 14% win) |
| d40_direct | -11.5% (393, 12% win) | -10.8% (393, 12% win) | -9.1% (393, 13% win) | -8.5% (393, 13% win) | -11.6% (393, 12% win) | -10.9% (393, 12% win) |
| d45_direct | -12.3% (417, 10% win) | -11.7% (417, 11% win) | -10.0% (417, 11% win) | -9.3% (417, 11% win) | -12.5% (417, 10% win) | -11.9% (417, 10% win) |
| d50_direct | -12.2% (438, 8% win) | -11.5% (438, 8% win) | -9.9% (438, 9% win) | -9.2% (438, 9% win) | -12.6% (438, 8% win) | -12.0% (438, 8% win) |
| d55_direct | -11.4% (443, 8% win) | -10.8% (443, 8% win) | -9.2% (443, 8% win) | -8.5% (443, 8% win) | -12.0% (443, 7% win) | -11.4% (443, 8% win) |
| d60_direct | -10.1% (431, 8% win) | -9.4% (431, 8% win) | -7.9% (431, 8% win) | -7.2% (431, 8% win) | -11.0% (431, 7% win) | -10.3% (431, 8% win) |
| d65_direct | -10.1% (339, 9% win) | -9.4% (339, 9% win) | -7.9% (339, 9% win) | -7.2% (339, 9% win) | -11.0% (339, 8% win) | -10.4% (339, 9% win) |
| d70_direct | -10.9% (255, 6% win) | -10.3% (255, 6% win) | -8.7% (255, 6% win) | -8.1% (255, 6% win) | -11.9% (255, 5% win) | -11.2% (255, 6% win) |
| d75_direct | -10.9% (183, 6% win) | -10.2% (183, 6% win) | -8.7% (183, 7% win) | -8.0% (183, 7% win) | -12.0% (183, 6% win) | -11.3% (183, 6% win) |
| d80_direct | -10.3% (114, 5% win) | -9.7% (114, 5% win) | -8.3% (114, 5% win) | -7.6% (114, 5% win) | -11.9% (114, 4% win) | -11.3% (114, 4% win) |
| d45_herstel5 | -10.2% (304, 14% win) | -9.5% (304, 14% win) | -7.8% (304, 14% win) | -7.1% (304, 14% win) | -10.2% (304, 14% win) | -9.6% (304, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (1150, 19% win) | -9.0% (1150, 19% win) | -7.2% (1150, 20% win) | -6.5% (1150, 20% win) | -9.3% (1150, 19% win) | -8.6% (1150, 20% win) |
| d35_direct | -10.2% (1270, 18% win) | -9.5% (1270, 18% win) | -7.8% (1270, 19% win) | -7.1% (1270, 20% win) | -10.0% (1270, 18% win) | -9.3% (1270, 19% win) |
| d40_direct | -10.4% (1402, 17% win) | -9.8% (1402, 18% win) | -8.0% (1402, 19% win) | -7.4% (1402, 19% win) | -10.3% (1402, 17% win) | -9.7% (1402, 18% win) |
| d45_direct | -10.2% (1493, 17% win) | -9.6% (1493, 18% win) | -7.9% (1493, 19% win) | -7.2% (1493, 19% win) | -10.3% (1493, 17% win) | -9.7% (1493, 18% win) |
| d50_direct | -10.0% (1600, 18% win) | -9.3% (1600, 18% win) | -7.6% (1600, 19% win) | -6.9% (1600, 19% win) | -10.2% (1600, 17% win) | -9.6% (1600, 18% win) |
| d55_direct | -8.8% (1709, 17% win) | -8.1% (1709, 18% win) | -6.5% (1709, 19% win) | -5.8% (1709, 19% win) | -9.4% (1709, 17% win) | -8.7% (1709, 17% win) |
| d60_direct | -8.1% (1765, 18% win) | -7.4% (1765, 18% win) | -5.8% (1765, 19% win) | -5.2% (1765, 19% win) | -8.9% (1765, 18% win) | -8.3% (1765, 18% win) |
| d65_direct | -7.8% (1611, 19% win) | -7.0% (1611, 20% win) | -5.6% (1611, 20% win) | -4.9% (1611, 21% win) | -8.9% (1611, 19% win) | -8.2% (1611, 19% win) |
| d70_direct | -7.2% (1456, 22% win) | -6.5% (1456, 22% win) | -5.1% (1456, 23% win) | -4.4% (1456, 23% win) | -8.8% (1456, 21% win) | -8.2% (1456, 21% win) |
| d75_direct | -7.6% (1274, 23% win) | -6.9% (1274, 23% win) | -5.6% (1274, 24% win) | -4.9% (1274, 24% win) | -9.9% (1274, 21% win) | -9.3% (1274, 22% win) |
| d80_direct | -7.7% (1106, 25% win) | -7.0% (1106, 26% win) | -6.0% (1106, 26% win) | -5.3% (1106, 26% win) | -11.4% (1106, 23% win) | -10.8% (1106, 23% win) |
| d45_herstel5 | -7.2% (1217, 22% win) | -6.5% (1217, 22% win) | -4.8% (1217, 23% win) | -4.1% (1217, 23% win) | -7.3% (1217, 22% win) | -6.6% (1217, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.2% (6600, 24% win) | -8.5% (6600, 24% win) | -6.9% (6600, 25% win) | -6.2% (6600, 25% win) | -9.4% (6600, 23% win) | -8.8% (6600, 24% win) |
| d35_direct | -9.3% (6457, 23% win) | -8.6% (6457, 23% win) | -7.0% (6457, 24% win) | -6.3% (6457, 24% win) | -9.7% (6457, 22% win) | -9.1% (6457, 23% win) |
| d40_direct | -9.7% (6315, 22% win) | -9.0% (6315, 22% win) | -7.4% (6315, 23% win) | -6.8% (6315, 23% win) | -10.3% (6315, 21% win) | -9.7% (6315, 22% win) |
| d45_direct | -9.3% (6167, 21% win) | -8.6% (6167, 22% win) | -7.1% (6167, 22% win) | -6.4% (6167, 23% win) | -10.1% (6167, 21% win) | -9.5% (6167, 21% win) |
| d50_direct | -9.8% (6032, 20% win) | -9.1% (6032, 21% win) | -7.6% (6032, 22% win) | -6.9% (6032, 22% win) | -10.8% (6032, 20% win) | -10.2% (6032, 20% win) |
| d55_direct | -9.6% (5814, 20% win) | -8.9% (5814, 20% win) | -7.5% (5814, 21% win) | -6.8% (5814, 22% win) | -10.9% (5814, 19% win) | -10.3% (5814, 19% win) |
| d60_direct | -9.0% (5402, 21% win) | -8.3% (5402, 21% win) | -7.0% (5402, 22% win) | -6.3% (5402, 22% win) | -10.7% (5402, 20% win) | -10.1% (5402, 20% win) |
| d65_direct | -8.9% (4823, 22% win) | -8.2% (4823, 22% win) | -6.9% (4823, 23% win) | -6.2% (4823, 24% win) | -11.1% (4823, 20% win) | -10.5% (4823, 21% win) |
| d70_direct | -8.2% (4266, 24% win) | -7.5% (4266, 24% win) | -6.4% (4266, 25% win) | -5.7% (4266, 25% win) | -11.2% (4266, 22% win) | -10.6% (4266, 23% win) |
| d75_direct | -8.6% (3768, 24% win) | -8.0% (3768, 24% win) | -7.0% (3768, 25% win) | -6.3% (3768, 25% win) | -12.6% (3768, 22% win) | -12.0% (3768, 22% win) |
| d80_direct | -8.9% (3269, 27% win) | -8.3% (3269, 27% win) | -7.7% (3269, 27% win) | -7.0% (3269, 27% win) | -14.7% (3269, 23% win) | -14.1% (3269, 23% win) |
| d45_herstel5 | -8.7% (5081, 25% win) | -8.0% (5081, 26% win) | -6.6% (5081, 26% win) | -5.9% (5081, 27% win) | -9.8% (5081, 24% win) | -9.2% (5081, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.4% (6167, 23% win) | -6.1% (6167, 22% win) | -6.5% (6167, 22% win) |
| schoon | -6.2% (4954, 24% win) | -6.0% (4954, 24% win) | -6.3% (4954, 23% win) |
| bundelgrafiek | -7.1% (1213, 18% win) | -6.5% (1213, 18% win) | -7.4% (1213, 16% win) |
| schoon+houders_ok | -7.2% (1493, 19% win) | -6.7% (1493, 18% win) | -6.6% (1493, 20% win) |
| schoon+houders_ok+final_stretch | -8.5% (639, 12% win) | -7.3% (639, 11% win) | -9.9% (639, 14% win) |
| volledige_screening+schoon | -9.3% (417, 11% win) | -8.3% (417, 9% win) | -11.4% (417, 14% win) |
| volledige_screening+schoon+x_link | -9.3% (296, 12% win) | -8.3% (296, 10% win) | -11.4% (296, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.5% (2648, 28% win); 1,3–2x: -7.0% (2305, 19% win); ≥ 2x (bundelgrafiek): -7.1% (1214, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.5% (3902, 29% win); 5–20%: -8.3% (1064, 14% win); ≥ 20%: -7.5% (1201, 11% win)

**top t.o.v. start:** 2–3x: -6.5% (3474, 22% win); 3–6x: -5.9% (2112, 24% win); ≥ 6x: -7.4% (581, 25% win)

**unieke kopers tot de top:** < 30: -5.5% (3892, 29% win); 30–100: -7.2% (1294, 12% win); ≥ 100: -8.7% (981, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.8% (1494, 16% win); 1–2: -6.0% (2961, 24% win); ≥ 3 (trap): -6.6% (1712, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.4% (1520, 13% win); 10–25%: -7.9% (1001, 12% win); ≥ 25%: -5.1% (3646, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.7% (4846, 26% win); 30 s–3 min: -8.6% (1050, 14% win); ≥ 3 min (langzaam): -10.3% (271, 7% win)

**tijd van start tot top:** < 2 min: -6.0% (5059, 25% win); 2–10 min: -7.6% (883, 16% win); ≥ 10 min: -10.7% (225, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
