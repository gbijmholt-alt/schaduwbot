# Videostrategie op alle trades — 2026-09-14 12:19 UTC

Tokens sinds 2026-09-11 08:47 UTC: 62026 geschikt (≥ 2 uur oud, geen herstart), 48476 met trades, 8706 haalden 2x de startkoers, 6642 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2043 tokens. Houdercheck echt uitgevoerd bij 92% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1564, winkans 19%, EV per trade -7.1% (95%-marge -8.7% tot -5.6%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 4864, winkans 23%, EV -6.7% (95%-marge -8.3% tot -5.1%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 159, winkans 19%, EV -8.8% (95%-marge -12.2% tot -5.5%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 6642 | 40% | 77% | 37% |
| schoon | 5353 | 42% | 76% | 40% |
| bundelgrafiek | 1289 | 31% | 77% | 25% |
| schoon+houders_ok | 1564 | 36% | 80% | 23% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.2% (7105, 25% win) | -6.3% (6949, 24% win) | -6.9% (6799, 23% win) | -6.4% (6642, 23% win) | -6.8% (6495, 22% win) | -6.8% (6263, 22% win) | -6.3% (5820, 22% win) | -6.3% (5191, 24% win) | -5.7% (4591, 25% win) | -6.3% (4063, 25% win) | -7.1% (3535, 28% win) | -5.8% (5497, 27% win) |
| schoon | -6.3% (5716, 26% win) | -6.2% (5606, 25% win) | -6.7% (5488, 24% win) | -6.4% (5353, 24% win) | -6.5% (5235, 24% win) | -6.7% (5040, 23% win) | -6.0% (4647, 24% win) | -5.9% (4133, 25% win) | -5.3% (3682, 27% win) | -5.9% (3271, 27% win) | -6.8% (2893, 29% win) | -5.8% (4611, 27% win) |
| bundelgrafiek | -5.6% (1389, 25% win) | -7.0% (1343, 22% win) | -7.4% (1311, 20% win) | -6.6% (1289, 19% win) | -8.1% (1260, 17% win) | -7.0% (1223, 16% win) | -7.5% (1173, 17% win) | -8.2% (1058, 17% win) | -7.0% (909, 19% win) | -8.2% (792, 18% win) | -8.6% (642, 20% win) | -5.9% (886, 25% win) |
| schoon+houders_ok | -6.5% (1189, 20% win) | -7.1% (1319, 20% win) | -7.3% (1463, 19% win) | -7.1% (1564, 19% win) | -7.0% (1682, 19% win) | -6.0% (1801, 19% win) | -5.3% (1866, 19% win) | -5.0% (1693, 20% win) | -4.5% (1524, 22% win) | -5.1% (1330, 24% win) | -5.5% (1155, 26% win) | -4.1% (1272, 23% win) |
| schoon+houders_ok+final_stretch | -7.0% (507, 17% win) | -7.4% (565, 14% win) | -7.9% (628, 13% win) | -8.2% (673, 12% win) | -8.3% (722, 10% win) | -7.4% (766, 10% win) | -7.0% (766, 9% win) | -6.8% (599, 10% win) | -6.9% (465, 10% win) | -7.0% (320, 9% win) | -5.2% (204, 11% win) | -5.5% (514, 16% win) |
| volledige_screening+schoon | -6.5% (358, 17% win) | -7.0% (386, 15% win) | -8.6% (410, 12% win) | -9.1% (436, 11% win) | -9.2% (460, 9% win) | -8.5% (468, 8% win) | -7.2% (458, 8% win) | -7.4% (356, 8% win) | -8.1% (270, 6% win) | -7.9% (196, 7% win) | -7.4% (124, 6% win) | -7.0% (318, 14% win) |
| volledige_screening+schoon+x_link | -6.8% (274, 18% win) | -6.0% (291, 18% win) | -8.5% (300, 14% win) | -9.2% (309, 12% win) | -9.3% (315, 10% win) | -9.0% (318, 8% win) | -8.3% (313, 7% win) | -8.5% (253, 7% win) | -8.3% (193, 6% win) | -8.2% (142, 6% win) | -7.7% (92, 3% win) | -7.4% (221, 13% win) |

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
| alle | -6.1% (7105, 30% win) | -6.5% (6949, 29% win) | -6.7% (6799, 28% win) | -6.4% (6642, 28% win) | -7.2% (6495, 27% win) | -6.6% (6263, 26% win) | -6.8% (5820, 27% win) | -6.5% (5191, 28% win) | -6.2% (4591, 31% win) | -7.0% (4063, 32% win) | -7.8% (3535, 33% win) |
| schoon | -6.2% (5716, 30% win) | -6.3% (5606, 30% win) | -6.7% (5488, 29% win) | -6.5% (5353, 29% win) | -7.2% (5235, 28% win) | -6.8% (5040, 28% win) | -6.7% (4647, 29% win) | -6.0% (4133, 31% win) | -5.8% (3682, 33% win) | -6.5% (3271, 34% win) | -7.3% (2893, 35% win) |
| bundelgrafiek | -5.7% (1389, 28% win) | -7.1% (1343, 25% win) | -6.8% (1311, 23% win) | -6.2% (1289, 22% win) | -6.9% (1260, 22% win) | -6.2% (1223, 21% win) | -7.0% (1173, 20% win) | -8.2% (1058, 19% win) | -8.2% (909, 22% win) | -9.0% (792, 22% win) | -10.3% (642, 24% win) |
| schoon+houders_ok | -6.5% (1189, 27% win) | -6.7% (1319, 27% win) | -6.8% (1463, 27% win) | -7.2% (1564, 27% win) | -7.4% (1682, 26% win) | -6.1% (1801, 26% win) | -5.7% (1866, 26% win) | -5.4% (1693, 28% win) | -4.6% (1524, 31% win) | -5.1% (1330, 33% win) | -6.7% (1155, 33% win) |
| schoon+houders_ok+final_stretch | -6.8% (507, 25% win) | -7.3% (565, 24% win) | -7.4% (628, 23% win) | -9.2% (673, 21% win) | -10.1% (722, 18% win) | -8.9% (766, 18% win) | -7.6% (766, 19% win) | -7.9% (599, 20% win) | -7.6% (465, 23% win) | -7.3% (320, 26% win) | -6.3% (204, 26% win) |
| volledige_screening+schoon | -7.0% (358, 25% win) | -7.4% (386, 23% win) | -8.3% (410, 24% win) | -10.5% (436, 20% win) | -11.3% (460, 16% win) | -10.1% (468, 18% win) | -8.2% (458, 18% win) | -8.7% (356, 18% win) | -10.0% (270, 18% win) | -9.4% (196, 19% win) | -8.7% (124, 18% win) |
| volledige_screening+schoon+x_link | -7.0% (274, 26% win) | -6.5% (291, 25% win) | -8.3% (300, 23% win) | -10.8% (309, 19% win) | -11.7% (315, 15% win) | -9.8% (318, 17% win) | -8.0% (313, 18% win) | -8.5% (253, 18% win) | -9.1% (193, 19% win) | -9.0% (142, 20% win) | -8.5% (92, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 436 instappen, mediane hoogste stijging +8.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 24% | -7.8% | 25% |
| +15% | 43% | 20% | -7.8% | 22% |
| +20% | 39% | 17% | -7.8% | 19% |
| +25% | 34% | 15% | -8.1% | 17% |
| +30% | 31% | 13% | -8.2% | 16% |
| +35% | 29% | 12% | -8.2% | 15% |
| +45% | 24% | 8% | -9.1% | 11% |
| +60% | 20% | 7% | -8.9% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1564 instappen, mediane hoogste stijging +19.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.8% | 30% |
| +15% | 53% | 26% | -5.9% | 27% |
| +20% | 50% | 23% | -6.0% | 25% |
| +25% | 46% | 21% | -6.1% | 24% |
| +30% | 44% | 19% | -6.3% | 23% |
| +35% | 41% | 16% | -6.4% | 21% |
| +45% | 36% | 13% | -7.1% | 19% |
| +60% | 31% | 10% | -6.9% | 18% |

**filter `alle`** — variant `d45_direct`, 6642 instappen, mediane hoogste stijging +23.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.8% | 30% |
| +15% | 55% | 30% | -5.9% | 28% |
| +20% | 52% | 26% | -6.0% | 27% |
| +25% | 49% | 23% | -6.1% | 26% |
| +30% | 46% | 21% | -6.2% | 25% |
| +35% | 44% | 19% | -6.3% | 24% |
| +45% | 40% | 16% | -6.4% | 23% |
| +60% | 35% | 13% | -6.3% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (358, 16% win) | -8.9% (358, 16% win) | -7.2% (358, 16% win) | -6.5% (358, 17% win) | -9.6% (358, 16% win) | -8.9% (358, 16% win) |
| d35_direct | -10.1% (386, 14% win) | -9.4% (386, 14% win) | -7.7% (386, 15% win) | -7.0% (386, 15% win) | -10.1% (386, 14% win) | -9.5% (386, 14% win) |
| d40_direct | -11.7% (410, 12% win) | -11.0% (410, 12% win) | -9.3% (410, 12% win) | -8.6% (410, 12% win) | -11.7% (410, 11% win) | -11.1% (410, 12% win) |
| d45_direct | -12.1% (436, 10% win) | -11.4% (436, 11% win) | -9.8% (436, 11% win) | -9.1% (436, 11% win) | -12.3% (436, 10% win) | -11.7% (436, 10% win) |
| d50_direct | -12.2% (460, 8% win) | -11.6% (460, 8% win) | -9.9% (460, 9% win) | -9.2% (460, 9% win) | -12.6% (460, 8% win) | -12.0% (460, 8% win) |
| d55_direct | -11.4% (468, 8% win) | -10.7% (468, 8% win) | -9.1% (468, 8% win) | -8.5% (468, 8% win) | -12.0% (468, 7% win) | -11.4% (468, 8% win) |
| d60_direct | -10.1% (458, 8% win) | -9.4% (458, 8% win) | -7.9% (458, 8% win) | -7.2% (458, 8% win) | -11.0% (458, 7% win) | -10.3% (458, 8% win) |
| d65_direct | -10.3% (356, 8% win) | -9.7% (356, 8% win) | -8.1% (356, 8% win) | -7.4% (356, 8% win) | -11.2% (356, 7% win) | -10.6% (356, 8% win) |
| d70_direct | -11.0% (270, 6% win) | -10.3% (270, 6% win) | -8.7% (270, 6% win) | -8.1% (270, 6% win) | -11.9% (270, 5% win) | -11.3% (270, 6% win) |
| d75_direct | -10.8% (196, 6% win) | -10.1% (196, 6% win) | -8.6% (196, 7% win) | -7.9% (196, 7% win) | -11.9% (196, 6% win) | -11.2% (196, 6% win) |
| d80_direct | -10.1% (124, 6% win) | -9.4% (124, 6% win) | -8.0% (124, 6% win) | -7.4% (124, 6% win) | -11.7% (124, 5% win) | -11.1% (124, 5% win) |
| d45_herstel5 | -10.0% (318, 14% win) | -9.3% (318, 14% win) | -7.6% (318, 14% win) | -7.0% (318, 14% win) | -10.1% (318, 14% win) | -9.4% (318, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (1189, 19% win) | -9.0% (1189, 19% win) | -7.2% (1189, 20% win) | -6.5% (1189, 20% win) | -9.3% (1189, 19% win) | -8.6% (1189, 20% win) |
| d35_direct | -10.2% (1319, 18% win) | -9.5% (1319, 18% win) | -7.8% (1319, 20% win) | -7.1% (1319, 20% win) | -10.0% (1319, 18% win) | -9.3% (1319, 19% win) |
| d40_direct | -10.4% (1463, 17% win) | -9.7% (1463, 18% win) | -8.0% (1463, 19% win) | -7.3% (1463, 19% win) | -10.3% (1463, 17% win) | -9.7% (1463, 18% win) |
| d45_direct | -10.2% (1564, 17% win) | -9.5% (1564, 17% win) | -7.8% (1564, 18% win) | -7.1% (1564, 19% win) | -10.2% (1564, 17% win) | -9.6% (1564, 18% win) |
| d50_direct | -10.0% (1682, 17% win) | -9.3% (1682, 18% win) | -7.6% (1682, 18% win) | -7.0% (1682, 19% win) | -10.2% (1682, 17% win) | -9.6% (1682, 17% win) |
| d55_direct | -8.9% (1801, 17% win) | -8.2% (1801, 17% win) | -6.7% (1801, 18% win) | -6.0% (1801, 19% win) | -9.5% (1801, 17% win) | -8.8% (1801, 17% win) |
| d60_direct | -8.2% (1866, 18% win) | -7.5% (1866, 18% win) | -6.0% (1866, 18% win) | -5.3% (1866, 19% win) | -9.1% (1866, 17% win) | -8.4% (1866, 18% win) |
| d65_direct | -7.8% (1693, 19% win) | -7.1% (1693, 19% win) | -5.7% (1693, 20% win) | -5.0% (1693, 20% win) | -8.9% (1693, 18% win) | -8.3% (1693, 19% win) |
| d70_direct | -7.3% (1524, 21% win) | -6.6% (1524, 22% win) | -5.2% (1524, 22% win) | -4.5% (1524, 22% win) | -8.9% (1524, 20% win) | -8.2% (1524, 21% win) |
| d75_direct | -7.8% (1330, 22% win) | -7.1% (1330, 23% win) | -5.8% (1330, 23% win) | -5.1% (1330, 24% win) | -10.0% (1330, 21% win) | -9.4% (1330, 21% win) |
| d80_direct | -7.9% (1155, 24% win) | -7.2% (1155, 25% win) | -6.2% (1155, 26% win) | -5.5% (1155, 26% win) | -11.4% (1155, 22% win) | -10.8% (1155, 22% win) |
| d45_herstel5 | -7.1% (1272, 22% win) | -6.4% (1272, 22% win) | -4.8% (1272, 23% win) | -4.1% (1272, 23% win) | -7.2% (1272, 22% win) | -6.6% (1272, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.2% (7105, 24% win) | -8.5% (7105, 24% win) | -6.9% (7105, 25% win) | -6.2% (7105, 25% win) | -9.4% (7105, 23% win) | -8.8% (7105, 24% win) |
| d35_direct | -9.3% (6949, 23% win) | -8.6% (6949, 23% win) | -7.0% (6949, 24% win) | -6.3% (6949, 24% win) | -9.7% (6949, 22% win) | -9.1% (6949, 23% win) |
| d40_direct | -9.8% (6799, 22% win) | -9.1% (6799, 22% win) | -7.5% (6799, 23% win) | -6.9% (6799, 23% win) | -10.4% (6799, 21% win) | -9.7% (6799, 21% win) |
| d45_direct | -9.3% (6642, 21% win) | -8.6% (6642, 22% win) | -7.1% (6642, 22% win) | -6.4% (6642, 23% win) | -10.1% (6642, 21% win) | -9.5% (6642, 21% win) |
| d50_direct | -9.7% (6495, 21% win) | -9.0% (6495, 21% win) | -7.5% (6495, 22% win) | -6.8% (6495, 22% win) | -10.7% (6495, 20% win) | -10.1% (6495, 20% win) |
| d55_direct | -9.6% (6263, 20% win) | -8.9% (6263, 20% win) | -7.4% (6263, 21% win) | -6.8% (6263, 22% win) | -10.9% (6263, 19% win) | -10.3% (6263, 19% win) |
| d60_direct | -9.1% (5820, 21% win) | -8.4% (5820, 21% win) | -7.0% (5820, 22% win) | -6.3% (5820, 22% win) | -10.8% (5820, 19% win) | -10.2% (5820, 20% win) |
| d65_direct | -9.0% (5191, 22% win) | -8.3% (5191, 22% win) | -7.0% (5191, 23% win) | -6.3% (5191, 24% win) | -11.2% (5191, 20% win) | -10.6% (5191, 21% win) |
| d70_direct | -8.2% (4591, 24% win) | -7.5% (4591, 24% win) | -6.3% (4591, 25% win) | -5.7% (4591, 25% win) | -11.2% (4591, 22% win) | -10.5% (4591, 23% win) |
| d75_direct | -8.6% (4063, 24% win) | -7.9% (4063, 24% win) | -7.0% (4063, 25% win) | -6.3% (4063, 25% win) | -12.6% (4063, 22% win) | -12.0% (4063, 22% win) |
| d80_direct | -9.1% (3535, 26% win) | -8.4% (3535, 27% win) | -7.8% (3535, 27% win) | -7.1% (3535, 28% win) | -14.8% (3535, 22% win) | -14.2% (3535, 23% win) |
| d45_herstel5 | -8.7% (5497, 25% win) | -8.0% (5497, 26% win) | -6.5% (5497, 26% win) | -5.8% (5497, 27% win) | -9.8% (5497, 24% win) | -9.1% (5497, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.4% (6642, 23% win) | -6.1% (6642, 22% win) | -6.6% (6642, 22% win) |
| schoon | -6.4% (5353, 24% win) | -6.1% (5353, 24% win) | -6.3% (5353, 23% win) |
| bundelgrafiek | -6.6% (1289, 19% win) | -6.0% (1289, 18% win) | -7.5% (1289, 16% win) |
| schoon+houders_ok | -7.1% (1564, 19% win) | -6.7% (1564, 18% win) | -6.8% (1564, 20% win) |
| schoon+houders_ok+final_stretch | -8.2% (673, 12% win) | -7.2% (673, 11% win) | -9.8% (673, 14% win) |
| volledige_screening+schoon | -9.1% (436, 11% win) | -8.4% (436, 9% win) | -11.8% (436, 13% win) |
| volledige_screening+schoon+x_link | -9.2% (309, 12% win) | -8.3% (309, 9% win) | -11.6% (309, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (2867, 28% win); 1,3–2x: -7.1% (2485, 19% win); ≥ 2x (bundelgrafiek): -6.6% (1290, 19% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.6% (4221, 29% win); 5–20%: -8.2% (1127, 13% win); ≥ 20%: -7.6% (1294, 11% win)

**top t.o.v. start:** 2–3x: -6.5% (3740, 22% win); 3–6x: -6.1% (2277, 24% win); ≥ 6x: -7.5% (625, 25% win)

**unieke kopers tot de top:** < 30: -5.6% (4209, 29% win); 30–100: -7.1% (1394, 12% win); ≥ 100: -8.8% (1039, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.6% (1563, 16% win); 1–2: -6.2% (3215, 24% win); ≥ 3 (trap): -6.6% (1864, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.4% (1627, 13% win); 10–25%: -7.8% (1064, 12% win); ≥ 25%: -5.2% (3951, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.8% (5210, 26% win); 30 s–3 min: -8.6% (1145, 14% win); ≥ 3 min (langzaam): -9.8% (287, 8% win)

**tijd van start tot top:** < 2 min: -6.0% (5450, 25% win); 2–10 min: -7.6% (957, 16% win); ≥ 10 min: -10.9% (235, 11% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
