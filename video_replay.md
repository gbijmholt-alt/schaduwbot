# Videostrategie op alle trades — 2026-09-14 22:17 UTC

Tokens sinds 2026-09-11 08:47 UTC: 75941 geschikt (≥ 2 uur oud, geen herstart), 58679 met trades, 10735 haalden 2x de startkoers, 8234 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2541 tokens. Houdercheck echt uitgevoerd bij 92% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1630, winkans 19%, EV per trade -7.2% (95%-marge -8.7% tot -5.7%), mediaan -10.4%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 6129, winkans 22%, EV -7.5% (95%-marge -8.8% tot -6.1%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 198, winkans 18%, EV -9.9% (95%-marge -13.0% tot -6.8%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 8234 | 39% | 77% | 36% |
| schoon | 6618 | 41% | 77% | 38% |
| bundelgrafiek | 1616 | 31% | 78% | 25% |
| schoon+houders_ok | 1630 | 35% | 80% | 22% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.3% (8804, 25% win) | -6.7% (8616, 24% win) | -7.2% (8424, 22% win) | -6.7% (8234, 22% win) | -7.0% (8061, 22% win) | -7.2% (7743, 21% win) | -6.7% (7185, 22% win) | -6.5% (6398, 23% win) | -6.0% (5640, 24% win) | -6.6% (4977, 25% win) | -6.7% (4316, 27% win) | -6.3% (6667, 26% win) |
| schoon | -6.5% (7063, 25% win) | -6.6% (6924, 24% win) | -7.1% (6774, 23% win) | -6.6% (6618, 23% win) | -6.8% (6477, 23% win) | -7.1% (6206, 22% win) | -6.5% (5713, 23% win) | -6.2% (5084, 24% win) | -5.6% (4520, 26% win) | -6.2% (4000, 26% win) | -6.2% (3528, 29% win) | -6.2% (5573, 27% win) |
| bundelgrafiek | -5.2% (1741, 25% win) | -6.8% (1692, 22% win) | -7.5% (1650, 19% win) | -7.0% (1616, 18% win) | -7.9% (1584, 16% win) | -7.3% (1537, 16% win) | -7.4% (1472, 16% win) | -7.8% (1314, 17% win) | -7.6% (1120, 18% win) | -8.2% (977, 18% win) | -8.7% (788, 19% win) | -6.3% (1094, 24% win) |
| schoon+houders_ok | -6.7% (1234, 20% win) | -7.2% (1372, 19% win) | -7.4% (1524, 19% win) | -7.2% (1630, 19% win) | -7.2% (1755, 18% win) | -6.2% (1882, 18% win) | -5.5% (1951, 18% win) | -5.1% (1772, 20% win) | -4.5% (1600, 22% win) | -5.1% (1393, 23% win) | -5.5% (1205, 25% win) | -4.1% (1313, 23% win) |
| schoon+houders_ok+final_stretch | -7.3% (534, 16% win) | -7.6% (597, 14% win) | -8.0% (665, 13% win) | -8.2% (712, 12% win) | -8.6% (765, 10% win) | -7.7% (816, 10% win) | -7.2% (817, 9% win) | -6.9% (640, 9% win) | -6.9% (505, 10% win) | -7.0% (355, 8% win) | -5.6% (231, 10% win) | -5.5% (541, 16% win) |
| volledige_screening+schoon | -6.9% (382, 16% win) | -7.4% (412, 15% win) | -8.9% (439, 12% win) | -9.4% (467, 11% win) | -9.8% (494, 9% win) | -8.9% (507, 8% win) | -7.5% (497, 8% win) | -7.7% (386, 8% win) | -8.0% (295, 6% win) | -7.7% (220, 7% win) | -7.4% (142, 6% win) | -7.2% (339, 13% win) |
| volledige_screening+schoon+x_link | -7.2% (295, 17% win) | -6.6% (314, 18% win) | -9.0% (323, 13% win) | -9.6% (332, 11% win) | -9.9% (340, 9% win) | -9.4% (346, 8% win) | -8.5% (343, 7% win) | -8.7% (279, 6% win) | -8.1% (215, 6% win) | -7.8% (163, 7% win) | -7.8% (107, 3% win) | -7.7% (234, 12% win) |

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
| alle | -6.3% (8804, 30% win) | -6.8% (8616, 28% win) | -7.1% (8424, 27% win) | -6.8% (8234, 27% win) | -7.3% (8061, 26% win) | -7.1% (7743, 26% win) | -7.0% (7185, 26% win) | -6.7% (6398, 28% win) | -6.7% (5640, 30% win) | -7.2% (4977, 31% win) | -7.2% (4316, 33% win) |
| schoon | -6.4% (7063, 30% win) | -6.7% (6924, 29% win) | -7.0% (6774, 28% win) | -6.8% (6618, 28% win) | -7.4% (6477, 27% win) | -7.2% (6206, 27% win) | -7.0% (5713, 28% win) | -6.3% (5084, 30% win) | -6.2% (4520, 32% win) | -6.8% (4000, 33% win) | -6.7% (3528, 35% win) |
| bundelgrafiek | -5.6% (1741, 28% win) | -7.1% (1692, 25% win) | -7.3% (1650, 22% win) | -6.8% (1616, 21% win) | -7.0% (1584, 21% win) | -6.7% (1537, 20% win) | -6.9% (1472, 19% win) | -8.1% (1314, 19% win) | -8.6% (1120, 21% win) | -8.7% (977, 23% win) | -9.3% (788, 25% win) |
| schoon+houders_ok | -6.6% (1234, 27% win) | -6.8% (1372, 27% win) | -6.9% (1524, 26% win) | -7.2% (1630, 27% win) | -7.6% (1755, 25% win) | -6.3% (1882, 26% win) | -5.8% (1951, 25% win) | -5.7% (1772, 28% win) | -4.9% (1600, 31% win) | -5.3% (1393, 32% win) | -6.9% (1205, 32% win) |
| schoon+houders_ok+final_stretch | -7.0% (534, 25% win) | -7.7% (597, 23% win) | -7.7% (665, 23% win) | -9.4% (712, 21% win) | -10.5% (765, 17% win) | -9.1% (816, 18% win) | -7.6% (817, 19% win) | -8.4% (640, 20% win) | -8.0% (505, 23% win) | -7.5% (355, 24% win) | -7.0% (231, 24% win) |
| volledige_screening+schoon | -7.1% (382, 25% win) | -7.7% (412, 23% win) | -8.6% (439, 23% win) | -10.8% (467, 20% win) | -11.8% (494, 16% win) | -10.4% (507, 17% win) | -8.3% (497, 17% win) | -9.1% (386, 18% win) | -10.3% (295, 18% win) | -9.4% (220, 19% win) | -9.3% (142, 18% win) |
| volledige_screening+schoon+x_link | -7.2% (295, 25% win) | -7.0% (314, 24% win) | -8.8% (323, 23% win) | -11.2% (332, 19% win) | -12.0% (340, 15% win) | -10.0% (346, 17% win) | -8.1% (343, 18% win) | -9.0% (279, 17% win) | -9.4% (215, 18% win) | -8.9% (163, 19% win) | -9.3% (107, 16% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 467 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 24% | -8.0% | 25% |
| +15% | 43% | 20% | -8.1% | 21% |
| +20% | 39% | 17% | -8.1% | 19% |
| +25% | 34% | 15% | -8.4% | 16% |
| +30% | 31% | 13% | -8.5% | 15% |
| +35% | 29% | 12% | -8.4% | 14% |
| +45% | 23% | 8% | -9.4% | 11% |
| +60% | 19% | 7% | -9.3% | 9% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1630 instappen, mediane hoogste stijging +18.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.9% | 30% |
| +15% | 52% | 26% | -6.0% | 27% |
| +20% | 49% | 23% | -6.1% | 24% |
| +25% | 46% | 20% | -6.3% | 23% |
| +30% | 43% | 18% | -6.4% | 22% |
| +35% | 40% | 16% | -6.5% | 21% |
| +45% | 35% | 13% | -7.2% | 19% |
| +60% | 31% | 10% | -7.0% | 17% |

**filter `alle`** — variant `d45_direct`, 8234 instappen, mediane hoogste stijging +21.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 33% | -6.1% | 29% |
| +15% | 54% | 29% | -6.2% | 27% |
| +20% | 51% | 26% | -6.3% | 26% |
| +25% | 48% | 23% | -6.4% | 25% |
| +30% | 45% | 20% | -6.5% | 24% |
| +35% | 42% | 18% | -6.6% | 24% |
| +45% | 38% | 15% | -6.7% | 22% |
| +60% | 34% | 12% | -6.7% | 21% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.9% (382, 15% win) | -9.2% (382, 15% win) | -7.5% (382, 16% win) | -6.9% (382, 16% win) | -9.9% (382, 15% win) | -9.3% (382, 15% win) |
| d35_direct | -10.5% (412, 14% win) | -9.8% (412, 14% win) | -8.1% (412, 15% win) | -7.4% (412, 15% win) | -10.5% (412, 14% win) | -9.8% (412, 14% win) |
| d40_direct | -11.9% (439, 12% win) | -11.2% (439, 12% win) | -9.5% (439, 12% win) | -8.9% (439, 12% win) | -11.9% (439, 11% win) | -11.3% (439, 12% win) |
| d45_direct | -12.4% (467, 10% win) | -11.7% (467, 10% win) | -10.0% (467, 11% win) | -9.4% (467, 11% win) | -12.5% (467, 10% win) | -11.9% (467, 10% win) |
| d50_direct | -12.7% (494, 8% win) | -12.1% (494, 8% win) | -10.4% (494, 8% win) | -9.8% (494, 9% win) | -13.1% (494, 8% win) | -12.5% (494, 8% win) |
| d55_direct | -11.8% (507, 8% win) | -11.2% (507, 8% win) | -9.5% (507, 8% win) | -8.9% (507, 8% win) | -12.4% (507, 7% win) | -11.8% (507, 8% win) |
| d60_direct | -10.3% (497, 8% win) | -9.7% (497, 8% win) | -8.1% (497, 8% win) | -7.5% (497, 8% win) | -11.2% (497, 7% win) | -10.6% (497, 7% win) |
| d65_direct | -10.6% (386, 8% win) | -9.9% (386, 8% win) | -8.4% (386, 8% win) | -7.7% (386, 8% win) | -11.5% (386, 7% win) | -10.9% (386, 8% win) |
| d70_direct | -10.8% (295, 6% win) | -10.2% (295, 6% win) | -8.6% (295, 6% win) | -8.0% (295, 6% win) | -11.8% (295, 5% win) | -11.2% (295, 6% win) |
| d75_direct | -10.5% (220, 6% win) | -9.8% (220, 6% win) | -8.3% (220, 7% win) | -7.7% (220, 7% win) | -11.6% (220, 6% win) | -11.0% (220, 6% win) |
| d80_direct | -10.2% (142, 5% win) | -9.5% (142, 5% win) | -8.1% (142, 5% win) | -7.4% (142, 6% win) | -11.7% (142, 4% win) | -11.1% (142, 4% win) |
| d45_herstel5 | -10.3% (339, 13% win) | -9.6% (339, 13% win) | -7.9% (339, 13% win) | -7.2% (339, 13% win) | -10.3% (339, 13% win) | -9.7% (339, 13% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.8% (1234, 19% win) | -9.2% (1234, 19% win) | -7.4% (1234, 20% win) | -6.7% (1234, 20% win) | -9.5% (1234, 19% win) | -8.8% (1234, 19% win) |
| d35_direct | -10.3% (1372, 18% win) | -9.6% (1372, 18% win) | -7.8% (1372, 19% win) | -7.2% (1372, 19% win) | -10.1% (1372, 18% win) | -9.4% (1372, 19% win) |
| d40_direct | -10.5% (1524, 17% win) | -9.8% (1524, 18% win) | -8.1% (1524, 18% win) | -7.4% (1524, 19% win) | -10.4% (1524, 17% win) | -9.8% (1524, 18% win) |
| d45_direct | -10.2% (1630, 17% win) | -9.6% (1630, 17% win) | -7.9% (1630, 18% win) | -7.2% (1630, 19% win) | -10.3% (1630, 17% win) | -9.7% (1630, 17% win) |
| d50_direct | -10.2% (1755, 17% win) | -9.5% (1755, 17% win) | -7.8% (1755, 18% win) | -7.2% (1755, 18% win) | -10.4% (1755, 16% win) | -9.8% (1755, 17% win) |
| d55_direct | -9.1% (1882, 17% win) | -8.4% (1882, 17% win) | -6.8% (1882, 18% win) | -6.2% (1882, 18% win) | -9.7% (1882, 16% win) | -9.0% (1882, 17% win) |
| d60_direct | -8.4% (1951, 17% win) | -7.7% (1951, 17% win) | -6.2% (1951, 18% win) | -5.5% (1951, 18% win) | -9.2% (1951, 16% win) | -8.6% (1951, 17% win) |
| d65_direct | -8.0% (1772, 18% win) | -7.3% (1772, 18% win) | -5.8% (1772, 19% win) | -5.1% (1772, 20% win) | -9.1% (1772, 18% win) | -8.5% (1772, 18% win) |
| d70_direct | -7.3% (1600, 21% win) | -6.6% (1600, 21% win) | -5.2% (1600, 22% win) | -4.5% (1600, 22% win) | -8.9% (1600, 20% win) | -8.2% (1600, 20% win) |
| d75_direct | -7.8% (1393, 22% win) | -7.1% (1393, 22% win) | -5.8% (1393, 22% win) | -5.1% (1393, 23% win) | -10.0% (1393, 20% win) | -9.3% (1393, 20% win) |
| d80_direct | -7.9% (1205, 24% win) | -7.2% (1205, 24% win) | -6.2% (1205, 25% win) | -5.5% (1205, 25% win) | -11.4% (1205, 22% win) | -10.8% (1205, 22% win) |
| d45_herstel5 | -7.2% (1313, 22% win) | -6.5% (1313, 22% win) | -4.8% (1313, 23% win) | -4.1% (1313, 23% win) | -7.2% (1313, 22% win) | -6.6% (1313, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.3% (8804, 23% win) | -8.6% (8804, 24% win) | -7.0% (8804, 25% win) | -6.3% (8804, 25% win) | -9.5% (8804, 23% win) | -8.9% (8804, 24% win) |
| d35_direct | -9.6% (8616, 22% win) | -8.9% (8616, 22% win) | -7.3% (8616, 23% win) | -6.7% (8616, 24% win) | -10.0% (8616, 22% win) | -9.4% (8616, 22% win) |
| d40_direct | -10.1% (8424, 21% win) | -9.4% (8424, 21% win) | -7.8% (8424, 22% win) | -7.2% (8424, 22% win) | -10.7% (8424, 20% win) | -10.0% (8424, 21% win) |
| d45_direct | -9.6% (8234, 20% win) | -8.9% (8234, 21% win) | -7.4% (8234, 22% win) | -6.7% (8234, 22% win) | -10.4% (8234, 20% win) | -9.8% (8234, 20% win) |
| d50_direct | -9.9% (8061, 20% win) | -9.2% (8061, 20% win) | -7.7% (8061, 21% win) | -7.0% (8061, 22% win) | -10.9% (8061, 19% win) | -10.3% (8061, 20% win) |
| d55_direct | -10.0% (7743, 19% win) | -9.3% (7743, 20% win) | -7.8% (7743, 20% win) | -7.2% (7743, 21% win) | -11.3% (7743, 18% win) | -10.7% (7743, 19% win) |
| d60_direct | -9.4% (7185, 20% win) | -8.8% (7185, 20% win) | -7.4% (7185, 21% win) | -6.7% (7185, 22% win) | -11.2% (7185, 19% win) | -10.5% (7185, 19% win) |
| d65_direct | -9.1% (6398, 21% win) | -8.5% (6398, 22% win) | -7.2% (6398, 22% win) | -6.5% (6398, 23% win) | -11.4% (6398, 20% win) | -10.7% (6398, 20% win) |
| d70_direct | -8.5% (5640, 23% win) | -7.8% (5640, 24% win) | -6.7% (5640, 24% win) | -6.0% (5640, 24% win) | -11.5% (5640, 21% win) | -10.9% (5640, 22% win) |
| d75_direct | -8.9% (4977, 24% win) | -8.2% (4977, 24% win) | -7.2% (4977, 24% win) | -6.6% (4977, 25% win) | -12.8% (4977, 21% win) | -12.2% (4977, 21% win) |
| d80_direct | -8.6% (4316, 26% win) | -7.9% (4316, 27% win) | -7.3% (4316, 27% win) | -6.7% (4316, 27% win) | -14.3% (4316, 22% win) | -13.8% (4316, 23% win) |
| d45_herstel5 | -9.1% (6667, 25% win) | -8.4% (6667, 25% win) | -6.9% (6667, 26% win) | -6.3% (6667, 26% win) | -10.2% (6667, 24% win) | -9.6% (6667, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.7% (8234, 22% win) | -6.4% (8234, 22% win) | -7.4% (8234, 21% win) |
| schoon | -6.6% (6618, 23% win) | -6.4% (6618, 23% win) | -7.1% (6618, 22% win) |
| bundelgrafiek | -7.0% (1616, 18% win) | -6.5% (1616, 18% win) | -8.3% (1616, 16% win) |
| schoon+houders_ok | -7.2% (1630, 19% win) | -6.8% (1630, 18% win) | -7.2% (1630, 19% win) |
| schoon+houders_ok+final_stretch | -8.2% (712, 12% win) | -7.3% (712, 10% win) | -10.2% (712, 14% win) |
| volledige_screening+schoon | -9.4% (467, 11% win) | -8.7% (467, 8% win) | -12.2% (467, 13% win) |
| volledige_screening+schoon+x_link | -9.6% (332, 11% win) | -8.9% (332, 8% win) | -12.2% (332, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.8% (3447, 28% win); 1,3–2x: -7.5% (3170, 18% win); ≥ 2x (bundelgrafiek): -7.0% (1617, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.6% (5069, 29% win); 5–20%: -8.4% (1426, 13% win); ≥ 20%: -8.6% (1739, 11% win)

**top t.o.v. start:** 2–3x: -6.2% (4662, 21% win); 3–6x: -7.1% (2790, 23% win); ≥ 6x: -8.1% (782, 24% win)

**unieke kopers tot de top:** < 30: -5.8% (5130, 28% win); 30–100: -7.3% (1751, 12% win); ≥ 100: -9.5% (1353, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.9% (2061, 16% win); 1–2: -6.6% (3951, 24% win); ≥ 3 (trap): -6.8% (2222, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.8% (2065, 12% win); 10–25%: -8.2% (1403, 11% win); ≥ 25%: -5.4% (4766, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.1% (6480, 25% win); 30 s–3 min: -8.8% (1395, 13% win); ≥ 3 min (langzaam): -9.4% (359, 9% win)

**tijd van start tot top:** < 2 min: -6.2% (6742, 24% win); 2–10 min: -8.1% (1188, 15% win); ≥ 10 min: -11.7% (304, 11% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
