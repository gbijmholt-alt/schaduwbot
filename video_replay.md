# Videostrategie op alle trades — 2026-09-13 15:06 UTC

Tokens sinds 2026-09-11 08:47 UTC: 39023 geschikt (≥ 2 uur oud, geen herstart), 31016 met trades, 5830 haalden 2x de startkoers, 4428 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1367 tokens. Houdercheck echt uitgevoerd bij 89% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1298, winkans 20%, EV per trade -7.2% (95%-marge -8.9% tot -5.4%), mediaan -10.7%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 3069, winkans 24%, EV -6.9% (95%-marge -8.8% tot -5.1%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 32, winkans 12%, EV -10.9% (95%-marge -16.9% tot -4.9%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4428 | 40% | 76% | 37% |
| schoon | 3558 | 42% | 76% | 40% |
| bundelgrafiek | 870 | 29% | 78% | 25% |
| schoon+houders_ok | 1298 | 37% | 79% | 26% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.2% (4743, 25% win) | -6.3% (4642, 24% win) | -6.7% (4539, 23% win) | -6.6% (4428, 23% win) | -7.0% (4331, 22% win) | -6.9% (4172, 21% win) | -6.4% (3873, 22% win) | -6.3% (3452, 23% win) | -5.6% (3054, 25% win) | -6.7% (2691, 25% win) | -7.0% (2340, 27% win) | -6.4% (3630, 26% win) |
| schoon | -6.0% (3813, 26% win) | -5.8% (3739, 26% win) | -6.3% (3655, 25% win) | -6.3% (3558, 24% win) | -6.5% (3484, 24% win) | -6.8% (3350, 23% win) | -6.1% (3083, 24% win) | -5.5% (2741, 26% win) | -5.1% (2451, 27% win) | -6.2% (2169, 27% win) | -6.6% (1914, 29% win) | -6.0% (3046, 27% win) |
| bundelgrafiek | -7.0% (930, 22% win) | -8.3% (903, 19% win) | -8.5% (884, 17% win) | -8.0% (870, 16% win) | -9.3% (847, 15% win) | -7.5% (822, 15% win) | -7.6% (790, 15% win) | -9.4% (711, 15% win) | -8.0% (603, 18% win) | -8.7% (522, 18% win) | -8.8% (426, 19% win) | -8.9% (584, 22% win) |
| schoon+houders_ok | -6.4% (1034, 21% win) | -6.7% (1134, 21% win) | -7.1% (1229, 20% win) | -7.2% (1298, 20% win) | -6.9% (1384, 20% win) | -5.7% (1466, 20% win) | -5.2% (1498, 21% win) | -4.6% (1360, 22% win) | -4.0% (1231, 25% win) | -5.2% (1080, 26% win) | -5.3% (956, 28% win) | -4.3% (1077, 24% win) |
| schoon+houders_ok+final_stretch | -7.2% (435, 17% win) | -7.2% (475, 15% win) | -8.1% (508, 13% win) | -9.2% (532, 12% win) | -8.8% (553, 10% win) | -7.9% (576, 9% win) | -6.9% (563, 10% win) | -6.1% (436, 11% win) | -7.6% (326, 9% win) | -7.8% (215, 8% win) | -5.6% (130, 12% win) | -6.3% (413, 15% win) |
| volledige_screening+schoon | -7.2% (301, 16% win) | -6.6% (314, 16% win) | -8.6% (321, 13% win) | -10.3% (333, 10% win) | -10.0% (339, 9% win) | -8.9% (341, 8% win) | -7.2% (329, 8% win) | -7.0% (259, 9% win) | -8.6% (194, 6% win) | -9.0% (132, 7% win) | -9.2% (81, 4% win) | -8.0% (246, 13% win) |
| volledige_screening+schoon+x_link | -7.8% (235, 17% win) | -5.7% (245, 19% win) | -9.0% (247, 14% win) | -10.4% (251, 10% win) | -10.2% (250, 8% win) | -9.7% (251, 7% win) | -8.8% (245, 6% win) | -8.4% (192, 7% win) | -8.7% (146, 5% win) | -8.9% (103, 6% win) | -8.8% (65, 2% win) | -8.3% (179, 12% win) |

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
| alle | -5.8% (4743, 30% win) | -5.8% (4642, 29% win) | -6.1% (4539, 28% win) | -6.4% (4428, 28% win) | -7.3% (4331, 26% win) | -6.8% (4172, 26% win) | -6.5% (3873, 27% win) | -6.7% (3452, 28% win) | -6.3% (3054, 31% win) | -6.6% (2691, 32% win) | -7.6% (2340, 33% win) |
| schoon | -5.6% (3813, 31% win) | -5.4% (3739, 30% win) | -5.9% (3655, 30% win) | -6.1% (3558, 29% win) | -7.2% (3484, 27% win) | -6.9% (3350, 27% win) | -6.3% (3083, 29% win) | -6.2% (2741, 31% win) | -5.8% (2451, 33% win) | -6.0% (2169, 34% win) | -7.0% (1914, 35% win) |
| bundelgrafiek | -6.5% (930, 26% win) | -7.4% (903, 24% win) | -7.1% (884, 22% win) | -7.3% (870, 20% win) | -7.8% (847, 20% win) | -6.5% (822, 20% win) | -7.0% (790, 18% win) | -8.6% (711, 17% win) | -8.5% (603, 20% win) | -9.2% (522, 22% win) | -10.7% (426, 24% win) |
| schoon+houders_ok | -6.4% (1034, 28% win) | -6.3% (1134, 28% win) | -6.4% (1229, 28% win) | -6.9% (1298, 28% win) | -7.2% (1384, 27% win) | -5.8% (1466, 27% win) | -5.0% (1498, 27% win) | -4.9% (1360, 30% win) | -4.0% (1231, 33% win) | -4.7% (1080, 34% win) | -6.8% (956, 34% win) |
| schoon+houders_ok+final_stretch | -6.9% (435, 24% win) | -6.8% (475, 24% win) | -7.1% (508, 24% win) | -9.2% (532, 21% win) | -10.4% (553, 17% win) | -9.4% (576, 18% win) | -6.3% (563, 21% win) | -6.7% (436, 22% win) | -8.5% (326, 23% win) | -7.9% (215, 25% win) | -7.2% (130, 25% win) |
| volledige_screening+schoon | -6.9% (301, 25% win) | -6.7% (314, 24% win) | -7.7% (321, 25% win) | -10.6% (333, 20% win) | -11.6% (339, 16% win) | -10.8% (341, 16% win) | -7.2% (329, 19% win) | -8.1% (259, 19% win) | -11.4% (194, 16% win) | -10.9% (132, 17% win) | -12.9% (81, 12% win) |
| volledige_screening+schoon+x_link | -7.1% (235, 26% win) | -6.0% (245, 26% win) | -7.8% (247, 24% win) | -11.1% (251, 19% win) | -12.3% (250, 14% win) | -11.1% (251, 14% win) | -7.7% (245, 17% win) | -8.1% (192, 18% win) | -10.0% (146, 17% win) | -11.1% (103, 16% win) | -13.0% (65, 9% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 333 instappen, mediane hoogste stijging +8.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 47% | 23% | -8.4% | 25% |
| +15% | 41% | 19% | -8.6% | 21% |
| +20% | 38% | 16% | -8.6% | 18% |
| +25% | 33% | 13% | -9.1% | 16% |
| +30% | 31% | 12% | -9.3% | 14% |
| +35% | 28% | 11% | -9.4% | 13% |
| +45% | 24% | 8% | -10.3% | 10% |
| +60% | 20% | 6% | -10.2% | 9% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1298 instappen, mediane hoogste stijging +20.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 33% | -5.5% | 30% |
| +15% | 54% | 27% | -5.7% | 28% |
| +20% | 51% | 24% | -5.8% | 26% |
| +25% | 47% | 21% | -6.0% | 24% |
| +30% | 45% | 20% | -6.2% | 23% |
| +35% | 42% | 17% | -6.4% | 22% |
| +45% | 37% | 14% | -7.2% | 20% |
| +60% | 32% | 11% | -7.0% | 19% |

**filter `alle`** — variant `d45_direct`, 4428 instappen, mediane hoogste stijging +22.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.8% | 30% |
| +15% | 55% | 30% | -6.1% | 28% |
| +20% | 52% | 27% | -6.2% | 26% |
| +25% | 48% | 24% | -6.2% | 26% |
| +30% | 46% | 21% | -6.4% | 25% |
| +35% | 43% | 19% | -6.5% | 24% |
| +45% | 39% | 16% | -6.6% | 23% |
| +60% | 35% | 13% | -6.5% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.3% (301, 15% win) | -9.6% (301, 15% win) | -7.9% (301, 15% win) | -7.2% (301, 16% win) | -10.3% (301, 15% win) | -9.7% (301, 15% win) |
| d35_direct | -9.7% (314, 15% win) | -9.0% (314, 15% win) | -7.3% (314, 16% win) | -6.6% (314, 16% win) | -9.8% (314, 15% win) | -9.1% (314, 15% win) |
| d40_direct | -11.7% (321, 13% win) | -11.0% (321, 13% win) | -9.3% (321, 13% win) | -8.6% (321, 13% win) | -11.8% (321, 12% win) | -11.1% (321, 12% win) |
| d45_direct | -13.3% (333, 10% win) | -12.7% (333, 10% win) | -11.0% (333, 10% win) | -10.3% (333, 10% win) | -13.5% (333, 9% win) | -12.9% (333, 9% win) |
| d50_direct | -13.0% (339, 8% win) | -12.3% (339, 8% win) | -10.7% (339, 9% win) | -10.0% (339, 9% win) | -13.4% (339, 8% win) | -12.7% (339, 8% win) |
| d55_direct | -11.9% (341, 7% win) | -11.2% (341, 8% win) | -9.6% (341, 8% win) | -8.9% (341, 8% win) | -12.4% (341, 7% win) | -11.8% (341, 7% win) |
| d60_direct | -10.1% (329, 8% win) | -9.4% (329, 8% win) | -7.9% (329, 8% win) | -7.2% (329, 8% win) | -11.0% (329, 7% win) | -10.4% (329, 8% win) |
| d65_direct | -9.9% (259, 10% win) | -9.2% (259, 10% win) | -7.7% (259, 9% win) | -7.0% (259, 9% win) | -10.9% (259, 8% win) | -10.3% (259, 9% win) |
| d70_direct | -11.5% (194, 6% win) | -10.8% (194, 6% win) | -9.3% (194, 6% win) | -8.6% (194, 6% win) | -12.4% (194, 5% win) | -11.8% (194, 5% win) |
| d75_direct | -11.8% (132, 5% win) | -11.1% (132, 5% win) | -9.7% (132, 7% win) | -9.0% (132, 7% win) | -13.0% (132, 4% win) | -12.4% (132, 4% win) |
| d80_direct | -11.9% (81, 4% win) | -11.2% (81, 4% win) | -9.9% (81, 4% win) | -9.2% (81, 4% win) | -13.7% (81, 2% win) | -13.1% (81, 2% win) |
| d45_herstel5 | -11.0% (246, 13% win) | -10.3% (246, 13% win) | -8.6% (246, 13% win) | -8.0% (246, 13% win) | -11.0% (246, 13% win) | -10.4% (246, 13% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.5% (1034, 19% win) | -8.8% (1034, 20% win) | -7.0% (1034, 21% win) | -6.4% (1034, 21% win) | -9.1% (1034, 20% win) | -8.5% (1034, 20% win) |
| d35_direct | -9.8% (1134, 19% win) | -9.1% (1134, 19% win) | -7.4% (1134, 20% win) | -6.7% (1134, 21% win) | -9.6% (1134, 19% win) | -8.9% (1134, 20% win) |
| d40_direct | -10.2% (1229, 18% win) | -9.5% (1229, 19% win) | -7.8% (1229, 20% win) | -7.1% (1229, 20% win) | -10.1% (1229, 18% win) | -9.5% (1229, 19% win) |
| d45_direct | -10.2% (1298, 18% win) | -9.5% (1298, 18% win) | -7.8% (1298, 19% win) | -7.2% (1298, 20% win) | -10.3% (1298, 18% win) | -9.6% (1298, 18% win) |
| d50_direct | -9.9% (1384, 18% win) | -9.3% (1384, 19% win) | -7.6% (1384, 20% win) | -6.9% (1384, 20% win) | -10.2% (1384, 18% win) | -9.6% (1384, 18% win) |
| d55_direct | -8.6% (1466, 18% win) | -8.0% (1466, 19% win) | -6.4% (1466, 20% win) | -5.7% (1466, 20% win) | -9.2% (1466, 18% win) | -8.6% (1466, 18% win) |
| d60_direct | -8.1% (1498, 19% win) | -7.4% (1498, 20% win) | -5.9% (1498, 20% win) | -5.2% (1498, 21% win) | -9.0% (1498, 19% win) | -8.4% (1498, 19% win) |
| d65_direct | -7.4% (1360, 21% win) | -6.7% (1360, 21% win) | -5.3% (1360, 22% win) | -4.6% (1360, 22% win) | -8.6% (1360, 20% win) | -8.0% (1360, 21% win) |
| d70_direct | -6.8% (1231, 23% win) | -6.1% (1231, 24% win) | -4.7% (1231, 24% win) | -4.0% (1231, 25% win) | -8.6% (1231, 23% win) | -7.9% (1231, 23% win) |
| d75_direct | -7.8% (1080, 24% win) | -7.1% (1080, 25% win) | -5.8% (1080, 25% win) | -5.2% (1080, 26% win) | -10.3% (1080, 23% win) | -9.7% (1080, 23% win) |
| d80_direct | -7.6% (956, 27% win) | -6.9% (956, 27% win) | -6.0% (956, 28% win) | -5.3% (956, 28% win) | -11.6% (956, 24% win) | -11.0% (956, 24% win) |
| d45_herstel5 | -7.4% (1077, 22% win) | -6.7% (1077, 22% win) | -5.0% (1077, 23% win) | -4.3% (1077, 24% win) | -7.5% (1077, 22% win) | -6.8% (1077, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.2% (4743, 23% win) | -8.6% (4743, 24% win) | -6.9% (4743, 25% win) | -6.2% (4743, 25% win) | -9.5% (4743, 23% win) | -8.8% (4743, 24% win) |
| d35_direct | -9.3% (4642, 23% win) | -8.6% (4642, 23% win) | -7.0% (4642, 24% win) | -6.3% (4642, 24% win) | -9.7% (4642, 22% win) | -9.1% (4642, 23% win) |
| d40_direct | -9.6% (4539, 22% win) | -8.9% (4539, 22% win) | -7.4% (4539, 23% win) | -6.7% (4539, 23% win) | -10.2% (4539, 21% win) | -9.6% (4539, 22% win) |
| d45_direct | -9.5% (4428, 21% win) | -8.8% (4428, 21% win) | -7.3% (4428, 22% win) | -6.6% (4428, 23% win) | -10.3% (4428, 20% win) | -9.7% (4428, 21% win) |
| d50_direct | -9.9% (4331, 20% win) | -9.2% (4331, 21% win) | -7.7% (4331, 22% win) | -7.0% (4331, 22% win) | -10.9% (4331, 20% win) | -10.3% (4331, 20% win) |
| d55_direct | -9.7% (4172, 20% win) | -9.0% (4172, 20% win) | -7.6% (4172, 21% win) | -6.9% (4172, 21% win) | -11.0% (4172, 19% win) | -10.4% (4172, 19% win) |
| d60_direct | -9.2% (3873, 21% win) | -8.5% (3873, 21% win) | -7.1% (3873, 22% win) | -6.4% (3873, 22% win) | -10.9% (3873, 19% win) | -10.2% (3873, 20% win) |
| d65_direct | -8.9% (3452, 22% win) | -8.3% (3452, 22% win) | -7.0% (3452, 23% win) | -6.3% (3452, 23% win) | -11.2% (3452, 20% win) | -10.5% (3452, 21% win) |
| d70_direct | -8.1% (3054, 24% win) | -7.4% (3054, 25% win) | -6.3% (3054, 25% win) | -5.6% (3054, 25% win) | -11.2% (3054, 22% win) | -10.6% (3054, 23% win) |
| d75_direct | -9.0% (2691, 24% win) | -8.3% (2691, 24% win) | -7.3% (2691, 24% win) | -6.7% (2691, 25% win) | -13.0% (2691, 21% win) | -12.4% (2691, 21% win) |
| d80_direct | -8.9% (2340, 26% win) | -8.2% (2340, 27% win) | -7.7% (2340, 27% win) | -7.0% (2340, 27% win) | -14.8% (2340, 22% win) | -14.2% (2340, 22% win) |
| d45_herstel5 | -9.3% (3630, 25% win) | -8.6% (3630, 25% win) | -7.1% (3630, 26% win) | -6.4% (3630, 26% win) | -10.4% (3630, 24% win) | -9.7% (3630, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.6% (4428, 23% win) | -6.2% (4428, 22% win) | -6.8% (4428, 22% win) |
| schoon | -6.3% (3558, 24% win) | -6.1% (3558, 24% win) | -6.4% (3558, 24% win) |
| bundelgrafiek | -8.0% (870, 16% win) | -7.0% (870, 16% win) | -8.8% (870, 15% win) |
| schoon+houders_ok | -7.2% (1298, 20% win) | -6.7% (1298, 20% win) | -6.3% (1298, 20% win) |
| schoon+houders_ok+final_stretch | -9.2% (532, 12% win) | -7.8% (532, 11% win) | -9.9% (532, 14% win) |
| volledige_screening+schoon | -10.3% (333, 10% win) | -9.1% (333, 9% win) | -11.2% (333, 14% win) |
| volledige_screening+schoon+x_link | -10.4% (251, 10% win) | -9.1% (251, 8% win) | -11.5% (251, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.9% (1899, 29% win); 1,3–2x: -7.9% (1659, 18% win); ≥ 2x (bundelgrafiek): -8.0% (870, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.5% (2845, 29% win); 5–20%: -8.8% (797, 13% win); ≥ 20%: -8.4% (786, 10% win)

**top t.o.v. start:** 2–3x: -6.2% (2487, 22% win); 3–6x: -6.8% (1520, 24% win); ≥ 6x: -8.5% (421, 22% win)

**unieke kopers tot de top:** < 30: -5.4% (2843, 29% win); 30–100: -7.6% (877, 11% win); ≥ 100: -10.1% (708, 11% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.8% (1099, 15% win); 1–2: -5.9% (2101, 25% win); ≥ 3 (trap): -6.8% (1228, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.4% (1079, 11% win); 10–25%: -7.4% (701, 12% win); ≥ 25%: -5.3% (2648, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (3526, 25% win); 30 s–3 min: -8.8% (710, 15% win); ≥ 3 min (langzaam): -10.1% (192, 7% win)

**tijd van start tot top:** < 2 min: -6.4% (3670, 24% win); 2–10 min: -7.4% (606, 16% win); ≥ 10 min: -8.9% (152, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
