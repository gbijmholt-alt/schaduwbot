# Videostrategie op alle trades — 2026-09-14 10:12 UTC

Tokens sinds 2026-09-11 08:47 UTC: 60260 geschikt (≥ 2 uur oud, geen herstart), 47069 met trades, 8452 haalden 2x de startkoers, 6469 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1983 tokens. Houdercheck echt uitgevoerd bij 92% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1535, winkans 19%, EV per trade -7.3% (95%-marge -8.8% tot -5.7%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 4716, winkans 23%, EV -6.6% (95%-marge -8.2% tot -5.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 152, winkans 18%, EV -9.1% (95%-marge -12.4% tot -5.8%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 6469 | 40% | 76% | 37% |
| schoon | 5205 | 43% | 76% | 40% |
| bundelgrafiek | 1264 | 31% | 77% | 25% |
| schoon+houders_ok | 1535 | 36% | 80% | 23% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.2% (6920, 25% win) | -6.3% (6769, 24% win) | -6.8% (6622, 23% win) | -6.3% (6469, 23% win) | -6.8% (6327, 22% win) | -6.7% (6097, 22% win) | -6.3% (5665, 22% win) | -6.3% (5054, 23% win) | -5.6% (4466, 25% win) | -6.2% (3953, 25% win) | -7.1% (3435, 28% win) | -5.9% (5346, 27% win) |
| schoon | -6.4% (5557, 26% win) | -6.2% (5451, 25% win) | -6.7% (5336, 24% win) | -6.3% (5205, 24% win) | -6.5% (5091, 24% win) | -6.6% (4898, 23% win) | -6.0% (4516, 24% win) | -5.8% (4018, 25% win) | -5.2% (3578, 27% win) | -5.8% (3182, 27% win) | -6.8% (2813, 29% win) | -5.9% (4479, 27% win) |
| bundelgrafiek | -5.6% (1363, 24% win) | -6.9% (1318, 22% win) | -7.3% (1286, 19% win) | -6.4% (1264, 19% win) | -8.1% (1236, 16% win) | -7.1% (1199, 16% win) | -7.8% (1149, 16% win) | -8.5% (1036, 16% win) | -7.2% (888, 19% win) | -8.1% (771, 18% win) | -8.3% (622, 20% win) | -5.7% (867, 25% win) |
| schoon+houders_ok | -6.5% (1171, 20% win) | -7.1% (1297, 19% win) | -7.4% (1438, 19% win) | -7.3% (1535, 19% win) | -7.0% (1650, 19% win) | -6.0% (1766, 19% win) | -5.3% (1829, 19% win) | -4.9% (1662, 20% win) | -4.5% (1492, 23% win) | -5.0% (1305, 24% win) | -5.6% (1133, 26% win) | -4.2% (1250, 23% win) |
| schoon+houders_ok+final_stretch | -7.0% (503, 16% win) | -7.5% (559, 14% win) | -8.1% (621, 12% win) | -8.4% (662, 12% win) | -8.5% (709, 10% win) | -7.5% (751, 10% win) | -6.9% (750, 9% win) | -6.7% (587, 10% win) | -7.0% (453, 10% win) | -6.9% (314, 9% win) | -5.3% (199, 11% win) | -5.8% (507, 15% win) |
| volledige_screening+schoon | -6.7% (355, 16% win) | -7.1% (382, 15% win) | -8.6% (406, 13% win) | -9.2% (431, 11% win) | -9.3% (453, 9% win) | -8.5% (461, 8% win) | -7.2% (450, 8% win) | -7.3% (351, 8% win) | -8.2% (265, 6% win) | -7.9% (192, 7% win) | -7.7% (120, 5% win) | -7.3% (314, 13% win) |
| volledige_screening+schoon+x_link | -7.0% (272, 17% win) | -6.0% (289, 18% win) | -8.5% (299, 14% win) | -9.2% (308, 12% win) | -9.3% (313, 10% win) | -8.9% (316, 8% win) | -8.2% (310, 7% win) | -8.4% (250, 7% win) | -8.2% (190, 6% win) | -8.2% (140, 6% win) | -8.2% (90, 2% win) | -7.3% (220, 13% win) |

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
| alle | -6.2% (6920, 30% win) | -6.5% (6769, 29% win) | -6.6% (6622, 28% win) | -6.3% (6469, 28% win) | -7.1% (6327, 27% win) | -6.7% (6097, 26% win) | -6.8% (5665, 27% win) | -6.5% (5054, 28% win) | -6.3% (4466, 31% win) | -6.8% (3953, 32% win) | -7.6% (3435, 33% win) |
| schoon | -6.3% (5557, 30% win) | -6.3% (5451, 30% win) | -6.6% (5336, 29% win) | -6.4% (5205, 29% win) | -7.2% (5091, 28% win) | -6.7% (4898, 28% win) | -6.6% (4516, 29% win) | -5.9% (4018, 31% win) | -5.8% (3578, 33% win) | -6.3% (3182, 34% win) | -7.1% (2813, 35% win) |
| bundelgrafiek | -5.7% (1363, 28% win) | -7.1% (1318, 25% win) | -6.7% (1286, 23% win) | -6.0% (1264, 22% win) | -6.9% (1236, 22% win) | -6.3% (1199, 21% win) | -7.2% (1149, 19% win) | -8.4% (1036, 19% win) | -8.3% (888, 22% win) | -8.8% (771, 23% win) | -9.7% (622, 25% win) |
| schoon+houders_ok | -6.7% (1171, 27% win) | -6.9% (1297, 27% win) | -6.7% (1438, 27% win) | -7.1% (1535, 27% win) | -7.4% (1650, 26% win) | -6.1% (1766, 26% win) | -5.6% (1829, 26% win) | -5.3% (1662, 28% win) | -4.5% (1492, 32% win) | -5.0% (1305, 33% win) | -6.9% (1133, 33% win) |
| schoon+houders_ok+final_stretch | -7.0% (503, 25% win) | -7.4% (559, 24% win) | -7.5% (621, 23% win) | -9.3% (662, 21% win) | -10.2% (709, 18% win) | -8.9% (751, 18% win) | -7.6% (750, 19% win) | -7.8% (587, 21% win) | -7.6% (453, 24% win) | -7.2% (314, 26% win) | -6.2% (199, 26% win) |
| volledige_screening+schoon | -7.1% (355, 25% win) | -7.4% (382, 23% win) | -8.2% (406, 24% win) | -10.5% (431, 20% win) | -11.3% (453, 17% win) | -10.2% (461, 17% win) | -8.3% (450, 17% win) | -8.6% (351, 18% win) | -10.1% (265, 18% win) | -9.3% (192, 20% win) | -8.7% (120, 18% win) |
| volledige_screening+schoon+x_link | -7.3% (272, 25% win) | -6.6% (289, 25% win) | -8.2% (299, 23% win) | -10.8% (308, 20% win) | -11.7% (313, 15% win) | -9.9% (316, 17% win) | -8.0% (310, 17% win) | -8.4% (250, 18% win) | -9.0% (190, 20% win) | -9.0% (140, 20% win) | -8.7% (90, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 431 instappen, mediane hoogste stijging +8.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -7.9% | 25% |
| +15% | 43% | 20% | -7.9% | 21% |
| +20% | 39% | 17% | -7.9% | 19% |
| +25% | 34% | 15% | -8.2% | 17% |
| +30% | 31% | 13% | -8.3% | 15% |
| +35% | 29% | 12% | -8.3% | 14% |
| +45% | 24% | 8% | -9.2% | 11% |
| +60% | 20% | 7% | -9.1% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1535 instappen, mediane hoogste stijging +19.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.8% | 30% |
| +15% | 53% | 26% | -5.9% | 27% |
| +20% | 50% | 23% | -6.0% | 25% |
| +25% | 46% | 20% | -6.2% | 23% |
| +30% | 44% | 19% | -6.4% | 23% |
| +35% | 41% | 16% | -6.5% | 21% |
| +45% | 36% | 13% | -7.3% | 19% |
| +60% | 31% | 10% | -7.1% | 18% |

**filter `alle`** — variant `d45_direct`, 6469 instappen, mediane hoogste stijging +23.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.7% | 30% |
| +15% | 55% | 30% | -5.8% | 28% |
| +20% | 52% | 26% | -5.9% | 27% |
| +25% | 49% | 24% | -6.0% | 26% |
| +30% | 46% | 21% | -6.0% | 25% |
| +35% | 44% | 19% | -6.2% | 24% |
| +45% | 40% | 16% | -6.3% | 23% |
| +60% | 35% | 13% | -6.2% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.7% (355, 15% win) | -9.0% (355, 16% win) | -7.3% (355, 16% win) | -6.7% (355, 16% win) | -9.7% (355, 15% win) | -9.1% (355, 15% win) |
| d35_direct | -10.1% (382, 14% win) | -9.4% (382, 14% win) | -7.8% (382, 15% win) | -7.1% (382, 15% win) | -10.2% (382, 14% win) | -9.5% (382, 14% win) |
| d40_direct | -11.6% (406, 12% win) | -11.0% (406, 12% win) | -9.3% (406, 13% win) | -8.6% (406, 13% win) | -11.7% (406, 11% win) | -11.1% (406, 12% win) |
| d45_direct | -12.2% (431, 10% win) | -11.6% (431, 10% win) | -9.9% (431, 11% win) | -9.2% (431, 11% win) | -12.4% (431, 10% win) | -11.8% (431, 10% win) |
| d50_direct | -12.2% (453, 8% win) | -11.6% (453, 8% win) | -9.9% (453, 9% win) | -9.3% (453, 9% win) | -12.7% (453, 8% win) | -12.0% (453, 8% win) |
| d55_direct | -11.5% (461, 8% win) | -10.8% (461, 8% win) | -9.2% (461, 8% win) | -8.5% (461, 8% win) | -12.1% (461, 7% win) | -11.4% (461, 8% win) |
| d60_direct | -10.1% (450, 8% win) | -9.4% (450, 8% win) | -7.9% (450, 8% win) | -7.2% (450, 8% win) | -11.0% (450, 7% win) | -10.3% (450, 8% win) |
| d65_direct | -10.2% (351, 8% win) | -9.5% (351, 8% win) | -8.0% (351, 8% win) | -7.3% (351, 8% win) | -11.1% (351, 7% win) | -10.5% (351, 8% win) |
| d70_direct | -11.1% (265, 6% win) | -10.4% (265, 6% win) | -8.9% (265, 6% win) | -8.2% (265, 6% win) | -12.0% (265, 5% win) | -11.4% (265, 5% win) |
| d75_direct | -10.8% (192, 6% win) | -10.1% (192, 6% win) | -8.6% (192, 7% win) | -7.9% (192, 7% win) | -11.8% (192, 6% win) | -11.2% (192, 6% win) |
| d80_direct | -10.5% (120, 5% win) | -9.8% (120, 5% win) | -8.4% (120, 5% win) | -7.7% (120, 5% win) | -12.0% (120, 4% win) | -11.4% (120, 4% win) |
| d45_herstel5 | -10.3% (314, 13% win) | -9.6% (314, 13% win) | -7.9% (314, 13% win) | -7.3% (314, 13% win) | -10.3% (314, 13% win) | -9.7% (314, 13% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (1171, 19% win) | -8.9% (1171, 19% win) | -7.2% (1171, 20% win) | -6.5% (1171, 20% win) | -9.3% (1171, 19% win) | -8.6% (1171, 20% win) |
| d35_direct | -10.2% (1297, 18% win) | -9.6% (1297, 18% win) | -7.8% (1297, 19% win) | -7.1% (1297, 19% win) | -10.0% (1297, 18% win) | -9.4% (1297, 19% win) |
| d40_direct | -10.5% (1438, 17% win) | -9.8% (1438, 18% win) | -8.1% (1438, 18% win) | -7.4% (1438, 19% win) | -10.4% (1438, 17% win) | -9.8% (1438, 18% win) |
| d45_direct | -10.3% (1535, 17% win) | -9.6% (1535, 17% win) | -7.9% (1535, 18% win) | -7.3% (1535, 19% win) | -10.4% (1535, 17% win) | -9.7% (1535, 17% win) |
| d50_direct | -10.0% (1650, 17% win) | -9.3% (1650, 18% win) | -7.7% (1650, 18% win) | -7.0% (1650, 19% win) | -10.3% (1650, 17% win) | -9.6% (1650, 17% win) |
| d55_direct | -8.9% (1766, 17% win) | -8.2% (1766, 17% win) | -6.7% (1766, 18% win) | -6.0% (1766, 19% win) | -9.5% (1766, 17% win) | -8.9% (1766, 17% win) |
| d60_direct | -8.2% (1829, 18% win) | -7.5% (1829, 18% win) | -5.9% (1829, 19% win) | -5.3% (1829, 19% win) | -9.0% (1829, 17% win) | -8.4% (1829, 18% win) |
| d65_direct | -7.8% (1662, 19% win) | -7.1% (1662, 19% win) | -5.6% (1662, 20% win) | -4.9% (1662, 20% win) | -8.9% (1662, 18% win) | -8.2% (1662, 19% win) |
| d70_direct | -7.2% (1492, 21% win) | -6.5% (1492, 22% win) | -5.1% (1492, 22% win) | -4.5% (1492, 23% win) | -8.8% (1492, 21% win) | -8.2% (1492, 21% win) |
| d75_direct | -7.7% (1305, 23% win) | -7.0% (1305, 23% win) | -5.7% (1305, 24% win) | -5.0% (1305, 24% win) | -10.0% (1305, 21% win) | -9.3% (1305, 22% win) |
| d80_direct | -8.0% (1133, 24% win) | -7.3% (1133, 25% win) | -6.2% (1133, 26% win) | -5.6% (1133, 26% win) | -11.6% (1133, 22% win) | -10.9% (1133, 22% win) |
| d45_herstel5 | -7.2% (1250, 22% win) | -6.5% (1250, 22% win) | -4.9% (1250, 23% win) | -4.2% (1250, 23% win) | -7.3% (1250, 22% win) | -6.7% (1250, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.2% (6920, 24% win) | -8.6% (6920, 24% win) | -6.9% (6920, 25% win) | -6.2% (6920, 25% win) | -9.5% (6920, 23% win) | -8.8% (6920, 24% win) |
| d35_direct | -9.3% (6769, 23% win) | -8.6% (6769, 23% win) | -7.0% (6769, 24% win) | -6.3% (6769, 24% win) | -9.7% (6769, 22% win) | -9.0% (6769, 23% win) |
| d40_direct | -9.8% (6622, 21% win) | -9.1% (6622, 22% win) | -7.5% (6622, 23% win) | -6.8% (6622, 23% win) | -10.3% (6622, 21% win) | -9.7% (6622, 21% win) |
| d45_direct | -9.2% (6469, 21% win) | -8.6% (6469, 22% win) | -7.0% (6469, 22% win) | -6.3% (6469, 23% win) | -10.1% (6469, 21% win) | -9.4% (6469, 21% win) |
| d50_direct | -9.7% (6327, 20% win) | -9.0% (6327, 21% win) | -7.5% (6327, 22% win) | -6.8% (6327, 22% win) | -10.7% (6327, 20% win) | -10.1% (6327, 20% win) |
| d55_direct | -9.6% (6097, 20% win) | -8.9% (6097, 20% win) | -7.4% (6097, 21% win) | -6.7% (6097, 22% win) | -10.9% (6097, 19% win) | -10.2% (6097, 19% win) |
| d60_direct | -9.1% (5665, 21% win) | -8.4% (5665, 21% win) | -7.0% (5665, 22% win) | -6.3% (5665, 22% win) | -10.8% (5665, 19% win) | -10.2% (5665, 20% win) |
| d65_direct | -9.0% (5054, 22% win) | -8.3% (5054, 22% win) | -7.0% (5054, 23% win) | -6.3% (5054, 23% win) | -11.2% (5054, 20% win) | -10.6% (5054, 21% win) |
| d70_direct | -8.1% (4466, 24% win) | -7.4% (4466, 24% win) | -6.3% (4466, 25% win) | -5.6% (4466, 25% win) | -11.2% (4466, 22% win) | -10.5% (4466, 23% win) |
| d75_direct | -8.6% (3953, 24% win) | -7.9% (3953, 25% win) | -6.9% (3953, 25% win) | -6.2% (3953, 25% win) | -12.6% (3953, 22% win) | -11.9% (3953, 22% win) |
| d80_direct | -9.0% (3435, 27% win) | -8.3% (3435, 27% win) | -7.7% (3435, 27% win) | -7.1% (3435, 28% win) | -14.8% (3435, 22% win) | -14.2% (3435, 23% win) |
| d45_herstel5 | -8.7% (5346, 25% win) | -8.0% (5346, 26% win) | -6.5% (5346, 26% win) | -5.9% (5346, 27% win) | -9.8% (5346, 24% win) | -9.1% (5346, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.3% (6469, 23% win) | -6.0% (6469, 22% win) | -6.5% (6469, 22% win) |
| schoon | -6.3% (5205, 24% win) | -6.1% (5205, 24% win) | -6.2% (5205, 23% win) |
| bundelgrafiek | -6.4% (1264, 19% win) | -5.8% (1264, 18% win) | -7.2% (1264, 17% win) |
| schoon+houders_ok | -7.3% (1535, 19% win) | -6.8% (1535, 18% win) | -6.9% (1535, 20% win) |
| schoon+houders_ok+final_stretch | -8.4% (662, 12% win) | -7.3% (662, 11% win) | -10.1% (662, 14% win) |
| volledige_screening+schoon | -9.2% (431, 11% win) | -8.4% (431, 9% win) | -11.6% (431, 14% win) |
| volledige_screening+schoon+x_link | -9.2% (308, 12% win) | -8.3% (308, 9% win) | -11.6% (308, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (2788, 28% win); 1,3–2x: -7.0% (2416, 19% win); ≥ 2x (bundelgrafiek): -6.4% (1265, 19% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.4% (4099, 29% win); 5–20%: -8.3% (1106, 14% win); ≥ 20%: -7.6% (1264, 11% win)

**top t.o.v. start:** 2–3x: -6.4% (3646, 22% win); 3–6x: -5.9% (2213, 24% win); ≥ 6x: -7.4% (610, 25% win)

**unieke kopers tot de top:** < 30: -5.4% (4094, 29% win); 30–100: -7.2% (1356, 12% win); ≥ 100: -8.7% (1019, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.6% (1540, 16% win); 1–2: -6.2% (3121, 24% win); ≥ 3 (trap): -6.4% (1808, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.4% (1591, 13% win); 10–25%: -8.0% (1042, 12% win); ≥ 25%: -5.0% (3836, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.6% (5071, 26% win); 30 s–3 min: -8.6% (1117, 14% win); ≥ 3 min (langzaam): -10.1% (281, 7% win)

**tijd van start tot top:** < 2 min: -5.9% (5309, 25% win); 2–10 min: -7.7% (928, 16% win); ≥ 10 min: -10.9% (232, 11% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
