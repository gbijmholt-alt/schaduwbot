# Videostrategie op alle trades — 2026-09-14 08:10 UTC

Tokens sinds 2026-09-11 08:47 UTC: 58915 geschikt (≥ 2 uur oud, geen herstart), 45931 met trades, 8235 haalden 2x de startkoers, 6320 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1926 tokens. Houdercheck echt uitgevoerd bij 92% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1512, winkans 19%, EV per trade -7.2% (95%-marge -8.8% tot -5.7%), mediaan -10.6%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 4598, winkans 23%, EV -6.5% (95%-marge -8.2% tot -4.9%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 141, winkans 18%, EV -9.6% (95%-marge -13.0% tot -6.1%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 6320 | 40% | 77% | 37% |
| schoon | 5087 | 42% | 76% | 40% |
| bundelgrafiek | 1233 | 31% | 77% | 25% |
| schoon+houders_ok | 1512 | 36% | 80% | 23% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.2% (6757, 25% win) | -6.4% (6612, 24% win) | -6.9% (6470, 23% win) | -6.4% (6320, 23% win) | -6.9% (6181, 22% win) | -6.8% (5959, 22% win) | -6.3% (5540, 22% win) | -6.3% (4943, 23% win) | -5.7% (4367, 25% win) | -6.3% (3860, 25% win) | -7.0% (3354, 28% win) | -5.8% (5222, 27% win) |
| schoon | -6.3% (5428, 26% win) | -6.1% (5326, 25% win) | -6.6% (5215, 24% win) | -6.2% (5087, 24% win) | -6.4% (4975, 24% win) | -6.6% (4788, 23% win) | -6.0% (4418, 24% win) | -5.7% (3931, 25% win) | -5.2% (3500, 27% win) | -5.9% (3108, 27% win) | -6.8% (2746, 29% win) | -5.7% (4381, 27% win) |
| bundelgrafiek | -6.0% (1329, 24% win) | -7.3% (1286, 22% win) | -7.9% (1255, 19% win) | -7.2% (1233, 18% win) | -8.9% (1206, 16% win) | -7.6% (1171, 16% win) | -7.9% (1122, 16% win) | -8.6% (1012, 16% win) | -7.6% (867, 18% win) | -8.3% (752, 18% win) | -8.0% (608, 20% win) | -6.2% (841, 25% win) |
| schoon+houders_ok | -6.6% (1157, 20% win) | -7.1% (1280, 20% win) | -7.3% (1417, 19% win) | -7.2% (1512, 19% win) | -7.0% (1626, 19% win) | -5.9% (1742, 19% win) | -5.2% (1802, 19% win) | -4.9% (1639, 21% win) | -4.4% (1473, 23% win) | -5.0% (1289, 24% win) | -5.5% (1120, 26% win) | -4.1% (1233, 23% win) |
| schoon+houders_ok+final_stretch | -7.3% (493, 16% win) | -7.5% (548, 14% win) | -8.0% (608, 12% win) | -8.4% (647, 12% win) | -8.4% (693, 10% win) | -7.4% (735, 10% win) | -6.9% (733, 9% win) | -6.6% (572, 10% win) | -7.0% (441, 9% win) | -7.0% (304, 9% win) | -5.1% (191, 12% win) | -5.7% (497, 16% win) |
| volledige_screening+schoon | -7.1% (347, 16% win) | -7.1% (373, 15% win) | -8.5% (396, 13% win) | -9.3% (420, 11% win) | -9.2% (442, 9% win) | -8.5% (450, 8% win) | -7.2% (438, 8% win) | -7.2% (341, 8% win) | -8.1% (256, 6% win) | -8.0% (184, 7% win) | -7.6% (114, 5% win) | -7.2% (306, 14% win) |
| volledige_screening+schoon+x_link | -7.6% (264, 17% win) | -6.0% (280, 18% win) | -8.3% (289, 14% win) | -9.3% (297, 12% win) | -9.2% (302, 10% win) | -8.8% (305, 8% win) | -8.3% (298, 7% win) | -8.3% (240, 7% win) | -8.0% (181, 6% win) | -8.3% (132, 6% win) | -8.1% (84, 2% win) | -7.2% (212, 14% win) |

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
| alle | -6.1% (6757, 30% win) | -6.4% (6612, 29% win) | -6.6% (6470, 28% win) | -6.4% (6320, 28% win) | -7.2% (6181, 26% win) | -6.8% (5959, 26% win) | -6.7% (5540, 27% win) | -6.4% (4943, 28% win) | -6.5% (4367, 31% win) | -6.9% (3860, 32% win) | -7.5% (3354, 33% win) |
| schoon | -6.2% (5428, 30% win) | -6.2% (5326, 30% win) | -6.5% (5215, 29% win) | -6.3% (5087, 29% win) | -7.2% (4975, 28% win) | -6.8% (4788, 28% win) | -6.6% (4418, 29% win) | -5.9% (3931, 31% win) | -5.9% (3500, 33% win) | -6.4% (3108, 34% win) | -7.0% (2746, 35% win) |
| bundelgrafiek | -5.9% (1329, 28% win) | -7.2% (1286, 25% win) | -6.9% (1255, 23% win) | -6.5% (1233, 22% win) | -7.5% (1206, 21% win) | -6.7% (1171, 20% win) | -7.2% (1122, 19% win) | -8.5% (1012, 19% win) | -8.7% (867, 21% win) | -8.9% (752, 23% win) | -9.4% (608, 25% win) |
| schoon+houders_ok | -6.7% (1157, 27% win) | -6.8% (1280, 27% win) | -6.6% (1417, 27% win) | -7.1% (1512, 27% win) | -7.4% (1626, 26% win) | -6.1% (1742, 26% win) | -5.7% (1802, 26% win) | -5.3% (1639, 28% win) | -4.6% (1473, 32% win) | -4.8% (1289, 33% win) | -6.7% (1120, 33% win) |
| schoon+houders_ok+final_stretch | -7.1% (493, 24% win) | -7.4% (548, 23% win) | -7.4% (608, 23% win) | -9.2% (647, 21% win) | -10.2% (693, 18% win) | -9.1% (735, 18% win) | -7.5% (733, 19% win) | -7.6% (572, 21% win) | -7.7% (441, 24% win) | -7.0% (304, 26% win) | -6.0% (191, 26% win) |
| volledige_screening+schoon | -7.2% (347, 25% win) | -7.5% (373, 23% win) | -8.0% (396, 24% win) | -10.5% (420, 20% win) | -11.3% (442, 16% win) | -10.4% (450, 17% win) | -8.2% (438, 18% win) | -8.4% (341, 19% win) | -10.1% (256, 19% win) | -9.4% (184, 20% win) | -8.8% (114, 18% win) |
| volledige_screening+schoon+x_link | -7.3% (264, 25% win) | -6.6% (280, 24% win) | -8.0% (289, 24% win) | -10.8% (297, 19% win) | -11.8% (302, 15% win) | -10.1% (305, 16% win) | -7.8% (298, 18% win) | -8.1% (240, 18% win) | -9.0% (181, 20% win) | -9.2% (132, 20% win) | -8.8% (84, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 420 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 47% | 24% | -7.9% | 25% |
| +15% | 42% | 20% | -8.0% | 21% |
| +20% | 39% | 17% | -7.9% | 19% |
| +25% | 34% | 14% | -8.3% | 17% |
| +30% | 31% | 13% | -8.4% | 15% |
| +35% | 29% | 12% | -8.4% | 14% |
| +45% | 24% | 8% | -9.3% | 11% |
| +60% | 20% | 7% | -9.2% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1512 instappen, mediane hoogste stijging +19.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.8% | 30% |
| +15% | 53% | 26% | -5.9% | 27% |
| +20% | 50% | 23% | -6.0% | 25% |
| +25% | 46% | 20% | -6.2% | 23% |
| +30% | 44% | 19% | -6.4% | 23% |
| +35% | 41% | 16% | -6.5% | 21% |
| +45% | 36% | 13% | -7.2% | 19% |
| +60% | 31% | 10% | -7.1% | 18% |

**filter `alle`** — variant `d45_direct`, 6320 instappen, mediane hoogste stijging +23.2%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.7% | 30% |
| +15% | 55% | 30% | -5.8% | 28% |
| +20% | 52% | 26% | -5.9% | 27% |
| +25% | 49% | 23% | -6.0% | 26% |
| +30% | 46% | 21% | -6.1% | 25% |
| +35% | 44% | 19% | -6.3% | 24% |
| +45% | 40% | 16% | -6.4% | 23% |
| +60% | 35% | 13% | -6.3% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.2% (347, 15% win) | -9.5% (347, 15% win) | -7.8% (347, 15% win) | -7.1% (347, 16% win) | -10.2% (347, 15% win) | -9.5% (347, 15% win) |
| d35_direct | -10.2% (373, 14% win) | -9.5% (373, 14% win) | -7.8% (373, 15% win) | -7.1% (373, 15% win) | -10.2% (373, 14% win) | -9.6% (373, 14% win) |
| d40_direct | -11.5% (396, 12% win) | -10.8% (396, 12% win) | -9.1% (396, 13% win) | -8.5% (396, 13% win) | -11.6% (396, 12% win) | -10.9% (396, 12% win) |
| d45_direct | -12.3% (420, 10% win) | -11.7% (420, 10% win) | -10.0% (420, 11% win) | -9.3% (420, 11% win) | -12.5% (420, 10% win) | -11.9% (420, 10% win) |
| d50_direct | -12.2% (442, 8% win) | -11.5% (442, 8% win) | -9.9% (442, 9% win) | -9.2% (442, 9% win) | -12.6% (442, 8% win) | -12.0% (442, 8% win) |
| d55_direct | -11.4% (450, 8% win) | -10.8% (450, 8% win) | -9.2% (450, 8% win) | -8.5% (450, 8% win) | -12.0% (450, 7% win) | -11.4% (450, 8% win) |
| d60_direct | -10.1% (438, 8% win) | -9.5% (438, 8% win) | -7.9% (438, 8% win) | -7.2% (438, 8% win) | -11.0% (438, 7% win) | -10.4% (438, 8% win) |
| d65_direct | -10.1% (341, 9% win) | -9.4% (341, 9% win) | -7.9% (341, 8% win) | -7.2% (341, 8% win) | -11.0% (341, 8% win) | -10.4% (341, 8% win) |
| d70_direct | -10.9% (256, 6% win) | -10.3% (256, 6% win) | -8.7% (256, 6% win) | -8.1% (256, 6% win) | -11.9% (256, 5% win) | -11.3% (256, 6% win) |
| d75_direct | -10.9% (184, 6% win) | -10.2% (184, 6% win) | -8.7% (184, 7% win) | -8.0% (184, 7% win) | -12.0% (184, 5% win) | -11.3% (184, 5% win) |
| d80_direct | -10.3% (114, 5% win) | -9.7% (114, 5% win) | -8.3% (114, 5% win) | -7.6% (114, 5% win) | -11.9% (114, 4% win) | -11.3% (114, 4% win) |
| d45_herstel5 | -10.2% (306, 14% win) | -9.5% (306, 14% win) | -7.8% (306, 14% win) | -7.2% (306, 14% win) | -10.3% (306, 14% win) | -9.6% (306, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (1157, 19% win) | -9.0% (1157, 19% win) | -7.3% (1157, 20% win) | -6.6% (1157, 20% win) | -9.3% (1157, 19% win) | -8.7% (1157, 20% win) |
| d35_direct | -10.2% (1280, 18% win) | -9.6% (1280, 18% win) | -7.8% (1280, 19% win) | -7.1% (1280, 20% win) | -10.0% (1280, 18% win) | -9.4% (1280, 19% win) |
| d40_direct | -10.4% (1417, 17% win) | -9.7% (1417, 18% win) | -8.0% (1417, 19% win) | -7.3% (1417, 19% win) | -10.3% (1417, 17% win) | -9.7% (1417, 18% win) |
| d45_direct | -10.3% (1512, 17% win) | -9.6% (1512, 17% win) | -7.9% (1512, 18% win) | -7.2% (1512, 19% win) | -10.4% (1512, 17% win) | -9.7% (1512, 18% win) |
| d50_direct | -10.0% (1626, 17% win) | -9.3% (1626, 18% win) | -7.6% (1626, 18% win) | -7.0% (1626, 19% win) | -10.2% (1626, 17% win) | -9.6% (1626, 18% win) |
| d55_direct | -8.9% (1742, 17% win) | -8.2% (1742, 18% win) | -6.6% (1742, 18% win) | -5.9% (1742, 19% win) | -9.4% (1742, 17% win) | -8.8% (1742, 17% win) |
| d60_direct | -8.1% (1802, 18% win) | -7.4% (1802, 18% win) | -5.9% (1802, 19% win) | -5.2% (1802, 19% win) | -9.0% (1802, 17% win) | -8.3% (1802, 18% win) |
| d65_direct | -7.8% (1639, 19% win) | -7.0% (1639, 20% win) | -5.6% (1639, 20% win) | -4.9% (1639, 21% win) | -8.9% (1639, 19% win) | -8.2% (1639, 19% win) |
| d70_direct | -7.2% (1473, 21% win) | -6.5% (1473, 22% win) | -5.1% (1473, 22% win) | -4.4% (1473, 23% win) | -8.8% (1473, 21% win) | -8.2% (1473, 21% win) |
| d75_direct | -7.6% (1289, 23% win) | -6.9% (1289, 23% win) | -5.7% (1289, 24% win) | -5.0% (1289, 24% win) | -10.0% (1289, 21% win) | -9.3% (1289, 22% win) |
| d80_direct | -7.9% (1120, 25% win) | -7.2% (1120, 25% win) | -6.2% (1120, 26% win) | -5.5% (1120, 26% win) | -11.5% (1120, 23% win) | -10.9% (1120, 23% win) |
| d45_herstel5 | -7.1% (1233, 22% win) | -6.4% (1233, 22% win) | -4.8% (1233, 23% win) | -4.1% (1233, 23% win) | -7.2% (1233, 22% win) | -6.6% (1233, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.2% (6757, 24% win) | -8.6% (6757, 24% win) | -6.9% (6757, 25% win) | -6.2% (6757, 25% win) | -9.5% (6757, 23% win) | -8.8% (6757, 24% win) |
| d35_direct | -9.3% (6612, 23% win) | -8.7% (6612, 23% win) | -7.0% (6612, 24% win) | -6.4% (6612, 24% win) | -9.7% (6612, 22% win) | -9.1% (6612, 23% win) |
| d40_direct | -9.8% (6470, 22% win) | -9.1% (6470, 22% win) | -7.5% (6470, 23% win) | -6.9% (6470, 23% win) | -10.4% (6470, 21% win) | -9.7% (6470, 21% win) |
| d45_direct | -9.3% (6320, 21% win) | -8.6% (6320, 22% win) | -7.1% (6320, 22% win) | -6.4% (6320, 23% win) | -10.1% (6320, 21% win) | -9.5% (6320, 21% win) |
| d50_direct | -9.8% (6181, 20% win) | -9.1% (6181, 21% win) | -7.6% (6181, 22% win) | -6.9% (6181, 22% win) | -10.8% (6181, 20% win) | -10.2% (6181, 20% win) |
| d55_direct | -9.6% (5959, 20% win) | -8.9% (5959, 20% win) | -7.5% (5959, 21% win) | -6.8% (5959, 22% win) | -11.0% (5959, 19% win) | -10.3% (5959, 19% win) |
| d60_direct | -9.1% (5540, 21% win) | -8.4% (5540, 21% win) | -7.0% (5540, 22% win) | -6.3% (5540, 22% win) | -10.8% (5540, 19% win) | -10.2% (5540, 20% win) |
| d65_direct | -8.9% (4943, 22% win) | -8.2% (4943, 22% win) | -7.0% (4943, 23% win) | -6.3% (4943, 23% win) | -11.2% (4943, 20% win) | -10.5% (4943, 21% win) |
| d70_direct | -8.2% (4367, 24% win) | -7.5% (4367, 24% win) | -6.4% (4367, 25% win) | -5.7% (4367, 25% win) | -11.2% (4367, 22% win) | -10.6% (4367, 23% win) |
| d75_direct | -8.6% (3860, 24% win) | -8.0% (3860, 25% win) | -7.0% (3860, 25% win) | -6.3% (3860, 25% win) | -12.6% (3860, 22% win) | -12.0% (3860, 22% win) |
| d80_direct | -8.9% (3354, 27% win) | -8.2% (3354, 27% win) | -7.7% (3354, 27% win) | -7.0% (3354, 28% win) | -14.7% (3354, 23% win) | -14.1% (3354, 23% win) |
| d45_herstel5 | -8.7% (5222, 25% win) | -8.0% (5222, 26% win) | -6.5% (5222, 26% win) | -5.8% (5222, 27% win) | -9.8% (5222, 24% win) | -9.1% (5222, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.4% (6320, 23% win) | -6.1% (6320, 22% win) | -6.4% (6320, 22% win) |
| schoon | -6.2% (5087, 24% win) | -6.0% (5087, 24% win) | -6.2% (5087, 23% win) |
| bundelgrafiek | -7.2% (1233, 18% win) | -6.6% (1233, 18% win) | -7.5% (1233, 16% win) |
| schoon+houders_ok | -7.2% (1512, 19% win) | -6.8% (1512, 18% win) | -6.8% (1512, 20% win) |
| schoon+houders_ok+final_stretch | -8.4% (647, 12% win) | -7.3% (647, 11% win) | -10.0% (647, 14% win) |
| volledige_screening+schoon | -9.3% (420, 11% win) | -8.4% (420, 9% win) | -11.5% (420, 14% win) |
| volledige_screening+schoon+x_link | -9.3% (297, 12% win) | -8.3% (297, 9% win) | -11.5% (297, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.5% (2721, 28% win); 1,3–2x: -7.0% (2365, 19% win); ≥ 2x (bundelgrafiek): -7.2% (1234, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.5% (4001, 29% win); 5–20%: -8.3% (1084, 14% win); ≥ 20%: -7.5% (1235, 11% win)

**top t.o.v. start:** 2–3x: -6.5% (3560, 22% win); 3–6x: -5.9% (2162, 24% win); ≥ 6x: -7.6% (598, 25% win)

**unieke kopers tot de top:** < 30: -5.6% (3995, 29% win); 30–100: -7.1% (1329, 12% win); ≥ 100: -8.8% (996, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.0% (1513, 16% win); 1–2: -6.1% (3048, 24% win); ≥ 3 (trap): -6.4% (1759, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.3% (1556, 13% win); 10–25%: -8.0% (1026, 12% win); ≥ 25%: -5.2% (3738, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.7% (4961, 26% win); 30 s–3 min: -8.6% (1085, 14% win); ≥ 3 min (langzaam): -10.1% (274, 7% win)

**tijd van start tot top:** < 2 min: -6.0% (5191, 25% win); 2–10 min: -7.7% (902, 16% win); ≥ 10 min: -10.8% (227, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
