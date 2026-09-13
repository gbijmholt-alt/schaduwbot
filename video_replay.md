# Videostrategie op alle trades — 2026-09-13 09:16 UTC

Tokens sinds 2026-09-11 08:47 UTC: 34914 geschikt (≥ 2 uur oud, geen herstart), 28003 met trades, 5401 haalden 2x de startkoers, 4117 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1261 tokens. Houdercheck echt uitgevoerd bij 88% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1244, winkans 21%, EV per trade -6.9% (95%-marge -8.7% tot -5.1%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2794, winkans 24%, EV -6.6% (95%-marge -8.6% tot -4.6%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 3, winkans 0%, EV -13.3% (95%-marge -19.7% tot -7.0%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4117 | 40% | 76% | 37% |
| schoon | 3283 | 43% | 76% | 40% |
| bundelgrafiek | 834 | 30% | 78% | 25% |
| schoon+houders_ok | 1244 | 38% | 79% | 27% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.4% (4398, 25% win) | -6.6% (4308, 24% win) | -7.0% (4214, 23% win) | -6.8% (4117, 23% win) | -7.3% (4024, 22% win) | -7.1% (3873, 21% win) | -6.5% (3599, 22% win) | -6.2% (3215, 24% win) | -5.5% (2849, 26% win) | -6.5% (2518, 25% win) | -6.9% (2191, 27% win) | -6.6% (3382, 26% win) |
| schoon | -6.2% (3514, 26% win) | -6.1% (3449, 26% win) | -6.6% (3369, 25% win) | -6.4% (3283, 24% win) | -6.8% (3213, 23% win) | -7.0% (3087, 23% win) | -6.0% (2841, 24% win) | -5.3% (2529, 26% win) | -4.9% (2266, 28% win) | -6.0% (2012, 27% win) | -6.5% (1776, 29% win) | -6.0% (2821, 27% win) |
| bundelgrafiek | -7.2% (884, 22% win) | -8.4% (859, 19% win) | -8.5% (845, 17% win) | -8.1% (834, 16% win) | -9.5% (811, 15% win) | -7.7% (786, 15% win) | -8.1% (758, 15% win) | -9.8% (686, 15% win) | -8.1% (583, 17% win) | -8.5% (506, 18% win) | -8.7% (415, 19% win) | -9.4% (561, 22% win) |
| schoon+houders_ok | -6.6% (993, 21% win) | -6.8% (1088, 21% win) | -7.1% (1176, 20% win) | -6.9% (1244, 21% win) | -6.7% (1326, 21% win) | -5.5% (1398, 21% win) | -5.0% (1423, 21% win) | -4.3% (1287, 23% win) | -3.9% (1171, 26% win) | -4.8% (1038, 26% win) | -5.2% (926, 29% win) | -3.9% (1035, 24% win) |
| schoon+houders_ok+final_stretch | -7.7% (412, 16% win) | -7.0% (449, 16% win) | -8.0% (476, 13% win) | -8.8% (499, 12% win) | -8.6% (519, 10% win) | -7.6% (538, 10% win) | -6.7% (522, 10% win) | -6.1% (399, 11% win) | -7.7% (296, 9% win) | -7.5% (196, 9% win) | -5.2% (120, 12% win) | -5.8% (387, 16% win) |
| volledige_screening+schoon | -7.7% (281, 16% win) | -6.3% (292, 17% win) | -8.6% (294, 13% win) | -9.8% (306, 11% win) | -9.7% (311, 10% win) | -8.4% (312, 8% win) | -6.9% (301, 9% win) | -7.4% (235, 8% win) | -9.0% (174, 5% win) | -8.8% (117, 8% win) | -9.1% (73, 4% win) | -7.2% (225, 14% win) |
| volledige_screening+schoon+x_link | -8.3% (221, 16% win) | -5.2% (230, 20% win) | -8.9% (229, 14% win) | -10.0% (233, 11% win) | -10.0% (231, 9% win) | -9.3% (231, 8% win) | -8.5% (224, 7% win) | -8.7% (174, 6% win) | -8.6% (130, 5% win) | -8.7% (90, 7% win) | -8.7% (57, 2% win) | -7.6% (164, 13% win) |

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
| alle | -6.1% (4398, 30% win) | -6.0% (4308, 29% win) | -6.4% (4214, 28% win) | -6.5% (4117, 28% win) | -7.5% (4024, 26% win) | -7.0% (3873, 26% win) | -6.4% (3599, 27% win) | -6.6% (3215, 28% win) | -6.2% (2849, 31% win) | -6.5% (2518, 32% win) | -7.6% (2191, 33% win) |
| schoon | -5.9% (3514, 31% win) | -5.6% (3449, 30% win) | -6.2% (3369, 29% win) | -6.2% (3283, 30% win) | -7.5% (3213, 27% win) | -7.0% (3087, 27% win) | -6.1% (2841, 30% win) | -5.9% (2529, 31% win) | -5.5% (2266, 34% win) | -5.8% (2012, 34% win) | -6.9% (1776, 35% win) |
| bundelgrafiek | -6.7% (884, 26% win) | -7.7% (859, 24% win) | -7.1% (845, 22% win) | -7.3% (834, 21% win) | -7.7% (811, 20% win) | -6.7% (786, 20% win) | -7.4% (758, 18% win) | -9.0% (686, 17% win) | -8.6% (583, 20% win) | -9.0% (506, 22% win) | -10.3% (415, 23% win) |
| schoon+houders_ok | -6.5% (993, 28% win) | -6.4% (1088, 28% win) | -6.5% (1176, 28% win) | -6.8% (1244, 28% win) | -6.9% (1326, 27% win) | -5.6% (1398, 28% win) | -4.9% (1423, 28% win) | -4.7% (1287, 30% win) | -3.8% (1171, 34% win) | -4.5% (1038, 35% win) | -6.8% (926, 34% win) |
| schoon+houders_ok+final_stretch | -7.1% (412, 24% win) | -7.0% (449, 24% win) | -7.2% (476, 23% win) | -8.8% (499, 21% win) | -10.3% (519, 17% win) | -9.3% (538, 18% win) | -6.2% (522, 21% win) | -6.7% (399, 22% win) | -8.3% (296, 23% win) | -7.3% (196, 26% win) | -6.7% (120, 25% win) |
| volledige_screening+schoon | -7.0% (281, 25% win) | -6.9% (292, 24% win) | -7.9% (294, 25% win) | -10.0% (306, 21% win) | -11.5% (311, 17% win) | -10.8% (312, 17% win) | -7.3% (301, 18% win) | -8.5% (235, 18% win) | -11.6% (174, 16% win) | -10.9% (117, 17% win) | -13.0% (73, 11% win) |
| volledige_screening+schoon+x_link | -7.1% (221, 26% win) | -6.0% (230, 26% win) | -7.6% (229, 24% win) | -10.7% (233, 20% win) | -12.3% (231, 14% win) | -10.9% (231, 15% win) | -7.9% (224, 16% win) | -8.8% (174, 16% win) | -9.6% (130, 18% win) | -11.2% (90, 17% win) | -13.1% (57, 7% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 306 instappen, mediane hoogste stijging +8.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 47% | 24% | -8.4% | 25% |
| +15% | 41% | 18% | -8.6% | 21% |
| +20% | 38% | 16% | -8.6% | 18% |
| +25% | 33% | 13% | -8.8% | 16% |
| +30% | 30% | 12% | -8.9% | 15% |
| +35% | 28% | 11% | -9.0% | 14% |
| +45% | 24% | 8% | -9.8% | 11% |
| +60% | 21% | 7% | -9.6% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1244 instappen, mediane hoogste stijging +21.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.4% | 31% |
| +15% | 54% | 28% | -5.6% | 28% |
| +20% | 51% | 24% | -5.7% | 26% |
| +25% | 48% | 22% | -5.9% | 24% |
| +30% | 45% | 20% | -6.0% | 24% |
| +35% | 42% | 17% | -6.2% | 22% |
| +45% | 38% | 14% | -6.9% | 21% |
| +60% | 33% | 11% | -6.7% | 19% |

**filter `alle`** — variant `d45_direct`, 4117 instappen, mediane hoogste stijging +22.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -6.0% | 30% |
| +15% | 55% | 30% | -6.2% | 28% |
| +20% | 52% | 27% | -6.4% | 26% |
| +25% | 49% | 24% | -6.4% | 26% |
| +30% | 46% | 21% | -6.6% | 25% |
| +35% | 43% | 19% | -6.7% | 24% |
| +45% | 39% | 16% | -6.8% | 23% |
| +60% | 35% | 13% | -6.6% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.8% (281, 14% win) | -10.1% (281, 15% win) | -8.4% (281, 15% win) | -7.7% (281, 16% win) | -10.8% (281, 14% win) | -10.1% (281, 14% win) |
| d35_direct | -9.3% (292, 16% win) | -8.6% (292, 16% win) | -7.0% (292, 17% win) | -6.3% (292, 17% win) | -9.4% (292, 16% win) | -8.8% (292, 16% win) |
| d40_direct | -11.6% (294, 13% win) | -11.0% (294, 13% win) | -9.3% (294, 13% win) | -8.6% (294, 13% win) | -11.7% (294, 12% win) | -11.1% (294, 13% win) |
| d45_direct | -12.8% (306, 10% win) | -12.2% (306, 10% win) | -10.5% (306, 11% win) | -9.8% (306, 11% win) | -13.0% (306, 10% win) | -12.4% (306, 10% win) |
| d50_direct | -12.6% (311, 9% win) | -12.0% (311, 9% win) | -10.3% (311, 9% win) | -9.7% (311, 10% win) | -13.0% (311, 8% win) | -12.4% (311, 9% win) |
| d55_direct | -11.4% (312, 8% win) | -10.7% (312, 8% win) | -9.1% (312, 8% win) | -8.4% (312, 8% win) | -12.0% (312, 7% win) | -11.4% (312, 8% win) |
| d60_direct | -9.8% (301, 9% win) | -9.2% (301, 9% win) | -7.6% (301, 9% win) | -6.9% (301, 9% win) | -10.8% (301, 7% win) | -10.1% (301, 8% win) |
| d65_direct | -10.2% (235, 9% win) | -9.6% (235, 9% win) | -8.0% (235, 8% win) | -7.4% (235, 8% win) | -11.2% (235, 8% win) | -10.6% (235, 8% win) |
| d70_direct | -11.9% (174, 5% win) | -11.2% (174, 5% win) | -9.7% (174, 5% win) | -9.0% (174, 5% win) | -12.9% (174, 4% win) | -12.3% (174, 5% win) |
| d75_direct | -11.7% (117, 6% win) | -11.0% (117, 6% win) | -9.5% (117, 8% win) | -8.8% (117, 8% win) | -12.9% (117, 5% win) | -12.3% (117, 5% win) |
| d80_direct | -11.8% (73, 4% win) | -11.1% (73, 4% win) | -9.8% (73, 4% win) | -9.1% (73, 4% win) | -13.7% (73, 3% win) | -13.1% (73, 3% win) |
| d45_herstel5 | -10.2% (225, 14% win) | -9.6% (225, 14% win) | -7.9% (225, 14% win) | -7.2% (225, 14% win) | -10.3% (225, 14% win) | -9.7% (225, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (993, 19% win) | -9.0% (993, 20% win) | -7.3% (993, 21% win) | -6.6% (993, 21% win) | -9.3% (993, 20% win) | -8.7% (993, 20% win) |
| d35_direct | -9.8% (1088, 19% win) | -9.2% (1088, 19% win) | -7.4% (1088, 21% win) | -6.8% (1088, 21% win) | -9.6% (1088, 19% win) | -9.0% (1088, 20% win) |
| d40_direct | -10.2% (1176, 19% win) | -9.5% (1176, 19% win) | -7.8% (1176, 20% win) | -7.1% (1176, 20% win) | -10.1% (1176, 18% win) | -9.4% (1176, 19% win) |
| d45_direct | -9.9% (1244, 18% win) | -9.3% (1244, 19% win) | -7.6% (1244, 20% win) | -6.9% (1244, 21% win) | -10.0% (1244, 18% win) | -9.4% (1244, 19% win) |
| d50_direct | -9.7% (1326, 19% win) | -9.0% (1326, 19% win) | -7.3% (1326, 20% win) | -6.7% (1326, 21% win) | -9.9% (1326, 19% win) | -9.3% (1326, 19% win) |
| d55_direct | -8.4% (1398, 19% win) | -7.7% (1398, 19% win) | -6.1% (1398, 20% win) | -5.5% (1398, 21% win) | -9.0% (1398, 18% win) | -8.3% (1398, 19% win) |
| d60_direct | -7.9% (1423, 20% win) | -7.2% (1423, 20% win) | -5.7% (1423, 21% win) | -5.0% (1423, 21% win) | -8.8% (1423, 19% win) | -8.1% (1423, 20% win) |
| d65_direct | -7.2% (1287, 21% win) | -6.5% (1287, 22% win) | -5.0% (1287, 23% win) | -4.3% (1287, 23% win) | -8.4% (1287, 21% win) | -7.8% (1287, 21% win) |
| d70_direct | -6.7% (1171, 24% win) | -5.9% (1171, 25% win) | -4.6% (1171, 25% win) | -3.9% (1171, 26% win) | -8.5% (1171, 23% win) | -7.8% (1171, 24% win) |
| d75_direct | -7.4% (1038, 25% win) | -6.7% (1038, 26% win) | -5.5% (1038, 26% win) | -4.8% (1038, 26% win) | -10.0% (1038, 23% win) | -9.4% (1038, 24% win) |
| d80_direct | -7.5% (926, 27% win) | -6.8% (926, 28% win) | -5.9% (926, 28% win) | -5.2% (926, 29% win) | -11.6% (926, 25% win) | -11.0% (926, 25% win) |
| d45_herstel5 | -7.0% (1035, 23% win) | -6.3% (1035, 23% win) | -4.6% (1035, 24% win) | -3.9% (1035, 24% win) | -7.1% (1035, 23% win) | -6.4% (1035, 23% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.4% (4398, 23% win) | -8.8% (4398, 24% win) | -7.1% (4398, 25% win) | -6.4% (4398, 25% win) | -9.7% (4398, 23% win) | -9.0% (4398, 24% win) |
| d35_direct | -9.5% (4308, 22% win) | -8.8% (4308, 23% win) | -7.2% (4308, 24% win) | -6.6% (4308, 24% win) | -10.0% (4308, 22% win) | -9.3% (4308, 23% win) |
| d40_direct | -9.9% (4214, 22% win) | -9.2% (4214, 22% win) | -7.7% (4214, 23% win) | -7.0% (4214, 23% win) | -10.5% (4214, 21% win) | -9.9% (4214, 22% win) |
| d45_direct | -9.7% (4117, 21% win) | -9.0% (4117, 22% win) | -7.4% (4117, 22% win) | -6.8% (4117, 23% win) | -10.5% (4117, 20% win) | -9.8% (4117, 21% win) |
| d50_direct | -10.2% (4024, 20% win) | -9.5% (4024, 21% win) | -8.0% (4024, 21% win) | -7.3% (4024, 22% win) | -11.2% (4024, 19% win) | -10.6% (4024, 20% win) |
| d55_direct | -10.0% (3873, 20% win) | -9.3% (3873, 20% win) | -7.8% (3873, 21% win) | -7.1% (3873, 21% win) | -11.3% (3873, 18% win) | -10.6% (3873, 19% win) |
| d60_direct | -9.2% (3599, 21% win) | -8.5% (3599, 21% win) | -7.1% (3599, 22% win) | -6.5% (3599, 22% win) | -10.9% (3599, 20% win) | -10.3% (3599, 20% win) |
| d65_direct | -8.9% (3215, 22% win) | -8.2% (3215, 22% win) | -6.9% (3215, 23% win) | -6.2% (3215, 24% win) | -11.1% (3215, 20% win) | -10.5% (3215, 21% win) |
| d70_direct | -8.1% (2849, 24% win) | -7.3% (2849, 25% win) | -6.2% (2849, 25% win) | -5.5% (2849, 26% win) | -11.1% (2849, 22% win) | -10.5% (2849, 23% win) |
| d75_direct | -8.8% (2518, 24% win) | -8.1% (2518, 24% win) | -7.2% (2518, 25% win) | -6.5% (2518, 25% win) | -12.9% (2518, 21% win) | -12.2% (2518, 22% win) |
| d80_direct | -8.8% (2191, 27% win) | -8.1% (2191, 27% win) | -7.6% (2191, 27% win) | -6.9% (2191, 27% win) | -14.8% (2191, 22% win) | -14.2% (2191, 22% win) |
| d45_herstel5 | -9.4% (3382, 25% win) | -8.7% (3382, 25% win) | -7.2% (3382, 26% win) | -6.6% (3382, 26% win) | -10.5% (3382, 24% win) | -9.9% (3382, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.8% (4117, 23% win) | -6.4% (4117, 22% win) | -6.6% (4117, 22% win) |
| schoon | -6.4% (3283, 24% win) | -6.2% (3283, 24% win) | -6.1% (3283, 24% win) |
| bundelgrafiek | -8.1% (834, 16% win) | -7.0% (834, 16% win) | -8.7% (834, 15% win) |
| schoon+houders_ok | -6.9% (1244, 21% win) | -6.5% (1244, 20% win) | -6.1% (1244, 21% win) |
| schoon+houders_ok+final_stretch | -8.8% (499, 12% win) | -7.5% (499, 11% win) | -9.4% (499, 14% win) |
| volledige_screening+schoon | -9.8% (306, 11% win) | -8.6% (306, 10% win) | -10.5% (306, 15% win) |
| volledige_screening+schoon+x_link | -10.0% (233, 11% win) | -8.8% (233, 9% win) | -11.0% (233, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.9% (1752, 29% win); 1,3–2x: -8.2% (1531, 18% win); ≥ 2x (bundelgrafiek): -8.1% (834, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.8% (2655, 29% win); 5–20%: -8.7% (738, 13% win); ≥ 20%: -8.4% (724, 10% win)

**top t.o.v. start:** 2–3x: -6.3% (2309, 22% win); 3–6x: -7.0% (1409, 24% win); ≥ 6x: -8.3% (399, 22% win)

**unieke kopers tot de top:** < 30: -5.7% (2662, 29% win); 30–100: -7.5% (795, 11% win); ≥ 100: -10.1% (660, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.0% (1030, 16% win); 1–2: -5.9% (1966, 25% win); ≥ 3 (trap): -7.0% (1121, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.5% (991, 12% win); 10–25%: -7.1% (640, 12% win); ≥ 25%: -5.5% (2486, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.2% (3291, 25% win); 30 s–3 min: -8.5% (657, 15% win); ≥ 3 min (langzaam): -9.6% (169, 7% win)

**tijd van start tot top:** < 2 min: -6.5% (3430, 24% win); 2–10 min: -7.9% (549, 16% win); ≥ 10 min: -9.2% (138, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
