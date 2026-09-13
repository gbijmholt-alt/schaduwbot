# Videostrategie op alle trades — 2026-09-13 15:35 UTC

Tokens sinds 2026-09-11 08:47 UTC: 39500 geschikt (≥ 2 uur oud, geen herstart), 31376 met trades, 5894 haalden 2x de startkoers, 4478 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1383 tokens. Houdercheck echt uitgevoerd bij 89% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1302, winkans 20%, EV per trade -7.2% (95%-marge -8.9% tot -5.4%), mediaan -10.7%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 3108, winkans 24%, EV -6.9% (95%-marge -8.8% tot -5.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 34, winkans 12%, EV -11.4% (95%-marge -17.2% tot -5.7%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4478 | 40% | 77% | 37% |
| schoon | 3597 | 42% | 76% | 40% |
| bundelgrafiek | 881 | 29% | 78% | 25% |
| schoon+houders_ok | 1302 | 37% | 80% | 26% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.3% (4797, 25% win) | -6.4% (4695, 24% win) | -6.7% (4590, 23% win) | -6.6% (4478, 23% win) | -7.0% (4381, 22% win) | -6.9% (4222, 21% win) | -6.4% (3922, 22% win) | -6.4% (3499, 23% win) | -5.7% (3098, 26% win) | -6.6% (2732, 25% win) | -6.9% (2377, 27% win) | -6.5% (3676, 26% win) |
| schoon | -6.1% (3855, 26% win) | -5.9% (3781, 25% win) | -6.3% (3695, 25% win) | -6.2% (3597, 24% win) | -6.5% (3523, 24% win) | -6.8% (3389, 23% win) | -6.1% (3121, 24% win) | -5.6% (2777, 26% win) | -5.2% (2485, 27% win) | -6.1% (2201, 27% win) | -6.5% (1943, 29% win) | -6.0% (3085, 27% win) |
| bundelgrafiek | -7.0% (942, 22% win) | -8.5% (914, 19% win) | -8.4% (895, 17% win) | -8.1% (881, 16% win) | -9.2% (858, 15% win) | -7.4% (833, 15% win) | -7.6% (801, 16% win) | -9.4% (722, 15% win) | -8.0% (613, 18% win) | -8.7% (531, 18% win) | -8.6% (434, 19% win) | -9.0% (591, 22% win) |
| schoon+houders_ok | -6.4% (1038, 21% win) | -6.7% (1138, 21% win) | -7.2% (1234, 20% win) | -7.2% (1302, 20% win) | -7.0% (1388, 20% win) | -5.7% (1472, 20% win) | -5.2% (1505, 21% win) | -4.7% (1368, 22% win) | -4.1% (1238, 25% win) | -5.2% (1086, 25% win) | -5.3% (960, 28% win) | -4.3% (1081, 24% win) |
| schoon+houders_ok+final_stretch | -7.3% (436, 16% win) | -7.2% (476, 15% win) | -8.2% (509, 13% win) | -9.2% (533, 11% win) | -8.9% (554, 10% win) | -7.9% (578, 9% win) | -6.8% (566, 10% win) | -6.2% (439, 11% win) | -7.6% (328, 9% win) | -7.8% (217, 8% win) | -5.7% (132, 11% win) | -6.2% (414, 15% win) |
| volledige_screening+schoon | -7.3% (302, 16% win) | -6.7% (315, 16% win) | -8.7% (322, 13% win) | -10.4% (334, 10% win) | -10.0% (340, 9% win) | -9.0% (343, 8% win) | -7.3% (331, 8% win) | -7.1% (261, 9% win) | -8.6% (195, 6% win) | -9.0% (133, 7% win) | -9.3% (82, 4% win) | -7.7% (247, 13% win) |
| volledige_screening+schoon+x_link | -8.0% (236, 16% win) | -5.8% (246, 19% win) | -9.1% (248, 14% win) | -10.5% (252, 10% win) | -10.3% (251, 8% win) | -9.8% (253, 7% win) | -8.8% (247, 6% win) | -8.5% (194, 7% win) | -8.6% (147, 5% win) | -8.9% (104, 6% win) | -8.9% (66, 2% win) | -8.0% (180, 13% win) |

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
| alle | -5.8% (4797, 30% win) | -5.9% (4695, 29% win) | -6.1% (4590, 28% win) | -6.4% (4478, 28% win) | -7.3% (4381, 26% win) | -6.8% (4222, 26% win) | -6.5% (3922, 27% win) | -6.8% (3499, 28% win) | -6.4% (3098, 31% win) | -6.7% (2732, 32% win) | -7.7% (2377, 33% win) |
| schoon | -5.7% (3855, 31% win) | -5.5% (3781, 30% win) | -5.9% (3695, 30% win) | -6.1% (3597, 29% win) | -7.2% (3523, 27% win) | -6.9% (3389, 27% win) | -6.4% (3121, 29% win) | -6.3% (2777, 31% win) | -5.9% (2485, 34% win) | -6.1% (2201, 34% win) | -7.0% (1943, 35% win) |
| bundelgrafiek | -6.5% (942, 26% win) | -7.6% (914, 24% win) | -7.1% (895, 22% win) | -7.4% (881, 20% win) | -7.7% (858, 20% win) | -6.4% (833, 20% win) | -7.0% (801, 18% win) | -8.6% (722, 17% win) | -8.5% (613, 20% win) | -9.1% (531, 22% win) | -10.5% (434, 23% win) |
| schoon+houders_ok | -6.4% (1038, 28% win) | -6.4% (1138, 28% win) | -6.5% (1234, 28% win) | -7.0% (1302, 28% win) | -7.2% (1388, 26% win) | -5.8% (1472, 27% win) | -5.1% (1505, 27% win) | -4.9% (1368, 30% win) | -4.1% (1238, 33% win) | -4.8% (1086, 34% win) | -6.7% (960, 34% win) |
| schoon+houders_ok+final_stretch | -7.0% (436, 24% win) | -6.8% (476, 24% win) | -7.1% (509, 24% win) | -9.2% (533, 21% win) | -10.4% (554, 17% win) | -9.4% (578, 18% win) | -6.3% (566, 21% win) | -6.7% (439, 22% win) | -8.5% (328, 23% win) | -7.8% (217, 25% win) | -7.1% (132, 25% win) |
| volledige_screening+schoon | -7.0% (302, 25% win) | -6.8% (315, 24% win) | -7.8% (322, 25% win) | -10.6% (334, 20% win) | -11.6% (340, 16% win) | -10.8% (343, 16% win) | -7.3% (331, 19% win) | -7.9% (261, 19% win) | -11.2% (195, 16% win) | -10.6% (133, 17% win) | -12.4% (82, 13% win) |
| volledige_screening+schoon+x_link | -7.2% (236, 25% win) | -6.2% (246, 26% win) | -7.9% (248, 24% win) | -11.2% (252, 19% win) | -12.3% (251, 14% win) | -11.1% (253, 14% win) | -7.8% (247, 17% win) | -7.9% (194, 18% win) | -9.8% (147, 18% win) | -10.8% (104, 17% win) | -12.4% (66, 11% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 334 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 47% | 23% | -8.5% | 25% |
| +15% | 42% | 19% | -8.6% | 21% |
| +20% | 39% | 16% | -8.7% | 18% |
| +25% | 34% | 13% | -9.1% | 16% |
| +30% | 31% | 12% | -9.3% | 14% |
| +35% | 28% | 11% | -9.4% | 13% |
| +45% | 24% | 8% | -10.4% | 10% |
| +60% | 20% | 6% | -10.2% | 9% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1302 instappen, mediane hoogste stijging +20.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 33% | -5.5% | 31% |
| +15% | 54% | 27% | -5.7% | 28% |
| +20% | 51% | 24% | -5.8% | 26% |
| +25% | 47% | 21% | -6.1% | 24% |
| +30% | 45% | 19% | -6.2% | 23% |
| +35% | 42% | 17% | -6.4% | 22% |
| +45% | 37% | 13% | -7.2% | 20% |
| +60% | 32% | 11% | -7.1% | 19% |

**filter `alle`** — variant `d45_direct`, 4478 instappen, mediane hoogste stijging +22.5%

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
| d30_direct | -10.4% (302, 15% win) | -9.7% (302, 15% win) | -8.0% (302, 15% win) | -7.3% (302, 16% win) | -10.4% (302, 15% win) | -9.8% (302, 15% win) |
| d35_direct | -9.8% (315, 15% win) | -9.1% (315, 15% win) | -7.4% (315, 16% win) | -6.7% (315, 16% win) | -9.8% (315, 15% win) | -9.2% (315, 15% win) |
| d40_direct | -11.7% (322, 13% win) | -11.1% (322, 13% win) | -9.4% (322, 13% win) | -8.7% (322, 13% win) | -11.8% (322, 12% win) | -11.2% (322, 12% win) |
| d45_direct | -13.4% (334, 10% win) | -12.7% (334, 10% win) | -11.0% (334, 10% win) | -10.4% (334, 10% win) | -13.5% (334, 9% win) | -12.9% (334, 9% win) |
| d50_direct | -13.0% (340, 8% win) | -12.3% (340, 8% win) | -10.7% (340, 8% win) | -10.0% (340, 9% win) | -13.4% (340, 8% win) | -12.8% (340, 8% win) |
| d55_direct | -11.9% (343, 7% win) | -11.2% (343, 8% win) | -9.6% (343, 8% win) | -9.0% (343, 8% win) | -12.5% (343, 7% win) | -11.9% (343, 7% win) |
| d60_direct | -10.2% (331, 8% win) | -9.5% (331, 8% win) | -7.9% (331, 8% win) | -7.3% (331, 8% win) | -11.1% (331, 7% win) | -10.4% (331, 8% win) |
| d65_direct | -10.0% (261, 10% win) | -9.3% (261, 10% win) | -7.8% (261, 9% win) | -7.1% (261, 9% win) | -11.0% (261, 8% win) | -10.3% (261, 9% win) |
| d70_direct | -11.4% (195, 6% win) | -10.8% (195, 6% win) | -9.2% (195, 6% win) | -8.6% (195, 6% win) | -12.4% (195, 5% win) | -11.8% (195, 5% win) |
| d75_direct | -11.8% (133, 5% win) | -11.2% (133, 5% win) | -9.7% (133, 7% win) | -9.0% (133, 7% win) | -13.0% (133, 4% win) | -12.4% (133, 4% win) |
| d80_direct | -12.0% (82, 4% win) | -11.3% (82, 4% win) | -9.9% (82, 4% win) | -9.3% (82, 4% win) | -13.7% (82, 2% win) | -13.1% (82, 2% win) |
| d45_herstel5 | -10.8% (247, 13% win) | -10.1% (247, 13% win) | -8.4% (247, 13% win) | -7.7% (247, 13% win) | -10.8% (247, 13% win) | -10.2% (247, 13% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.5% (1038, 19% win) | -8.8% (1038, 20% win) | -7.1% (1038, 20% win) | -6.4% (1038, 21% win) | -9.2% (1038, 20% win) | -8.5% (1038, 20% win) |
| d35_direct | -9.8% (1138, 19% win) | -9.2% (1138, 19% win) | -7.4% (1138, 20% win) | -6.7% (1138, 21% win) | -9.6% (1138, 19% win) | -9.0% (1138, 20% win) |
| d40_direct | -10.2% (1234, 18% win) | -9.6% (1234, 18% win) | -7.9% (1234, 20% win) | -7.2% (1234, 20% win) | -10.2% (1234, 18% win) | -9.5% (1234, 19% win) |
| d45_direct | -10.2% (1302, 18% win) | -9.6% (1302, 18% win) | -7.9% (1302, 19% win) | -7.2% (1302, 20% win) | -10.3% (1302, 18% win) | -9.7% (1302, 18% win) |
| d50_direct | -10.0% (1388, 18% win) | -9.3% (1388, 19% win) | -7.6% (1388, 20% win) | -7.0% (1388, 20% win) | -10.2% (1388, 18% win) | -9.6% (1388, 18% win) |
| d55_direct | -8.6% (1472, 18% win) | -8.0% (1472, 19% win) | -6.4% (1472, 20% win) | -5.7% (1472, 20% win) | -9.2% (1472, 18% win) | -8.6% (1472, 18% win) |
| d60_direct | -8.1% (1505, 19% win) | -7.4% (1505, 20% win) | -5.9% (1505, 20% win) | -5.2% (1505, 21% win) | -9.0% (1505, 19% win) | -8.3% (1505, 19% win) |
| d65_direct | -7.5% (1368, 20% win) | -6.8% (1368, 21% win) | -5.4% (1368, 22% win) | -4.7% (1368, 22% win) | -8.7% (1368, 20% win) | -8.1% (1368, 21% win) |
| d70_direct | -6.8% (1238, 23% win) | -6.1% (1238, 24% win) | -4.8% (1238, 24% win) | -4.1% (1238, 25% win) | -8.6% (1238, 22% win) | -8.0% (1238, 23% win) |
| d75_direct | -7.8% (1086, 24% win) | -7.1% (1086, 25% win) | -5.9% (1086, 25% win) | -5.2% (1086, 25% win) | -10.3% (1086, 22% win) | -9.7% (1086, 23% win) |
| d80_direct | -7.6% (960, 27% win) | -7.0% (960, 27% win) | -6.0% (960, 28% win) | -5.3% (960, 28% win) | -11.6% (960, 24% win) | -11.0% (960, 24% win) |
| d45_herstel5 | -7.4% (1081, 22% win) | -6.7% (1081, 22% win) | -5.0% (1081, 23% win) | -4.3% (1081, 24% win) | -7.5% (1081, 22% win) | -6.8% (1081, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.3% (4797, 23% win) | -8.6% (4797, 24% win) | -7.0% (4797, 25% win) | -6.3% (4797, 25% win) | -9.5% (4797, 23% win) | -8.9% (4797, 24% win) |
| d35_direct | -9.4% (4695, 22% win) | -8.7% (4695, 23% win) | -7.1% (4695, 24% win) | -6.4% (4695, 24% win) | -9.8% (4695, 22% win) | -9.2% (4695, 23% win) |
| d40_direct | -9.6% (4590, 22% win) | -9.0% (4590, 22% win) | -7.4% (4590, 23% win) | -6.7% (4590, 23% win) | -10.2% (4590, 21% win) | -9.6% (4590, 22% win) |
| d45_direct | -9.5% (4478, 21% win) | -8.8% (4478, 21% win) | -7.3% (4478, 22% win) | -6.6% (4478, 23% win) | -10.3% (4478, 20% win) | -9.7% (4478, 21% win) |
| d50_direct | -9.9% (4381, 20% win) | -9.2% (4381, 21% win) | -7.7% (4381, 22% win) | -7.0% (4381, 22% win) | -10.9% (4381, 20% win) | -10.3% (4381, 20% win) |
| d55_direct | -9.7% (4222, 20% win) | -9.0% (4222, 20% win) | -7.6% (4222, 21% win) | -6.9% (4222, 21% win) | -11.0% (4222, 19% win) | -10.4% (4222, 19% win) |
| d60_direct | -9.1% (3922, 21% win) | -8.5% (3922, 21% win) | -7.1% (3922, 22% win) | -6.4% (3922, 22% win) | -10.9% (3922, 20% win) | -10.2% (3922, 20% win) |
| d65_direct | -9.0% (3499, 22% win) | -8.3% (3499, 22% win) | -7.0% (3499, 23% win) | -6.4% (3499, 23% win) | -11.2% (3499, 20% win) | -10.6% (3499, 21% win) |
| d70_direct | -8.2% (3098, 24% win) | -7.5% (3098, 25% win) | -6.4% (3098, 25% win) | -5.7% (3098, 26% win) | -11.3% (3098, 22% win) | -10.6% (3098, 23% win) |
| d75_direct | -8.9% (2732, 24% win) | -8.2% (2732, 24% win) | -7.3% (2732, 25% win) | -6.6% (2732, 25% win) | -12.9% (2732, 21% win) | -12.3% (2732, 21% win) |
| d80_direct | -8.8% (2377, 26% win) | -8.1% (2377, 27% win) | -7.6% (2377, 27% win) | -6.9% (2377, 27% win) | -14.7% (2377, 22% win) | -14.1% (2377, 22% win) |
| d45_herstel5 | -9.3% (3676, 25% win) | -8.6% (3676, 25% win) | -7.1% (3676, 26% win) | -6.5% (3676, 26% win) | -10.4% (3676, 24% win) | -9.8% (3676, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.6% (4478, 23% win) | -6.2% (4478, 22% win) | -6.9% (4478, 22% win) |
| schoon | -6.2% (3597, 24% win) | -6.0% (3597, 24% win) | -6.3% (3597, 24% win) |
| bundelgrafiek | -8.1% (881, 16% win) | -7.0% (881, 16% win) | -8.9% (881, 15% win) |
| schoon+houders_ok | -7.2% (1302, 20% win) | -6.7% (1302, 20% win) | -6.4% (1302, 20% win) |
| schoon+houders_ok+final_stretch | -9.2% (533, 11% win) | -7.8% (533, 11% win) | -10.0% (533, 14% win) |
| volledige_screening+schoon | -10.4% (334, 10% win) | -9.1% (334, 9% win) | -11.3% (334, 14% win) |
| volledige_screening+schoon+x_link | -10.5% (252, 10% win) | -9.2% (252, 8% win) | -11.6% (252, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.8% (1923, 29% win); 1,3–2x: -7.9% (1674, 18% win); ≥ 2x (bundelgrafiek): -8.1% (881, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.5% (2877, 29% win); 5–20%: -8.8% (803, 13% win); ≥ 20%: -8.3% (798, 10% win)

**top t.o.v. start:** 2–3x: -6.2% (2512, 22% win); 3–6x: -6.8% (1535, 24% win); ≥ 6x: -8.3% (431, 22% win)

**unieke kopers tot de top:** < 30: -5.4% (2875, 29% win); 30–100: -7.5% (885, 11% win); ≥ 100: -10.1% (718, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.9% (1106, 15% win); 1–2: -5.9% (2130, 25% win); ≥ 3 (trap): -6.7% (1242, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.3% (1094, 11% win); 10–25%: -7.4% (705, 12% win); ≥ 25%: -5.2% (2679, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (3562, 25% win); 30 s–3 min: -8.6% (723, 15% win); ≥ 3 min (langzaam): -10.0% (193, 7% win)

**tijd van start tot top:** < 2 min: -6.4% (3710, 24% win); 2–10 min: -7.4% (616, 16% win); ≥ 10 min: -8.9% (152, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
