# Videostrategie op alle trades — 2026-09-14 03:18 UTC

Tokens sinds 2026-09-11 08:47 UTC: 54240 geschikt (≥ 2 uur oud, geen herstart), 42358 met trades, 7632 haalden 2x de startkoers, 5846 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1805 tokens. Houdercheck echt uitgevoerd bij 91% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1458, winkans 19%, EV per trade -7.2% (95%-marge -8.8% tot -5.6%), mediaan -10.6%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 4190, winkans 23%, EV -6.7% (95%-marge -8.4% tot -5.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 116, winkans 16%, EV -10.6% (95%-marge -14.2% tot -6.9%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 5846 | 40% | 77% | 37% |
| schoon | 4679 | 43% | 76% | 40% |
| bundelgrafiek | 1167 | 30% | 77% | 25% |
| schoon+houders_ok | 1458 | 37% | 80% | 24% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.4% (6252, 25% win) | -6.5% (6121, 24% win) | -6.7% (5987, 23% win) | -6.4% (5846, 23% win) | -7.0% (5717, 22% win) | -6.9% (5514, 21% win) | -6.4% (5125, 22% win) | -6.3% (4579, 23% win) | -5.7% (4057, 25% win) | -6.3% (3578, 25% win) | -6.9% (3110, 28% win) | -5.9% (4806, 27% win) |
| schoon | -6.4% (4999, 25% win) | -6.2% (4905, 25% win) | -6.5% (4801, 24% win) | -6.2% (4679, 24% win) | -6.4% (4575, 24% win) | -6.6% (4405, 23% win) | -5.9% (4063, 24% win) | -5.5% (3618, 26% win) | -5.1% (3233, 27% win) | -5.8% (2864, 27% win) | -6.7% (2532, 29% win) | -5.6% (4016, 27% win) |
| bundelgrafiek | -6.3% (1253, 24% win) | -7.5% (1216, 22% win) | -7.7% (1186, 19% win) | -7.4% (1167, 18% win) | -9.4% (1142, 15% win) | -8.1% (1109, 15% win) | -8.2% (1062, 15% win) | -9.1% (961, 15% win) | -7.8% (824, 18% win) | -8.3% (714, 18% win) | -7.7% (578, 20% win) | -7.4% (790, 24% win) |
| schoon+houders_ok | -6.6% (1131, 20% win) | -7.0% (1246, 20% win) | -7.2% (1370, 19% win) | -7.2% (1458, 19% win) | -7.0% (1557, 19% win) | -5.7% (1661, 19% win) | -5.2% (1713, 20% win) | -5.0% (1559, 21% win) | -4.4% (1414, 23% win) | -5.1% (1237, 24% win) | -5.5% (1081, 26% win) | -4.2% (1193, 23% win) |
| schoon+houders_ok+final_stretch | -7.1% (482, 17% win) | -7.3% (533, 15% win) | -8.0% (586, 12% win) | -8.6% (621, 12% win) | -8.5% (658, 10% win) | -7.5% (691, 10% win) | -7.0% (690, 10% win) | -6.7% (540, 10% win) | -7.0% (417, 9% win) | -6.9% (284, 9% win) | -4.8% (182, 12% win) | -5.7% (479, 15% win) |
| volledige_screening+schoon | -7.0% (339, 16% win) | -7.0% (361, 15% win) | -8.4% (380, 13% win) | -9.5% (402, 11% win) | -9.3% (419, 9% win) | -8.6% (425, 8% win) | -7.3% (413, 8% win) | -7.3% (323, 9% win) | -8.0% (244, 7% win) | -8.2% (174, 7% win) | -7.5% (111, 5% win) | -7.3% (293, 14% win) |
| volledige_screening+schoon+x_link | -7.4% (259, 17% win) | -6.0% (275, 18% win) | -8.4% (282, 14% win) | -9.4% (289, 12% win) | -9.4% (290, 9% win) | -9.1% (293, 8% win) | -8.4% (285, 7% win) | -8.5% (229, 7% win) | -7.9% (173, 6% win) | -8.6% (126, 6% win) | -8.1% (81, 2% win) | -7.1% (206, 14% win) |

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
| alle | -6.3% (6252, 30% win) | -6.5% (6121, 29% win) | -6.5% (5987, 28% win) | -6.4% (5846, 28% win) | -7.3% (5717, 26% win) | -6.8% (5514, 26% win) | -6.6% (5125, 27% win) | -6.4% (4579, 28% win) | -6.2% (4057, 31% win) | -6.5% (3578, 32% win) | -7.4% (3110, 33% win) |
| schoon | -6.3% (4999, 30% win) | -6.4% (4905, 30% win) | -6.5% (4801, 29% win) | -6.4% (4679, 29% win) | -7.1% (4575, 28% win) | -6.7% (4405, 28% win) | -6.4% (4063, 29% win) | -5.8% (3618, 31% win) | -5.6% (3233, 33% win) | -5.9% (2864, 34% win) | -6.9% (2532, 35% win) |
| bundelgrafiek | -6.2% (1253, 28% win) | -7.2% (1216, 25% win) | -6.6% (1186, 23% win) | -6.6% (1167, 22% win) | -7.9% (1142, 21% win) | -6.9% (1109, 20% win) | -7.4% (1062, 18% win) | -8.9% (961, 18% win) | -8.7% (824, 21% win) | -8.7% (714, 23% win) | -9.2% (578, 24% win) |
| schoon+houders_ok | -6.5% (1131, 27% win) | -6.6% (1246, 28% win) | -6.6% (1370, 27% win) | -7.0% (1458, 27% win) | -7.3% (1557, 26% win) | -6.0% (1661, 26% win) | -5.5% (1713, 26% win) | -5.2% (1559, 29% win) | -4.3% (1414, 32% win) | -4.9% (1237, 33% win) | -6.8% (1081, 34% win) |
| schoon+houders_ok+final_stretch | -6.9% (482, 25% win) | -7.2% (533, 24% win) | -7.4% (586, 23% win) | -9.2% (621, 21% win) | -10.3% (658, 17% win) | -9.3% (691, 18% win) | -7.4% (690, 20% win) | -7.5% (540, 22% win) | -7.6% (417, 24% win) | -6.9% (284, 27% win) | -5.7% (182, 27% win) |
| volledige_screening+schoon | -7.0% (339, 25% win) | -7.3% (361, 23% win) | -8.0% (380, 24% win) | -10.4% (402, 20% win) | -11.4% (419, 16% win) | -10.7% (425, 16% win) | -8.3% (413, 17% win) | -8.3% (323, 19% win) | -10.1% (244, 18% win) | -9.3% (174, 20% win) | -8.7% (111, 19% win) |
| volledige_screening+schoon+x_link | -7.0% (259, 26% win) | -6.5% (275, 25% win) | -8.1% (282, 23% win) | -10.7% (289, 19% win) | -11.9% (290, 14% win) | -10.4% (293, 16% win) | -8.0% (285, 17% win) | -8.2% (229, 18% win) | -9.0% (173, 19% win) | -9.0% (126, 20% win) | -8.6% (81, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 402 instappen, mediane hoogste stijging +8.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -7.8% | 26% |
| +15% | 43% | 20% | -7.9% | 22% |
| +20% | 40% | 18% | -7.8% | 19% |
| +25% | 34% | 15% | -8.3% | 17% |
| +30% | 32% | 13% | -8.4% | 15% |
| +35% | 29% | 12% | -8.4% | 14% |
| +45% | 24% | 8% | -9.5% | 11% |
| +60% | 20% | 7% | -9.2% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1458 instappen, mediane hoogste stijging +20.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 58% | 32% | -5.7% | 30% |
| +15% | 53% | 27% | -5.8% | 27% |
| +20% | 50% | 24% | -5.9% | 25% |
| +25% | 47% | 21% | -6.1% | 24% |
| +30% | 44% | 19% | -6.3% | 23% |
| +35% | 41% | 16% | -6.4% | 22% |
| +45% | 37% | 13% | -7.2% | 19% |
| +60% | 32% | 10% | -7.0% | 18% |

**filter `alle`** — variant `d45_direct`, 5846 instappen, mediane hoogste stijging +23.0%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.7% | 30% |
| +15% | 55% | 30% | -5.9% | 28% |
| +20% | 52% | 26% | -5.9% | 27% |
| +25% | 49% | 23% | -6.0% | 26% |
| +30% | 46% | 21% | -6.2% | 25% |
| +35% | 44% | 19% | -6.3% | 24% |
| +45% | 39% | 16% | -6.4% | 23% |
| +60% | 35% | 13% | -6.3% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.0% (339, 15% win) | -9.3% (339, 15% win) | -7.6% (339, 16% win) | -7.0% (339, 16% win) | -10.0% (339, 15% win) | -9.4% (339, 15% win) |
| d35_direct | -10.0% (361, 15% win) | -9.3% (361, 15% win) | -7.6% (361, 15% win) | -7.0% (361, 15% win) | -10.1% (361, 15% win) | -9.4% (361, 15% win) |
| d40_direct | -11.4% (380, 12% win) | -10.7% (380, 13% win) | -9.0% (380, 13% win) | -8.4% (380, 13% win) | -11.5% (380, 12% win) | -10.8% (380, 12% win) |
| d45_direct | -12.5% (402, 10% win) | -11.8% (402, 10% win) | -10.1% (402, 11% win) | -9.5% (402, 11% win) | -12.6% (402, 10% win) | -12.0% (402, 10% win) |
| d50_direct | -12.3% (419, 8% win) | -11.6% (419, 8% win) | -10.0% (419, 9% win) | -9.3% (419, 9% win) | -12.7% (419, 8% win) | -12.0% (419, 8% win) |
| d55_direct | -11.5% (425, 8% win) | -10.8% (425, 8% win) | -9.2% (425, 8% win) | -8.6% (425, 8% win) | -12.1% (425, 7% win) | -11.5% (425, 8% win) |
| d60_direct | -10.2% (413, 8% win) | -9.5% (413, 8% win) | -7.9% (413, 8% win) | -7.3% (413, 8% win) | -11.0% (413, 6% win) | -10.4% (413, 8% win) |
| d65_direct | -10.2% (323, 9% win) | -9.5% (323, 9% win) | -8.0% (323, 9% win) | -7.3% (323, 9% win) | -11.1% (323, 8% win) | -10.5% (323, 9% win) |
| d70_direct | -10.8% (244, 6% win) | -10.2% (244, 6% win) | -8.6% (244, 7% win) | -8.0% (244, 7% win) | -11.8% (244, 5% win) | -11.2% (244, 6% win) |
| d75_direct | -11.0% (174, 6% win) | -10.3% (174, 6% win) | -8.8% (174, 7% win) | -8.2% (174, 7% win) | -12.1% (174, 5% win) | -11.5% (174, 5% win) |
| d80_direct | -10.3% (111, 5% win) | -9.6% (111, 5% win) | -8.2% (111, 5% win) | -7.5% (111, 5% win) | -11.9% (111, 4% win) | -11.3% (111, 4% win) |
| d45_herstel5 | -10.3% (293, 14% win) | -9.6% (293, 14% win) | -7.9% (293, 14% win) | -7.3% (293, 14% win) | -10.3% (293, 14% win) | -9.7% (293, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (1131, 19% win) | -9.0% (1131, 19% win) | -7.2% (1131, 20% win) | -6.6% (1131, 20% win) | -9.3% (1131, 19% win) | -8.7% (1131, 20% win) |
| d35_direct | -10.1% (1246, 18% win) | -9.4% (1246, 18% win) | -7.6% (1246, 20% win) | -7.0% (1246, 20% win) | -9.8% (1246, 18% win) | -9.2% (1246, 19% win) |
| d40_direct | -10.3% (1370, 18% win) | -9.6% (1370, 18% win) | -7.9% (1370, 19% win) | -7.2% (1370, 19% win) | -10.2% (1370, 18% win) | -9.6% (1370, 18% win) |
| d45_direct | -10.2% (1458, 17% win) | -9.6% (1458, 18% win) | -7.9% (1458, 19% win) | -7.2% (1458, 19% win) | -10.3% (1458, 17% win) | -9.7% (1458, 18% win) |
| d50_direct | -10.0% (1557, 18% win) | -9.3% (1557, 18% win) | -7.6% (1557, 19% win) | -7.0% (1557, 19% win) | -10.2% (1557, 17% win) | -9.6% (1557, 18% win) |
| d55_direct | -8.7% (1661, 18% win) | -8.0% (1661, 18% win) | -6.4% (1661, 19% win) | -5.7% (1661, 19% win) | -9.2% (1661, 17% win) | -8.6% (1661, 18% win) |
| d60_direct | -8.1% (1713, 18% win) | -7.4% (1713, 19% win) | -5.9% (1713, 19% win) | -5.2% (1713, 20% win) | -8.9% (1713, 18% win) | -8.3% (1713, 18% win) |
| d65_direct | -7.9% (1559, 19% win) | -7.2% (1559, 20% win) | -5.7% (1559, 20% win) | -5.0% (1559, 21% win) | -9.0% (1559, 19% win) | -8.4% (1559, 19% win) |
| d70_direct | -7.1% (1414, 22% win) | -6.4% (1414, 22% win) | -5.1% (1414, 23% win) | -4.4% (1414, 23% win) | -8.8% (1414, 21% win) | -8.2% (1414, 22% win) |
| d75_direct | -7.7% (1237, 23% win) | -7.0% (1237, 23% win) | -5.8% (1237, 24% win) | -5.1% (1237, 24% win) | -10.1% (1237, 22% win) | -9.4% (1237, 22% win) |
| d80_direct | -7.9% (1081, 25% win) | -7.2% (1081, 26% win) | -6.2% (1081, 26% win) | -5.5% (1081, 26% win) | -11.6% (1081, 23% win) | -11.0% (1081, 23% win) |
| d45_herstel5 | -7.2% (1193, 22% win) | -6.5% (1193, 22% win) | -4.8% (1193, 23% win) | -4.2% (1193, 23% win) | -7.3% (1193, 22% win) | -6.6% (1193, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.4% (6252, 23% win) | -8.7% (6252, 24% win) | -7.1% (6252, 25% win) | -6.4% (6252, 25% win) | -9.6% (6252, 23% win) | -9.0% (6252, 24% win) |
| d35_direct | -9.5% (6121, 22% win) | -8.8% (6121, 23% win) | -7.2% (6121, 24% win) | -6.5% (6121, 24% win) | -9.8% (6121, 22% win) | -9.2% (6121, 23% win) |
| d40_direct | -9.7% (5987, 22% win) | -9.0% (5987, 22% win) | -7.4% (5987, 23% win) | -6.7% (5987, 23% win) | -10.3% (5987, 21% win) | -9.6% (5987, 22% win) |
| d45_direct | -9.3% (5846, 21% win) | -8.7% (5846, 22% win) | -7.1% (5846, 22% win) | -6.4% (5846, 23% win) | -10.2% (5846, 21% win) | -9.5% (5846, 21% win) |
| d50_direct | -9.9% (5717, 20% win) | -9.2% (5717, 21% win) | -7.7% (5717, 22% win) | -7.0% (5717, 22% win) | -10.9% (5717, 20% win) | -10.3% (5717, 20% win) |
| d55_direct | -9.7% (5514, 20% win) | -9.0% (5514, 20% win) | -7.5% (5514, 21% win) | -6.9% (5514, 21% win) | -11.0% (5514, 19% win) | -10.4% (5514, 19% win) |
| d60_direct | -9.1% (5125, 21% win) | -8.5% (5125, 21% win) | -7.1% (5125, 22% win) | -6.4% (5125, 22% win) | -10.8% (5125, 19% win) | -10.2% (5125, 20% win) |
| d65_direct | -8.9% (4579, 22% win) | -8.2% (4579, 22% win) | -7.0% (4579, 23% win) | -6.3% (4579, 23% win) | -11.1% (4579, 20% win) | -10.5% (4579, 21% win) |
| d70_direct | -8.2% (4057, 24% win) | -7.5% (4057, 24% win) | -6.3% (4057, 25% win) | -5.7% (4057, 25% win) | -11.2% (4057, 22% win) | -10.5% (4057, 23% win) |
| d75_direct | -8.6% (3578, 24% win) | -7.9% (3578, 24% win) | -7.0% (3578, 25% win) | -6.3% (3578, 25% win) | -12.6% (3578, 22% win) | -12.0% (3578, 22% win) |
| d80_direct | -8.8% (3110, 27% win) | -8.1% (3110, 27% win) | -7.5% (3110, 27% win) | -6.9% (3110, 28% win) | -14.6% (3110, 23% win) | -14.0% (3110, 23% win) |
| d45_herstel5 | -8.7% (4806, 25% win) | -8.0% (4806, 26% win) | -6.6% (4806, 26% win) | -5.9% (4806, 27% win) | -9.8% (4806, 24% win) | -9.2% (4806, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.4% (5846, 23% win) | -6.1% (5846, 22% win) | -6.5% (5846, 22% win) |
| schoon | -6.2% (4679, 24% win) | -6.0% (4679, 24% win) | -6.3% (4679, 23% win) |
| bundelgrafiek | -7.4% (1167, 18% win) | -6.7% (1167, 18% win) | -7.5% (1167, 16% win) |
| schoon+houders_ok | -7.2% (1458, 19% win) | -6.7% (1458, 19% win) | -6.5% (1458, 20% win) |
| schoon+houders_ok+final_stretch | -8.6% (621, 12% win) | -7.3% (621, 11% win) | -9.8% (621, 14% win) |
| volledige_screening+schoon | -9.5% (402, 11% win) | -8.2% (402, 9% win) | -11.3% (402, 14% win) |
| volledige_screening+schoon+x_link | -9.4% (289, 12% win) | -8.3% (289, 9% win) | -11.3% (289, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.4% (2513, 28% win); 1,3–2x: -7.1% (2165, 19% win); ≥ 2x (bundelgrafiek): -7.4% (1168, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.6% (3722, 29% win); 5–20%: -8.4% (1003, 14% win); ≥ 20%: -7.4% (1121, 12% win)

**top t.o.v. start:** 2–3x: -6.5% (3283, 22% win); 3–6x: -6.1% (2007, 24% win); ≥ 6x: -7.2% (556, 25% win)

**unieke kopers tot de top:** < 30: -5.6% (3706, 29% win); 30–100: -7.2% (1210, 12% win); ≥ 100: -8.7% (930, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.9% (1429, 16% win); 1–2: -6.1% (2808, 24% win); ≥ 3 (trap): -6.7% (1609, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.5% (1416, 13% win); 10–25%: -7.8% (950, 12% win); ≥ 25%: -5.2% (3480, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.8% (4609, 25% win); 30 s–3 min: -8.4% (981, 15% win); ≥ 3 min (langzaam): -10.3% (256, 7% win)

**tijd van start tot top:** < 2 min: -6.1% (4808, 24% win); 2–10 min: -7.5% (826, 16% win); ≥ 10 min: -10.3% (212, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
