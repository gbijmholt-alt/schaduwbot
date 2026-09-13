# Videostrategie op alle trades — 2026-09-13 17:51 UTC

Tokens sinds 2026-09-11 08:47 UTC: 42034 geschikt (≥ 2 uur oud, geen herstart), 33126 met trades, 6150 haalden 2x de startkoers, 4686 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1441 tokens. Houdercheck echt uitgevoerd bij 90% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1338, winkans 20%, EV per trade -7.1% (95%-marge -8.8% tot -5.4%), mediaan -10.6%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 3276, winkans 24%, EV -7.2% (95%-marge -9.0% tot -5.4%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 53, winkans 19%, EV -10.3% (95%-marge -15.7% tot -4.8%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4686 | 40% | 77% | 37% |
| schoon | 3765 | 42% | 76% | 40% |
| bundelgrafiek | 921 | 29% | 78% | 24% |
| schoon+houders_ok | 1338 | 37% | 80% | 25% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.3% (5015, 25% win) | -6.6% (4911, 24% win) | -6.8% (4803, 23% win) | -6.6% (4686, 23% win) | -7.0% (4585, 22% win) | -7.0% (4420, 21% win) | -6.4% (4110, 22% win) | -6.4% (3669, 24% win) | -5.8% (3246, 26% win) | -6.6% (2862, 25% win) | -6.9% (2491, 27% win) | -6.4% (3845, 27% win) |
| schoon | -6.2% (4032, 26% win) | -6.2% (3956, 25% win) | -6.6% (3867, 25% win) | -6.4% (3765, 24% win) | -6.6% (3687, 24% win) | -6.9% (3548, 23% win) | -6.2% (3271, 24% win) | -5.7% (2917, 26% win) | -5.3% (2608, 28% win) | -6.2% (2314, 27% win) | -6.7% (2044, 29% win) | -6.1% (3233, 27% win) |
| bundelgrafiek | -6.6% (983, 23% win) | -8.3% (955, 19% win) | -8.0% (936, 18% win) | -7.5% (921, 17% win) | -9.0% (898, 15% win) | -7.2% (872, 15% win) | -7.4% (839, 16% win) | -9.2% (752, 15% win) | -7.8% (638, 18% win) | -8.2% (548, 18% win) | -7.6% (447, 19% win) | -8.4% (612, 23% win) |
| schoon+houders_ok | -6.4% (1068, 21% win) | -6.7% (1169, 21% win) | -7.1% (1269, 20% win) | -7.1% (1338, 20% win) | -7.0% (1427, 20% win) | -5.7% (1514, 20% win) | -5.2% (1547, 20% win) | -4.7% (1408, 22% win) | -4.1% (1269, 24% win) | -5.3% (1115, 25% win) | -5.4% (982, 28% win) | -4.4% (1109, 23% win) |
| schoon+houders_ok+final_stretch | -7.2% (454, 17% win) | -7.1% (494, 15% win) | -8.0% (531, 13% win) | -8.9% (556, 12% win) | -8.8% (579, 10% win) | -7.8% (604, 10% win) | -6.8% (592, 10% win) | -6.3% (462, 11% win) | -7.8% (344, 8% win) | -7.9% (230, 8% win) | -5.1% (141, 12% win) | -6.0% (434, 15% win) |
| volledige_screening+schoon | -7.2% (316, 16% win) | -6.8% (329, 16% win) | -8.6% (337, 13% win) | -9.9% (350, 11% win) | -9.9% (358, 9% win) | -8.8% (362, 8% win) | -7.2% (350, 8% win) | -7.2% (275, 9% win) | -8.8% (204, 6% win) | -9.1% (141, 6% win) | -8.0% (89, 6% win) | -7.3% (260, 14% win) |
| volledige_screening+schoon+x_link | -7.8% (245, 17% win) | -5.8% (255, 19% win) | -8.8% (257, 14% win) | -10.0% (261, 11% win) | -10.1% (260, 8% win) | -9.7% (263, 7% win) | -8.6% (258, 7% win) | -8.3% (204, 7% win) | -8.9% (153, 5% win) | -9.0% (110, 6% win) | -9.0% (70, 1% win) | -7.6% (188, 14% win) |

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
| alle | -5.8% (5015, 30% win) | -6.1% (4911, 29% win) | -6.2% (4803, 28% win) | -6.5% (4686, 28% win) | -7.3% (4585, 26% win) | -7.0% (4420, 26% win) | -6.6% (4110, 27% win) | -6.9% (3669, 28% win) | -6.6% (3246, 31% win) | -6.7% (2862, 32% win) | -7.6% (2491, 33% win) |
| schoon | -5.7% (4032, 31% win) | -5.8% (3956, 30% win) | -6.1% (3867, 30% win) | -6.3% (3765, 29% win) | -7.2% (3687, 27% win) | -7.1% (3548, 27% win) | -6.6% (3271, 29% win) | -6.4% (2917, 31% win) | -6.2% (2608, 33% win) | -6.3% (2314, 34% win) | -7.1% (2044, 35% win) |
| bundelgrafiek | -6.3% (983, 26% win) | -7.5% (955, 24% win) | -6.7% (936, 22% win) | -7.0% (921, 20% win) | -7.5% (898, 20% win) | -6.3% (872, 20% win) | -6.9% (839, 18% win) | -8.5% (752, 17% win) | -8.2% (638, 20% win) | -8.6% (548, 22% win) | -9.8% (447, 24% win) |
| schoon+houders_ok | -6.4% (1068, 28% win) | -6.4% (1169, 28% win) | -6.4% (1269, 28% win) | -6.9% (1338, 28% win) | -7.3% (1427, 26% win) | -6.0% (1514, 27% win) | -5.1% (1547, 28% win) | -5.0% (1408, 30% win) | -4.2% (1269, 33% win) | -4.9% (1115, 34% win) | -6.8% (982, 34% win) |
| schoon+houders_ok+final_stretch | -6.8% (454, 25% win) | -6.7% (494, 24% win) | -6.9% (531, 24% win) | -8.9% (556, 21% win) | -10.4% (579, 17% win) | -9.4% (604, 18% win) | -6.6% (592, 21% win) | -7.1% (462, 22% win) | -8.8% (344, 22% win) | -7.5% (230, 25% win) | -5.8% (141, 26% win) |
| volledige_screening+schoon | -6.9% (316, 25% win) | -6.9% (329, 24% win) | -7.6% (337, 25% win) | -10.2% (350, 21% win) | -11.6% (358, 16% win) | -10.7% (362, 17% win) | -7.6% (350, 19% win) | -8.2% (275, 19% win) | -11.6% (204, 16% win) | -10.4% (141, 18% win) | -9.9% (89, 17% win) |
| volledige_screening+schoon+x_link | -7.2% (245, 26% win) | -6.3% (255, 26% win) | -7.6% (257, 24% win) | -10.7% (261, 20% win) | -12.4% (260, 14% win) | -11.1% (263, 15% win) | -7.7% (258, 18% win) | -8.0% (204, 18% win) | -10.1% (153, 18% win) | -10.3% (110, 18% win) | -11.2% (70, 13% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 350 instappen, mediane hoogste stijging +8.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -8.0% | 26% |
| +15% | 43% | 20% | -8.1% | 22% |
| +20% | 39% | 17% | -8.1% | 19% |
| +25% | 34% | 15% | -8.6% | 17% |
| +30% | 32% | 13% | -8.6% | 16% |
| +35% | 29% | 12% | -8.7% | 15% |
| +45% | 24% | 8% | -9.9% | 11% |
| +60% | 20% | 7% | -9.8% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1338 instappen, mediane hoogste stijging +20.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 33% | -5.4% | 31% |
| +15% | 54% | 27% | -5.6% | 28% |
| +20% | 51% | 24% | -5.7% | 26% |
| +25% | 47% | 21% | -6.0% | 24% |
| +30% | 45% | 20% | -6.1% | 24% |
| +35% | 41% | 17% | -6.3% | 22% |
| +45% | 37% | 13% | -7.1% | 20% |
| +60% | 32% | 11% | -7.0% | 19% |

**filter `alle`** — variant `d45_direct`, 4686 instappen, mediane hoogste stijging +22.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.9% | 30% |
| +15% | 55% | 30% | -6.1% | 28% |
| +20% | 52% | 27% | -6.2% | 27% |
| +25% | 49% | 24% | -6.2% | 26% |
| +30% | 46% | 21% | -6.4% | 25% |
| +35% | 43% | 19% | -6.5% | 24% |
| +45% | 39% | 16% | -6.6% | 23% |
| +60% | 35% | 13% | -6.5% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.2% (316, 15% win) | -9.5% (316, 15% win) | -7.8% (316, 16% win) | -7.2% (316, 16% win) | -10.2% (316, 15% win) | -9.6% (316, 15% win) |
| d35_direct | -9.9% (329, 15% win) | -9.2% (329, 15% win) | -7.5% (329, 16% win) | -6.8% (329, 16% win) | -9.9% (329, 15% win) | -9.3% (329, 15% win) |
| d40_direct | -11.6% (337, 13% win) | -10.9% (337, 13% win) | -9.2% (337, 13% win) | -8.6% (337, 13% win) | -11.7% (337, 12% win) | -11.1% (337, 12% win) |
| d45_direct | -12.9% (350, 10% win) | -12.2% (350, 10% win) | -10.5% (350, 11% win) | -9.9% (350, 11% win) | -13.0% (350, 10% win) | -12.4% (350, 10% win) |
| d50_direct | -12.9% (358, 8% win) | -12.2% (358, 8% win) | -10.5% (358, 9% win) | -9.9% (358, 9% win) | -13.2% (358, 8% win) | -12.6% (358, 8% win) |
| d55_direct | -11.7% (362, 8% win) | -11.1% (362, 8% win) | -9.4% (362, 8% win) | -8.8% (362, 8% win) | -12.3% (362, 7% win) | -11.7% (362, 8% win) |
| d60_direct | -10.1% (350, 8% win) | -9.4% (350, 8% win) | -7.9% (350, 8% win) | -7.2% (350, 8% win) | -11.0% (350, 7% win) | -10.3% (350, 8% win) |
| d65_direct | -10.1% (275, 10% win) | -9.4% (275, 10% win) | -7.8% (275, 9% win) | -7.2% (275, 9% win) | -11.0% (275, 8% win) | -10.4% (275, 9% win) |
| d70_direct | -11.6% (204, 5% win) | -11.0% (204, 5% win) | -9.4% (204, 6% win) | -8.8% (204, 6% win) | -12.6% (204, 4% win) | -11.9% (204, 5% win) |
| d75_direct | -11.9% (141, 5% win) | -11.2% (141, 5% win) | -9.7% (141, 6% win) | -9.1% (141, 6% win) | -13.0% (141, 4% win) | -12.4% (141, 4% win) |
| d80_direct | -10.7% (89, 6% win) | -10.0% (89, 6% win) | -8.7% (89, 6% win) | -8.0% (89, 6% win) | -12.4% (89, 4% win) | -11.8% (89, 4% win) |
| d45_herstel5 | -10.3% (260, 14% win) | -9.6% (260, 14% win) | -8.0% (260, 14% win) | -7.3% (260, 14% win) | -10.4% (260, 14% win) | -9.7% (260, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.5% (1068, 19% win) | -8.8% (1068, 20% win) | -7.1% (1068, 21% win) | -6.4% (1068, 21% win) | -9.1% (1068, 20% win) | -8.5% (1068, 20% win) |
| d35_direct | -9.8% (1169, 19% win) | -9.1% (1169, 19% win) | -7.4% (1169, 20% win) | -6.7% (1169, 21% win) | -9.6% (1169, 19% win) | -9.0% (1169, 20% win) |
| d40_direct | -10.2% (1269, 18% win) | -9.5% (1269, 19% win) | -7.8% (1269, 20% win) | -7.1% (1269, 20% win) | -10.1% (1269, 18% win) | -9.4% (1269, 19% win) |
| d45_direct | -10.1% (1338, 18% win) | -9.5% (1338, 18% win) | -7.8% (1338, 20% win) | -7.1% (1338, 20% win) | -10.2% (1338, 18% win) | -9.6% (1338, 18% win) |
| d50_direct | -10.0% (1427, 18% win) | -9.3% (1427, 18% win) | -7.6% (1427, 19% win) | -7.0% (1427, 20% win) | -10.2% (1427, 18% win) | -9.6% (1427, 18% win) |
| d55_direct | -8.7% (1514, 18% win) | -8.0% (1514, 18% win) | -6.4% (1514, 19% win) | -5.7% (1514, 20% win) | -9.3% (1514, 18% win) | -8.6% (1514, 18% win) |
| d60_direct | -8.2% (1547, 19% win) | -7.5% (1547, 19% win) | -5.9% (1547, 20% win) | -5.2% (1547, 20% win) | -9.0% (1547, 18% win) | -8.4% (1547, 19% win) |
| d65_direct | -7.5% (1408, 20% win) | -6.9% (1408, 21% win) | -5.4% (1408, 22% win) | -4.7% (1408, 22% win) | -8.7% (1408, 20% win) | -8.1% (1408, 20% win) |
| d70_direct | -6.9% (1269, 23% win) | -6.2% (1269, 24% win) | -4.8% (1269, 24% win) | -4.1% (1269, 24% win) | -8.6% (1269, 22% win) | -8.0% (1269, 23% win) |
| d75_direct | -7.9% (1115, 24% win) | -7.2% (1115, 24% win) | -5.9% (1115, 25% win) | -5.3% (1115, 25% win) | -10.4% (1115, 22% win) | -9.7% (1115, 22% win) |
| d80_direct | -7.8% (982, 26% win) | -7.1% (982, 27% win) | -6.1% (982, 27% win) | -5.4% (982, 28% win) | -11.7% (982, 24% win) | -11.1% (982, 24% win) |
| d45_herstel5 | -7.4% (1109, 22% win) | -6.7% (1109, 22% win) | -5.1% (1109, 23% win) | -4.4% (1109, 23% win) | -7.5% (1109, 22% win) | -6.9% (1109, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.3% (5015, 24% win) | -8.6% (5015, 24% win) | -7.0% (5015, 25% win) | -6.3% (5015, 25% win) | -9.5% (5015, 23% win) | -8.9% (5015, 24% win) |
| d35_direct | -9.6% (4911, 22% win) | -8.9% (4911, 23% win) | -7.3% (4911, 24% win) | -6.6% (4911, 24% win) | -10.0% (4911, 22% win) | -9.4% (4911, 22% win) |
| d40_direct | -9.8% (4803, 22% win) | -9.1% (4803, 22% win) | -7.5% (4803, 23% win) | -6.8% (4803, 23% win) | -10.4% (4803, 21% win) | -9.7% (4803, 22% win) |
| d45_direct | -9.5% (4686, 21% win) | -8.8% (4686, 22% win) | -7.3% (4686, 22% win) | -6.6% (4686, 23% win) | -10.3% (4686, 20% win) | -9.7% (4686, 21% win) |
| d50_direct | -9.9% (4585, 20% win) | -9.2% (4585, 21% win) | -7.7% (4585, 22% win) | -7.0% (4585, 22% win) | -10.9% (4585, 20% win) | -10.3% (4585, 20% win) |
| d55_direct | -9.8% (4420, 20% win) | -9.1% (4420, 20% win) | -7.7% (4420, 21% win) | -7.0% (4420, 21% win) | -11.1% (4420, 19% win) | -10.5% (4420, 19% win) |
| d60_direct | -9.2% (4110, 21% win) | -8.5% (4110, 21% win) | -7.1% (4110, 22% win) | -6.4% (4110, 22% win) | -10.9% (4110, 20% win) | -10.2% (4110, 20% win) |
| d65_direct | -9.0% (3669, 22% win) | -8.3% (3669, 22% win) | -7.1% (3669, 23% win) | -6.4% (3669, 24% win) | -11.2% (3669, 20% win) | -10.6% (3669, 21% win) |
| d70_direct | -8.3% (3246, 24% win) | -7.6% (3246, 25% win) | -6.5% (3246, 25% win) | -5.8% (3246, 26% win) | -11.3% (3246, 22% win) | -10.7% (3246, 23% win) |
| d75_direct | -8.9% (2862, 24% win) | -8.2% (2862, 24% win) | -7.2% (2862, 25% win) | -6.6% (2862, 25% win) | -12.9% (2862, 21% win) | -12.2% (2862, 22% win) |
| d80_direct | -8.8% (2491, 26% win) | -8.1% (2491, 27% win) | -7.5% (2491, 27% win) | -6.9% (2491, 27% win) | -14.6% (2491, 22% win) | -14.1% (2491, 22% win) |
| d45_herstel5 | -9.3% (3845, 25% win) | -8.6% (3845, 26% win) | -7.1% (3845, 26% win) | -6.4% (3845, 27% win) | -10.4% (3845, 24% win) | -9.8% (3845, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.6% (4686, 23% win) | -6.3% (4686, 22% win) | -6.8% (4686, 22% win) |
| schoon | -6.4% (3765, 24% win) | -6.2% (3765, 24% win) | -6.6% (3765, 24% win) |
| bundelgrafiek | -7.5% (921, 17% win) | -6.6% (921, 17% win) | -7.4% (921, 15% win) |
| schoon+houders_ok | -7.1% (1338, 20% win) | -6.7% (1338, 20% win) | -6.4% (1338, 21% win) |
| schoon+houders_ok+final_stretch | -8.9% (556, 12% win) | -7.7% (556, 11% win) | -9.8% (556, 14% win) |
| volledige_screening+schoon | -9.9% (350, 11% win) | -8.9% (350, 9% win) | -10.9% (350, 15% win) |
| volledige_screening+schoon+x_link | -10.0% (261, 11% win) | -9.0% (261, 9% win) | -11.1% (261, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.0% (2009, 29% win); 1,3–2x: -7.9% (1756, 19% win); ≥ 2x (bundelgrafiek): -7.5% (921, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.6% (3002, 29% win); 5–20%: -8.7% (831, 13% win); ≥ 20%: -8.1% (853, 10% win)

**top t.o.v. start:** 2–3x: -6.4% (2623, 22% win); 3–6x: -6.5% (1613, 24% win); ≥ 6x: -8.2% (450, 23% win)

**unieke kopers tot de top:** < 30: -5.6% (3001, 29% win); 30–100: -7.4% (934, 11% win); ≥ 100: -9.6% (751, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.7% (1152, 16% win); 1–2: -6.1% (2227, 25% win); ≥ 3 (trap): -6.5% (1307, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.0% (1148, 12% win); 10–25%: -7.4% (739, 12% win); ≥ 25%: -5.4% (2799, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (3706, 25% win); 30 s–3 min: -8.4% (773, 15% win); ≥ 3 min (langzaam): -10.1% (207, 8% win)

**tijd van start tot top:** < 2 min: -6.4% (3869, 24% win); 2–10 min: -7.1% (653, 16% win); ≥ 10 min: -9.4% (164, 15% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
