# Videostrategie op alle trades — 2026-09-13 23:10 UTC

Tokens sinds 2026-09-11 08:47 UTC: 48970 geschikt (≥ 2 uur oud, geen herstart), 38358 met trades, 6965 haalden 2x de startkoers, 5324 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1666 tokens. Houdercheck echt uitgevoerd bij 91% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1407, winkans 20%, EV per trade -7.1% (95%-marge -8.8% tot -5.5%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 3767, winkans 24%, EV -6.7% (95%-marge -8.5% tot -5.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 88, winkans 18%, EV -9.6% (95%-marge -14.0% tot -5.1%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 5324 | 40% | 76% | 37% |
| schoon | 4256 | 43% | 76% | 40% |
| bundelgrafiek | 1068 | 29% | 78% | 24% |
| schoon+houders_ok | 1407 | 37% | 79% | 24% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.4% (5691, 25% win) | -6.5% (5573, 24% win) | -6.7% (5454, 23% win) | -6.4% (5324, 23% win) | -6.9% (5206, 22% win) | -6.9% (5020, 21% win) | -6.4% (4668, 22% win) | -6.1% (4177, 24% win) | -5.5% (3698, 25% win) | -6.3% (3254, 25% win) | -6.8% (2833, 27% win) | -6.0% (4382, 27% win) |
| schoon | -6.4% (4545, 26% win) | -6.2% (4462, 25% win) | -6.4% (4369, 24% win) | -6.2% (4256, 24% win) | -6.3% (4163, 24% win) | -6.7% (4007, 23% win) | -6.0% (3695, 24% win) | -5.3% (3298, 26% win) | -4.9% (2947, 27% win) | -5.7% (2607, 27% win) | -6.6% (2309, 29% win) | -5.6% (3669, 27% win) |
| bundelgrafiek | -6.5% (1146, 24% win) | -7.5% (1111, 21% win) | -7.8% (1085, 18% win) | -7.2% (1068, 18% win) | -9.0% (1043, 15% win) | -7.7% (1013, 15% win) | -7.8% (973, 15% win) | -9.2% (879, 14% win) | -7.7% (751, 17% win) | -8.5% (647, 17% win) | -8.1% (524, 19% win) | -7.8% (713, 23% win) |
| schoon+houders_ok | -6.4% (1104, 21% win) | -6.9% (1210, 20% win) | -7.2% (1327, 19% win) | -7.1% (1407, 20% win) | -6.9% (1505, 20% win) | -5.6% (1600, 20% win) | -5.2% (1639, 20% win) | -4.9% (1493, 21% win) | -4.4% (1355, 24% win) | -5.3% (1183, 24% win) | -5.5% (1037, 27% win) | -4.3% (1159, 23% win) |
| schoon+houders_ok+final_stretch | -7.0% (472, 17% win) | -7.3% (516, 15% win) | -8.1% (563, 12% win) | -8.9% (593, 12% win) | -8.6% (627, 10% win) | -7.6% (655, 10% win) | -6.8% (646, 10% win) | -6.5% (508, 10% win) | -7.7% (392, 8% win) | -8.0% (264, 7% win) | -5.4% (164, 11% win) | -5.9% (460, 15% win) |
| volledige_screening+schoon | -6.8% (332, 17% win) | -6.9% (347, 15% win) | -8.6% (362, 13% win) | -9.8% (380, 10% win) | -9.4% (394, 9% win) | -8.5% (397, 8% win) | -7.2% (384, 8% win) | -7.2% (303, 9% win) | -8.6% (231, 6% win) | -8.9% (164, 6% win) | -8.3% (104, 5% win) | -7.4% (279, 14% win) |
| volledige_screening+schoon+x_link | -7.3% (254, 17% win) | -5.9% (266, 18% win) | -8.8% (272, 14% win) | -9.8% (277, 11% win) | -9.6% (277, 9% win) | -9.1% (279, 8% win) | -8.6% (272, 7% win) | -8.5% (219, 7% win) | -8.9% (164, 5% win) | -9.1% (119, 5% win) | -9.2% (76, 1% win) | -7.4% (198, 14% win) |

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
| alle | -6.1% (5691, 30% win) | -6.3% (5573, 29% win) | -6.4% (5454, 28% win) | -6.4% (5324, 28% win) | -7.2% (5206, 26% win) | -6.9% (5020, 26% win) | -6.6% (4668, 27% win) | -6.5% (4177, 28% win) | -6.2% (3698, 31% win) | -6.3% (3254, 32% win) | -7.5% (2833, 33% win) |
| schoon | -6.1% (4545, 31% win) | -6.1% (4462, 30% win) | -6.2% (4369, 30% win) | -6.2% (4256, 29% win) | -7.1% (4163, 28% win) | -6.9% (4007, 28% win) | -6.4% (3695, 29% win) | -5.8% (3298, 31% win) | -5.5% (2947, 34% win) | -5.6% (2607, 34% win) | -6.9% (2309, 35% win) |
| bundelgrafiek | -6.3% (1146, 27% win) | -7.3% (1111, 25% win) | -6.9% (1085, 22% win) | -6.8% (1068, 21% win) | -7.7% (1043, 20% win) | -6.7% (1013, 19% win) | -7.3% (973, 18% win) | -9.0% (879, 17% win) | -8.9% (751, 20% win) | -9.0% (647, 22% win) | -10.2% (524, 23% win) |
| schoon+houders_ok | -6.3% (1104, 28% win) | -6.4% (1210, 28% win) | -6.5% (1327, 27% win) | -6.9% (1407, 28% win) | -7.2% (1505, 26% win) | -5.9% (1600, 26% win) | -5.3% (1639, 27% win) | -5.2% (1493, 29% win) | -4.5% (1355, 32% win) | -5.0% (1183, 33% win) | -6.7% (1037, 34% win) |
| schoon+houders_ok+final_stretch | -6.6% (472, 25% win) | -6.9% (516, 24% win) | -7.4% (563, 23% win) | -9.2% (593, 21% win) | -10.2% (627, 17% win) | -9.3% (655, 18% win) | -7.0% (646, 20% win) | -7.5% (508, 22% win) | -8.6% (392, 22% win) | -7.1% (264, 26% win) | -5.2% (164, 27% win) |
| volledige_screening+schoon | -6.8% (332, 26% win) | -7.1% (347, 24% win) | -8.3% (362, 24% win) | -10.4% (380, 20% win) | -11.1% (394, 17% win) | -10.5% (397, 17% win) | -7.9% (384, 18% win) | -8.4% (303, 19% win) | -11.2% (231, 16% win) | -9.5% (164, 20% win) | -8.6% (104, 19% win) |
| volledige_screening+schoon+x_link | -6.9% (254, 26% win) | -6.3% (266, 25% win) | -8.4% (272, 23% win) | -10.9% (277, 19% win) | -12.0% (277, 14% win) | -10.4% (279, 16% win) | -7.8% (272, 18% win) | -8.4% (219, 18% win) | -10.1% (164, 17% win) | -9.3% (119, 19% win) | -8.9% (76, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 380 instappen, mediane hoogste stijging +8.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -7.9% | 26% |
| +15% | 43% | 20% | -8.0% | 22% |
| +20% | 40% | 18% | -8.0% | 20% |
| +25% | 34% | 15% | -8.5% | 17% |
| +30% | 32% | 13% | -8.6% | 15% |
| +35% | 29% | 12% | -8.6% | 14% |
| +45% | 24% | 8% | -9.8% | 10% |
| +60% | 20% | 7% | -9.5% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1407 instappen, mediane hoogste stijging +20.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 58% | 33% | -5.5% | 31% |
| +15% | 54% | 27% | -5.7% | 28% |
| +20% | 51% | 24% | -5.8% | 26% |
| +25% | 47% | 21% | -6.0% | 24% |
| +30% | 45% | 19% | -6.2% | 23% |
| +35% | 42% | 17% | -6.4% | 22% |
| +45% | 37% | 13% | -7.1% | 20% |
| +60% | 32% | 11% | -7.0% | 18% |

**filter `alle`** — variant `d45_direct`, 5324 instappen, mediane hoogste stijging +22.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.7% | 30% |
| +15% | 55% | 30% | -5.8% | 28% |
| +20% | 52% | 26% | -5.9% | 27% |
| +25% | 49% | 24% | -6.0% | 26% |
| +30% | 46% | 21% | -6.1% | 25% |
| +35% | 44% | 19% | -6.3% | 24% |
| +45% | 39% | 16% | -6.4% | 23% |
| +60% | 35% | 13% | -6.2% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.8% (332, 15% win) | -9.1% (332, 16% win) | -7.4% (332, 16% win) | -6.8% (332, 17% win) | -9.8% (332, 15% win) | -9.2% (332, 15% win) |
| d35_direct | -10.0% (347, 15% win) | -9.3% (347, 15% win) | -7.6% (347, 15% win) | -6.9% (347, 15% win) | -10.0% (347, 15% win) | -9.4% (347, 15% win) |
| d40_direct | -11.7% (362, 12% win) | -11.0% (362, 12% win) | -9.3% (362, 13% win) | -8.6% (362, 13% win) | -11.7% (362, 12% win) | -11.1% (362, 12% win) |
| d45_direct | -12.8% (380, 10% win) | -12.1% (380, 10% win) | -10.4% (380, 10% win) | -9.8% (380, 10% win) | -12.9% (380, 10% win) | -12.3% (380, 10% win) |
| d50_direct | -12.3% (394, 8% win) | -11.7% (394, 8% win) | -10.0% (394, 9% win) | -9.4% (394, 9% win) | -12.8% (394, 8% win) | -12.1% (394, 8% win) |
| d55_direct | -11.4% (397, 8% win) | -10.8% (397, 8% win) | -9.2% (397, 8% win) | -8.5% (397, 8% win) | -12.0% (397, 7% win) | -11.4% (397, 8% win) |
| d60_direct | -10.1% (384, 8% win) | -9.4% (384, 8% win) | -7.9% (384, 8% win) | -7.2% (384, 8% win) | -11.0% (384, 7% win) | -10.4% (384, 8% win) |
| d65_direct | -10.1% (303, 10% win) | -9.4% (303, 10% win) | -7.8% (303, 9% win) | -7.2% (303, 9% win) | -11.0% (303, 8% win) | -10.4% (303, 9% win) |
| d70_direct | -11.5% (231, 5% win) | -10.8% (231, 5% win) | -9.3% (231, 6% win) | -8.6% (231, 6% win) | -12.4% (231, 4% win) | -11.8% (231, 5% win) |
| d75_direct | -11.8% (164, 5% win) | -11.1% (164, 5% win) | -9.6% (164, 6% win) | -8.9% (164, 6% win) | -12.8% (164, 4% win) | -12.2% (164, 4% win) |
| d80_direct | -11.0% (104, 5% win) | -10.3% (104, 5% win) | -8.9% (104, 5% win) | -8.3% (104, 5% win) | -12.6% (104, 4% win) | -12.0% (104, 4% win) |
| d45_herstel5 | -10.4% (279, 14% win) | -9.8% (279, 14% win) | -8.1% (279, 14% win) | -7.4% (279, 14% win) | -10.5% (279, 14% win) | -9.8% (279, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.5% (1104, 19% win) | -8.8% (1104, 20% win) | -7.1% (1104, 20% win) | -6.4% (1104, 21% win) | -9.2% (1104, 20% win) | -8.5% (1104, 20% win) |
| d35_direct | -10.0% (1210, 18% win) | -9.3% (1210, 19% win) | -7.6% (1210, 20% win) | -6.9% (1210, 20% win) | -9.8% (1210, 18% win) | -9.1% (1210, 19% win) |
| d40_direct | -10.3% (1327, 18% win) | -9.6% (1327, 18% win) | -7.9% (1327, 19% win) | -7.2% (1327, 19% win) | -10.2% (1327, 18% win) | -9.6% (1327, 18% win) |
| d45_direct | -10.2% (1407, 17% win) | -9.5% (1407, 18% win) | -7.8% (1407, 19% win) | -7.1% (1407, 20% win) | -10.3% (1407, 17% win) | -9.6% (1407, 18% win) |
| d50_direct | -9.9% (1505, 18% win) | -9.2% (1505, 18% win) | -7.6% (1505, 19% win) | -6.9% (1505, 20% win) | -10.2% (1505, 18% win) | -9.5% (1505, 18% win) |
| d55_direct | -8.6% (1600, 18% win) | -7.9% (1600, 18% win) | -6.3% (1600, 19% win) | -5.6% (1600, 20% win) | -9.2% (1600, 18% win) | -8.5% (1600, 18% win) |
| d60_direct | -8.1% (1639, 19% win) | -7.4% (1639, 19% win) | -5.9% (1639, 20% win) | -5.2% (1639, 20% win) | -9.0% (1639, 18% win) | -8.3% (1639, 19% win) |
| d65_direct | -7.8% (1493, 20% win) | -7.1% (1493, 20% win) | -5.6% (1493, 21% win) | -4.9% (1493, 21% win) | -8.9% (1493, 19% win) | -8.3% (1493, 20% win) |
| d70_direct | -7.2% (1355, 22% win) | -6.5% (1355, 22% win) | -5.1% (1355, 23% win) | -4.4% (1355, 24% win) | -8.9% (1355, 21% win) | -8.2% (1355, 22% win) |
| d75_direct | -7.9% (1183, 23% win) | -7.2% (1183, 24% win) | -6.0% (1183, 24% win) | -5.3% (1183, 24% win) | -10.3% (1183, 22% win) | -9.7% (1183, 22% win) |
| d80_direct | -7.9% (1037, 26% win) | -7.2% (1037, 26% win) | -6.2% (1037, 26% win) | -5.5% (1037, 27% win) | -11.7% (1037, 23% win) | -11.0% (1037, 23% win) |
| d45_herstel5 | -7.4% (1159, 22% win) | -6.7% (1159, 22% win) | -5.0% (1159, 23% win) | -4.3% (1159, 23% win) | -7.5% (1159, 22% win) | -6.8% (1159, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.4% (5691, 24% win) | -8.7% (5691, 24% win) | -7.1% (5691, 25% win) | -6.4% (5691, 25% win) | -9.6% (5691, 23% win) | -9.0% (5691, 24% win) |
| d35_direct | -9.4% (5573, 23% win) | -8.7% (5573, 23% win) | -7.1% (5573, 24% win) | -6.5% (5573, 24% win) | -9.8% (5573, 22% win) | -9.2% (5573, 23% win) |
| d40_direct | -9.7% (5454, 22% win) | -9.0% (5454, 22% win) | -7.4% (5454, 23% win) | -6.7% (5454, 23% win) | -10.2% (5454, 21% win) | -9.6% (5454, 22% win) |
| d45_direct | -9.3% (5324, 21% win) | -8.6% (5324, 22% win) | -7.1% (5324, 22% win) | -6.4% (5324, 23% win) | -10.1% (5324, 21% win) | -9.5% (5324, 21% win) |
| d50_direct | -9.7% (5206, 20% win) | -9.0% (5206, 21% win) | -7.5% (5206, 22% win) | -6.9% (5206, 22% win) | -10.8% (5206, 20% win) | -10.1% (5206, 20% win) |
| d55_direct | -9.7% (5020, 20% win) | -9.0% (5020, 20% win) | -7.6% (5020, 21% win) | -6.9% (5020, 21% win) | -11.0% (5020, 19% win) | -10.4% (5020, 19% win) |
| d60_direct | -9.1% (4668, 21% win) | -8.5% (4668, 21% win) | -7.1% (4668, 22% win) | -6.4% (4668, 22% win) | -10.9% (4668, 19% win) | -10.2% (4668, 20% win) |
| d65_direct | -8.8% (4177, 22% win) | -8.1% (4177, 22% win) | -6.8% (4177, 23% win) | -6.1% (4177, 24% win) | -11.0% (4177, 20% win) | -10.4% (4177, 21% win) |
| d70_direct | -8.0% (3698, 24% win) | -7.3% (3698, 24% win) | -6.2% (3698, 25% win) | -5.5% (3698, 25% win) | -11.0% (3698, 22% win) | -10.4% (3698, 22% win) |
| d75_direct | -8.6% (3254, 24% win) | -7.9% (3254, 24% win) | -7.0% (3254, 25% win) | -6.3% (3254, 25% win) | -12.6% (3254, 21% win) | -12.0% (3254, 22% win) |
| d80_direct | -8.8% (2833, 26% win) | -8.1% (2833, 27% win) | -7.5% (2833, 27% win) | -6.8% (2833, 27% win) | -14.5% (2833, 22% win) | -14.0% (2833, 23% win) |
| d45_herstel5 | -8.8% (4382, 25% win) | -8.1% (4382, 26% win) | -6.6% (4382, 26% win) | -6.0% (4382, 27% win) | -9.9% (4382, 24% win) | -9.3% (4382, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.4% (5324, 23% win) | -6.0% (5324, 23% win) | -6.6% (5324, 22% win) |
| schoon | -6.2% (4256, 24% win) | -6.0% (4256, 24% win) | -6.3% (4256, 24% win) |
| bundelgrafiek | -7.2% (1068, 18% win) | -6.4% (1068, 18% win) | -7.6% (1068, 15% win) |
| schoon+houders_ok | -7.1% (1407, 20% win) | -6.7% (1407, 19% win) | -6.2% (1407, 20% win) |
| schoon+houders_ok+final_stretch | -8.9% (593, 12% win) | -7.6% (593, 10% win) | -9.6% (593, 14% win) |
| volledige_screening+schoon | -9.8% (380, 10% win) | -8.7% (380, 9% win) | -10.9% (380, 14% win) |
| volledige_screening+schoon+x_link | -9.8% (277, 11% win) | -8.6% (277, 9% win) | -10.8% (277, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.9% (2281, 29% win); 1,3–2x: -7.7% (1975, 19% win); ≥ 2x (bundelgrafiek): -7.2% (1068, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.5% (3381, 29% win); 5–20%: -8.6% (918, 13% win); ≥ 20%: -7.5% (1025, 11% win)

**top t.o.v. start:** 2–3x: -6.5% (2976, 22% win); 3–6x: -6.0% (1836, 24% win); ≥ 6x: -7.5% (512, 24% win)

**unieke kopers tot de top:** < 30: -5.5% (3371, 29% win); 30–100: -7.0% (1099, 12% win); ≥ 100: -9.0% (854, 13% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.8% (1302, 16% win); 1–2: -6.1% (2539, 24% win); ≥ 3 (trap): -6.5% (1483, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.6% (1283, 12% win); 10–25%: -7.4% (870, 13% win); ≥ 25%: -5.2% (3171, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.7% (4198, 26% win); 30 s–3 min: -8.4% (895, 14% win); ≥ 3 min (langzaam): -10.4% (231, 7% win)

**tijd van start tot top:** < 2 min: -6.1% (4381, 24% win); 2–10 min: -7.2% (751, 16% win); ≥ 10 min: -9.7% (192, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
