# Videostrategie op alle trades — 2026-09-13 20:26 UTC

Tokens sinds 2026-09-11 08:47 UTC: 45291 geschikt (≥ 2 uur oud, geen herstart), 35536 met trades, 6536 haalden 2x de startkoers, 5011 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1562 tokens. Houdercheck echt uitgevoerd bij 90% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1375, winkans 20%, EV per trade -7.1% (95%-marge -8.8% tot -5.4%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 3512, winkans 24%, EV -6.8% (95%-marge -8.5% tot -5.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 73, winkans 19%, EV -8.9% (95%-marge -14.0% tot -3.8%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 5011 | 40% | 77% | 36% |
| schoon | 4001 | 43% | 76% | 40% |
| bundelgrafiek | 1010 | 29% | 79% | 24% |
| schoon+houders_ok | 1375 | 37% | 79% | 25% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.1% (5352, 25% win) | -6.4% (5245, 24% win) | -6.7% (5132, 23% win) | -6.2% (5011, 23% win) | -6.6% (4904, 22% win) | -6.6% (4730, 21% win) | -6.1% (4394, 22% win) | -6.0% (3931, 24% win) | -5.7% (3475, 25% win) | -6.4% (3058, 25% win) | -6.9% (2652, 27% win) | -6.0% (4103, 27% win) |
| schoon | -6.0% (4274, 26% win) | -6.1% (4198, 25% win) | -6.4% (4106, 24% win) | -5.9% (4001, 24% win) | -5.9% (3919, 24% win) | -6.4% (3772, 23% win) | -5.7% (3474, 24% win) | -5.2% (3101, 26% win) | -5.1% (2768, 27% win) | -5.9% (2449, 27% win) | -6.6% (2161, 29% win) | -5.6% (3438, 28% win) |
| bundelgrafiek | -6.6% (1078, 23% win) | -7.8% (1047, 20% win) | -8.1% (1026, 18% win) | -7.4% (1010, 17% win) | -9.0% (985, 15% win) | -7.3% (958, 15% win) | -7.6% (920, 15% win) | -9.3% (830, 14% win) | -7.9% (707, 17% win) | -8.4% (609, 17% win) | -7.9% (491, 19% win) | -8.1% (665, 24% win) |
| schoon+houders_ok | -6.4% (1091, 21% win) | -6.9% (1196, 20% win) | -7.2% (1301, 20% win) | -7.1% (1375, 20% win) | -6.8% (1468, 20% win) | -5.5% (1561, 20% win) | -5.2% (1596, 20% win) | -4.8% (1460, 22% win) | -4.3% (1322, 24% win) | -5.3% (1161, 24% win) | -5.5% (1019, 27% win) | -4.3% (1134, 23% win) |
| schoon+houders_ok+final_stretch | -7.1% (463, 17% win) | -7.3% (506, 15% win) | -8.1% (545, 12% win) | -8.8% (571, 12% win) | -8.5% (599, 10% win) | -7.6% (629, 10% win) | -6.9% (618, 10% win) | -6.4% (488, 11% win) | -7.7% (369, 8% win) | -8.1% (250, 7% win) | -5.5% (154, 11% win) | -6.0% (443, 15% win) |
| volledige_screening+schoon | -7.0% (325, 16% win) | -7.0% (340, 15% win) | -8.7% (350, 13% win) | -9.8% (364, 11% win) | -9.4% (375, 9% win) | -8.5% (382, 8% win) | -7.4% (370, 8% win) | -7.2% (294, 9% win) | -8.6% (222, 6% win) | -9.2% (157, 6% win) | -8.3% (101, 5% win) | -7.2% (268, 14% win) |
| volledige_screening+schoon+x_link | -7.5% (251, 17% win) | -6.0% (263, 18% win) | -8.9% (267, 14% win) | -9.9% (271, 11% win) | -9.8% (271, 9% win) | -9.2% (276, 8% win) | -8.7% (270, 7% win) | -8.6% (216, 7% win) | -8.8% (162, 5% win) | -9.0% (117, 5% win) | -9.2% (75, 1% win) | -7.4% (194, 14% win) |

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
| alle | -6.0% (5352, 30% win) | -6.3% (5245, 29% win) | -6.4% (5132, 28% win) | -6.3% (5011, 28% win) | -7.0% (4904, 26% win) | -6.5% (4730, 26% win) | -6.4% (4394, 27% win) | -6.6% (3931, 28% win) | -6.5% (3475, 31% win) | -6.5% (3058, 32% win) | -7.6% (2652, 33% win) |
| schoon | -5.9% (4274, 31% win) | -6.0% (4198, 30% win) | -6.2% (4106, 29% win) | -6.1% (4001, 29% win) | -6.9% (3919, 28% win) | -6.5% (3772, 28% win) | -6.2% (3474, 29% win) | -6.0% (3101, 31% win) | -5.9% (2768, 33% win) | -5.9% (2449, 34% win) | -7.0% (2161, 35% win) |
| bundelgrafiek | -6.3% (1078, 27% win) | -7.3% (1047, 24% win) | -6.9% (1026, 22% win) | -6.9% (1010, 20% win) | -7.6% (985, 20% win) | -6.4% (958, 20% win) | -7.0% (920, 18% win) | -9.0% (830, 16% win) | -8.9% (707, 20% win) | -8.8% (609, 22% win) | -10.4% (491, 23% win) |
| schoon+houders_ok | -6.4% (1091, 28% win) | -6.5% (1196, 28% win) | -6.5% (1301, 27% win) | -6.8% (1375, 28% win) | -7.1% (1468, 27% win) | -5.7% (1561, 27% win) | -5.2% (1596, 27% win) | -5.1% (1460, 29% win) | -4.4% (1322, 32% win) | -4.8% (1161, 34% win) | -6.7% (1019, 34% win) |
| schoon+houders_ok+final_stretch | -6.9% (463, 25% win) | -7.1% (506, 24% win) | -7.3% (545, 24% win) | -9.0% (571, 21% win) | -10.2% (599, 17% win) | -9.3% (629, 18% win) | -6.9% (618, 20% win) | -7.2% (488, 22% win) | -8.5% (369, 22% win) | -7.0% (250, 26% win) | -5.0% (154, 27% win) |
| volledige_screening+schoon | -7.1% (325, 25% win) | -7.3% (340, 24% win) | -8.2% (350, 24% win) | -10.2% (364, 21% win) | -11.2% (375, 17% win) | -10.4% (382, 17% win) | -7.9% (370, 18% win) | -8.3% (294, 19% win) | -11.2% (222, 16% win) | -9.7% (157, 19% win) | -8.2% (101, 20% win) |
| volledige_screening+schoon+x_link | -7.1% (251, 26% win) | -6.4% (263, 25% win) | -8.4% (267, 23% win) | -10.8% (271, 19% win) | -12.1% (271, 14% win) | -10.5% (276, 16% win) | -7.9% (270, 17% win) | -8.5% (216, 18% win) | -10.0% (162, 17% win) | -9.2% (117, 20% win) | -8.9% (75, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 364 instappen, mediane hoogste stijging +8.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -7.9% | 26% |
| +15% | 43% | 20% | -8.0% | 22% |
| +20% | 39% | 18% | -8.0% | 20% |
| +25% | 34% | 15% | -8.5% | 17% |
| +30% | 32% | 14% | -8.5% | 16% |
| +35% | 29% | 12% | -8.6% | 15% |
| +45% | 24% | 8% | -9.8% | 11% |
| +60% | 20% | 7% | -9.6% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1375 instappen, mediane hoogste stijging +20.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 33% | -5.4% | 31% |
| +15% | 54% | 27% | -5.6% | 28% |
| +20% | 51% | 24% | -5.7% | 26% |
| +25% | 47% | 21% | -5.9% | 24% |
| +30% | 45% | 20% | -6.1% | 24% |
| +35% | 42% | 17% | -6.3% | 22% |
| +45% | 37% | 13% | -7.1% | 20% |
| +60% | 32% | 11% | -6.9% | 18% |

**filter `alle`** — variant `d45_direct`, 5011 instappen, mediane hoogste stijging +22.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.6% | 30% |
| +15% | 55% | 30% | -5.8% | 28% |
| +20% | 52% | 27% | -5.9% | 27% |
| +25% | 48% | 24% | -5.9% | 26% |
| +30% | 46% | 21% | -6.0% | 25% |
| +35% | 43% | 19% | -6.2% | 24% |
| +45% | 39% | 16% | -6.2% | 23% |
| +60% | 35% | 13% | -6.1% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.0% (325, 15% win) | -9.3% (325, 15% win) | -7.6% (325, 16% win) | -7.0% (325, 16% win) | -10.0% (325, 15% win) | -9.4% (325, 15% win) |
| d35_direct | -10.1% (340, 15% win) | -9.4% (340, 15% win) | -7.7% (340, 15% win) | -7.0% (340, 15% win) | -10.1% (340, 15% win) | -9.4% (340, 15% win) |
| d40_direct | -11.7% (350, 12% win) | -11.1% (350, 12% win) | -9.4% (350, 13% win) | -8.7% (350, 13% win) | -11.8% (350, 12% win) | -11.2% (350, 12% win) |
| d45_direct | -12.8% (364, 10% win) | -12.2% (364, 10% win) | -10.5% (364, 11% win) | -9.8% (364, 11% win) | -13.0% (364, 10% win) | -12.4% (364, 10% win) |
| d50_direct | -12.4% (375, 8% win) | -11.7% (375, 8% win) | -10.1% (375, 9% win) | -9.4% (375, 9% win) | -12.8% (375, 8% win) | -12.2% (375, 8% win) |
| d55_direct | -11.4% (382, 8% win) | -10.8% (382, 8% win) | -9.2% (382, 8% win) | -8.5% (382, 8% win) | -12.0% (382, 7% win) | -11.4% (382, 8% win) |
| d60_direct | -10.3% (370, 8% win) | -9.6% (370, 8% win) | -8.1% (370, 8% win) | -7.4% (370, 8% win) | -11.2% (370, 6% win) | -10.5% (370, 8% win) |
| d65_direct | -10.1% (294, 10% win) | -9.4% (294, 10% win) | -7.9% (294, 9% win) | -7.2% (294, 9% win) | -11.1% (294, 8% win) | -10.4% (294, 9% win) |
| d70_direct | -11.4% (222, 5% win) | -10.8% (222, 5% win) | -9.2% (222, 6% win) | -8.6% (222, 6% win) | -12.3% (222, 4% win) | -11.7% (222, 5% win) |
| d75_direct | -12.1% (157, 4% win) | -11.4% (157, 4% win) | -9.9% (157, 6% win) | -9.2% (157, 6% win) | -13.1% (157, 4% win) | -12.5% (157, 4% win) |
| d80_direct | -11.0% (101, 5% win) | -10.3% (101, 5% win) | -8.9% (101, 5% win) | -8.3% (101, 5% win) | -12.6% (101, 4% win) | -12.0% (101, 4% win) |
| d45_herstel5 | -10.2% (268, 14% win) | -9.5% (268, 14% win) | -7.8% (268, 14% win) | -7.2% (268, 14% win) | -10.3% (268, 14% win) | -9.6% (268, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (1091, 19% win) | -8.9% (1091, 20% win) | -7.1% (1091, 20% win) | -6.4% (1091, 21% win) | -9.2% (1091, 20% win) | -8.5% (1091, 20% win) |
| d35_direct | -10.0% (1196, 19% win) | -9.3% (1196, 19% win) | -7.5% (1196, 20% win) | -6.9% (1196, 20% win) | -9.7% (1196, 19% win) | -9.1% (1196, 19% win) |
| d40_direct | -10.3% (1301, 18% win) | -9.6% (1301, 18% win) | -7.9% (1301, 19% win) | -7.2% (1301, 20% win) | -10.2% (1301, 18% win) | -9.5% (1301, 18% win) |
| d45_direct | -10.1% (1375, 18% win) | -9.4% (1375, 18% win) | -7.7% (1375, 19% win) | -7.1% (1375, 20% win) | -10.2% (1375, 18% win) | -9.5% (1375, 18% win) |
| d50_direct | -9.8% (1468, 18% win) | -9.1% (1468, 18% win) | -7.5% (1468, 19% win) | -6.8% (1468, 20% win) | -10.1% (1468, 18% win) | -9.4% (1468, 18% win) |
| d55_direct | -8.5% (1561, 18% win) | -7.8% (1561, 19% win) | -6.2% (1561, 20% win) | -5.5% (1561, 20% win) | -9.1% (1561, 18% win) | -8.4% (1561, 18% win) |
| d60_direct | -8.2% (1596, 19% win) | -7.5% (1596, 19% win) | -5.9% (1596, 20% win) | -5.2% (1596, 20% win) | -9.0% (1596, 18% win) | -8.4% (1596, 19% win) |
| d65_direct | -7.6% (1460, 20% win) | -6.9% (1460, 20% win) | -5.5% (1460, 21% win) | -4.8% (1460, 22% win) | -8.8% (1460, 20% win) | -8.1% (1460, 20% win) |
| d70_direct | -7.1% (1322, 22% win) | -6.4% (1322, 23% win) | -5.0% (1322, 23% win) | -4.3% (1322, 24% win) | -8.8% (1322, 22% win) | -8.2% (1322, 22% win) |
| d75_direct | -7.9% (1161, 23% win) | -7.2% (1161, 24% win) | -5.9% (1161, 24% win) | -5.3% (1161, 24% win) | -10.3% (1161, 22% win) | -9.7% (1161, 22% win) |
| d80_direct | -7.9% (1019, 26% win) | -7.2% (1019, 26% win) | -6.2% (1019, 27% win) | -5.5% (1019, 27% win) | -11.7% (1019, 23% win) | -11.1% (1019, 23% win) |
| d45_herstel5 | -7.4% (1134, 22% win) | -6.7% (1134, 22% win) | -5.0% (1134, 23% win) | -4.3% (1134, 23% win) | -7.5% (1134, 22% win) | -6.8% (1134, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.1% (5352, 24% win) | -8.5% (5352, 24% win) | -6.8% (5352, 25% win) | -6.1% (5352, 25% win) | -9.4% (5352, 23% win) | -8.7% (5352, 24% win) |
| d35_direct | -9.4% (5245, 23% win) | -8.7% (5245, 23% win) | -7.1% (5245, 24% win) | -6.4% (5245, 24% win) | -9.8% (5245, 22% win) | -9.2% (5245, 23% win) |
| d40_direct | -9.7% (5132, 22% win) | -9.0% (5132, 22% win) | -7.4% (5132, 23% win) | -6.7% (5132, 23% win) | -10.2% (5132, 21% win) | -9.6% (5132, 22% win) |
| d45_direct | -9.1% (5011, 21% win) | -8.4% (5011, 22% win) | -6.9% (5011, 23% win) | -6.2% (5011, 23% win) | -10.0% (5011, 21% win) | -9.3% (5011, 21% win) |
| d50_direct | -9.4% (4904, 21% win) | -8.7% (4904, 21% win) | -7.2% (4904, 22% win) | -6.6% (4904, 22% win) | -10.5% (4904, 20% win) | -9.9% (4904, 20% win) |
| d55_direct | -9.4% (4730, 20% win) | -8.7% (4730, 20% win) | -7.3% (4730, 21% win) | -6.6% (4730, 21% win) | -10.7% (4730, 19% win) | -10.1% (4730, 19% win) |
| d60_direct | -8.9% (4394, 21% win) | -8.2% (4394, 21% win) | -6.8% (4394, 22% win) | -6.1% (4394, 22% win) | -10.6% (4394, 20% win) | -10.0% (4394, 20% win) |
| d65_direct | -8.7% (3931, 22% win) | -8.0% (3931, 22% win) | -6.7% (3931, 23% win) | -6.0% (3931, 24% win) | -10.9% (3931, 20% win) | -10.3% (3931, 21% win) |
| d70_direct | -8.2% (3475, 24% win) | -7.5% (3475, 24% win) | -6.4% (3475, 25% win) | -5.7% (3475, 25% win) | -11.2% (3475, 22% win) | -10.5% (3475, 22% win) |
| d75_direct | -8.7% (3058, 24% win) | -8.0% (3058, 24% win) | -7.1% (3058, 25% win) | -6.4% (3058, 25% win) | -12.7% (3058, 21% win) | -12.0% (3058, 22% win) |
| d80_direct | -8.8% (2652, 26% win) | -8.1% (2652, 27% win) | -7.5% (2652, 27% win) | -6.9% (2652, 27% win) | -14.5% (2652, 22% win) | -14.0% (2652, 22% win) |
| d45_herstel5 | -8.8% (4103, 25% win) | -8.1% (4103, 26% win) | -6.7% (4103, 26% win) | -6.0% (4103, 27% win) | -9.9% (4103, 24% win) | -9.3% (4103, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.2% (5011, 23% win) | -5.9% (5011, 23% win) | -6.5% (5011, 22% win) |
| schoon | -5.9% (4001, 24% win) | -5.8% (4001, 24% win) | -6.3% (4001, 24% win) |
| bundelgrafiek | -7.4% (1010, 17% win) | -6.5% (1010, 17% win) | -7.5% (1010, 15% win) |
| schoon+houders_ok | -7.1% (1375, 20% win) | -6.6% (1375, 19% win) | -6.4% (1375, 20% win) |
| schoon+houders_ok+final_stretch | -8.8% (571, 12% win) | -7.6% (571, 11% win) | -9.7% (571, 14% win) |
| volledige_screening+schoon | -9.8% (364, 11% win) | -8.8% (364, 9% win) | -10.8% (364, 15% win) |
| volledige_screening+schoon+x_link | -9.9% (271, 11% win) | -8.9% (271, 9% win) | -10.9% (271, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.5% (2133, 29% win); 1,3–2x: -7.6% (1868, 19% win); ≥ 2x (bundelgrafiek): -7.4% (1010, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.3% (3177, 29% win); 5–20%: -8.4% (874, 13% win); ≥ 20%: -7.3% (960, 11% win)

**top t.o.v. start:** 2–3x: -6.1% (2790, 22% win); 3–6x: -6.0% (1734, 24% win); ≥ 6x: -7.6% (487, 24% win)

**unieke kopers tot de top:** < 30: -5.3% (3174, 29% win); 30–100: -6.8% (1030, 12% win); ≥ 100: -9.2% (807, 13% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.7% (1243, 16% win); 1–2: -5.8% (2377, 25% win); ≥ 3 (trap): -6.5% (1391, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.6% (1217, 13% win); 10–25%: -7.5% (819, 12% win); ≥ 25%: -4.9% (2975, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.6% (3958, 25% win); 30 s–3 min: -8.2% (834, 15% win); ≥ 3 min (langzaam): -10.3% (219, 8% win)

**tijd van start tot top:** < 2 min: -5.9% (4121, 24% win); 2–10 min: -7.4% (712, 16% win); ≥ 10 min: -9.7% (178, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
