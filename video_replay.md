# Videostrategie op alle trades — 2026-09-13 12:36 UTC

Tokens sinds 2026-09-11 08:47 UTC: 36993 geschikt (≥ 2 uur oud, geen herstart), 29491 met trades, 5619 haalden 2x de startkoers, 4267 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1314 tokens. Houdercheck echt uitgevoerd bij 89% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1271, winkans 20%, EV per trade -7.0% (95%-marge -8.8% tot -5.2%), mediaan -10.6%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2931, winkans 24%, EV -6.8% (95%-marge -8.7% tot -4.8%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 14, winkans 14%, EV -9.6% (95%-marge -18.3% tot -1.0%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4267 | 40% | 76% | 37% |
| schoon | 3420 | 43% | 76% | 40% |
| bundelgrafiek | 847 | 30% | 78% | 25% |
| schoon+houders_ok | 1271 | 38% | 79% | 26% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.3% (4566, 25% win) | -6.4% (4468, 24% win) | -6.7% (4369, 23% win) | -6.6% (4267, 23% win) | -7.1% (4171, 22% win) | -7.0% (4018, 21% win) | -6.4% (3735, 22% win) | -6.4% (3338, 24% win) | -5.6% (2959, 26% win) | -6.6% (2608, 25% win) | -7.0% (2272, 27% win) | -6.5% (3512, 27% win) |
| schoon | -6.1% (3665, 26% win) | -5.9% (3594, 26% win) | -6.4% (3511, 25% win) | -6.3% (3420, 24% win) | -6.6% (3347, 24% win) | -6.9% (3219, 23% win) | -6.1% (2964, 24% win) | -5.6% (2640, 26% win) | -5.0% (2366, 28% win) | -6.1% (2095, 27% win) | -6.6% (1853, 29% win) | -6.0% (2941, 27% win) |
| bundelgrafiek | -6.9% (901, 22% win) | -8.3% (874, 19% win) | -8.2% (858, 18% win) | -7.8% (847, 17% win) | -9.1% (824, 15% win) | -7.3% (799, 15% win) | -7.6% (771, 15% win) | -9.4% (698, 15% win) | -8.0% (593, 18% win) | -8.5% (513, 18% win) | -8.7% (419, 19% win) | -8.8% (571, 23% win) |
| schoon+houders_ok | -6.4% (1020, 21% win) | -6.6% (1114, 21% win) | -7.0% (1205, 20% win) | -7.0% (1271, 20% win) | -6.8% (1353, 21% win) | -5.5% (1428, 20% win) | -5.0% (1456, 21% win) | -4.3% (1317, 23% win) | -3.8% (1199, 25% win) | -5.0% (1053, 26% win) | -5.3% (938, 28% win) | -4.1% (1056, 24% win) |
| schoon+houders_ok+final_stretch | -7.6% (427, 16% win) | -7.0% (464, 15% win) | -7.9% (493, 13% win) | -8.9% (513, 12% win) | -8.7% (533, 10% win) | -7.6% (553, 10% win) | -6.8% (538, 10% win) | -6.0% (412, 11% win) | -7.4% (308, 9% win) | -7.6% (200, 9% win) | -5.3% (122, 12% win) | -5.9% (397, 15% win) |
| volledige_screening+schoon | -7.7% (293, 15% win) | -6.3% (304, 16% win) | -8.3% (308, 14% win) | -10.0% (317, 11% win) | -9.9% (322, 9% win) | -8.6% (323, 8% win) | -7.0% (310, 8% win) | -7.0% (242, 9% win) | -8.5% (180, 6% win) | -8.8% (120, 8% win) | -9.1% (74, 4% win) | -7.5% (233, 14% win) |
| volledige_screening+schoon+x_link | -8.3% (228, 16% win) | -5.3% (237, 19% win) | -8.6% (236, 15% win) | -10.2% (239, 11% win) | -10.1% (237, 9% win) | -9.4% (237, 8% win) | -8.5% (230, 7% win) | -8.5% (179, 6% win) | -8.6% (134, 4% win) | -8.7% (93, 6% win) | -8.7% (58, 2% win) | -7.9% (169, 13% win) |

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
| alle | -5.8% (4566, 30% win) | -5.8% (4468, 29% win) | -6.1% (4369, 28% win) | -6.3% (4267, 28% win) | -7.3% (4171, 26% win) | -6.8% (4018, 26% win) | -6.4% (3735, 27% win) | -6.7% (3338, 28% win) | -6.2% (2959, 31% win) | -6.6% (2608, 32% win) | -7.7% (2272, 33% win) |
| schoon | -5.6% (3665, 31% win) | -5.4% (3594, 31% win) | -5.9% (3511, 30% win) | -6.1% (3420, 30% win) | -7.3% (3347, 27% win) | -6.9% (3219, 28% win) | -6.2% (2964, 30% win) | -6.2% (2640, 31% win) | -5.7% (2366, 34% win) | -5.9% (2095, 34% win) | -7.1% (1853, 35% win) |
| bundelgrafiek | -6.5% (901, 26% win) | -7.5% (874, 24% win) | -6.9% (858, 22% win) | -7.1% (847, 21% win) | -7.6% (824, 20% win) | -6.4% (799, 20% win) | -6.8% (771, 18% win) | -8.6% (698, 17% win) | -8.6% (593, 20% win) | -9.1% (513, 22% win) | -10.5% (419, 23% win) |
| schoon+houders_ok | -6.3% (1020, 28% win) | -6.3% (1114, 28% win) | -6.3% (1205, 28% win) | -6.7% (1271, 28% win) | -7.0% (1353, 27% win) | -5.5% (1428, 28% win) | -4.9% (1456, 28% win) | -4.7% (1317, 30% win) | -3.7% (1199, 34% win) | -4.6% (1053, 35% win) | -6.9% (938, 34% win) |
| schoon+houders_ok+final_stretch | -7.0% (427, 24% win) | -6.7% (464, 24% win) | -6.9% (493, 24% win) | -9.0% (513, 21% win) | -10.3% (533, 17% win) | -9.2% (553, 18% win) | -6.2% (538, 21% win) | -6.7% (412, 22% win) | -8.2% (308, 23% win) | -7.5% (200, 26% win) | -6.6% (122, 25% win) |
| volledige_screening+schoon | -7.0% (293, 25% win) | -6.5% (304, 25% win) | -7.4% (308, 26% win) | -10.2% (317, 20% win) | -11.6% (322, 16% win) | -10.7% (323, 17% win) | -7.3% (310, 18% win) | -8.2% (242, 19% win) | -11.3% (180, 16% win) | -10.9% (120, 17% win) | -12.4% (74, 12% win) |
| volledige_screening+schoon+x_link | -7.2% (228, 25% win) | -5.8% (237, 26% win) | -7.5% (236, 25% win) | -10.7% (239, 20% win) | -12.4% (237, 14% win) | -10.9% (237, 15% win) | -7.9% (230, 16% win) | -8.6% (179, 17% win) | -9.9% (134, 17% win) | -11.1% (93, 16% win) | -12.4% (58, 9% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 317 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 24% | -8.4% | 25% |
| +15% | 42% | 19% | -8.6% | 21% |
| +20% | 38% | 16% | -8.6% | 18% |
| +25% | 33% | 13% | -8.9% | 16% |
| +30% | 31% | 12% | -9.0% | 15% |
| +35% | 28% | 11% | -9.2% | 14% |
| +45% | 24% | 8% | -10.0% | 11% |
| +60% | 20% | 7% | -9.8% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1271 instappen, mediane hoogste stijging +21.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.4% | 31% |
| +15% | 54% | 28% | -5.6% | 28% |
| +20% | 51% | 24% | -5.7% | 26% |
| +25% | 48% | 21% | -5.9% | 24% |
| +30% | 45% | 20% | -6.1% | 24% |
| +35% | 42% | 17% | -6.3% | 22% |
| +45% | 38% | 14% | -7.0% | 20% |
| +60% | 32% | 11% | -6.9% | 19% |

**filter `alle`** — variant `d45_direct`, 4267 instappen, mediane hoogste stijging +22.9%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.8% | 30% |
| +15% | 55% | 30% | -6.0% | 28% |
| +20% | 52% | 27% | -6.2% | 27% |
| +25% | 49% | 24% | -6.2% | 26% |
| +30% | 46% | 22% | -6.4% | 25% |
| +35% | 44% | 19% | -6.5% | 24% |
| +45% | 39% | 16% | -6.6% | 23% |
| +60% | 35% | 13% | -6.5% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.8% (293, 14% win) | -10.1% (293, 14% win) | -8.4% (293, 15% win) | -7.7% (293, 15% win) | -10.8% (293, 14% win) | -10.1% (293, 14% win) |
| d35_direct | -9.4% (304, 16% win) | -8.7% (304, 16% win) | -7.0% (304, 16% win) | -6.3% (304, 16% win) | -9.5% (304, 16% win) | -8.8% (304, 16% win) |
| d40_direct | -11.4% (308, 13% win) | -10.7% (308, 13% win) | -9.0% (308, 14% win) | -8.3% (308, 14% win) | -11.5% (308, 13% win) | -10.8% (308, 13% win) |
| d45_direct | -13.0% (317, 10% win) | -12.4% (317, 10% win) | -10.7% (317, 11% win) | -10.0% (317, 11% win) | -13.2% (317, 10% win) | -12.6% (317, 10% win) |
| d50_direct | -12.8% (322, 9% win) | -12.2% (322, 9% win) | -10.5% (322, 9% win) | -9.9% (322, 9% win) | -13.2% (322, 8% win) | -12.6% (322, 8% win) |
| d55_direct | -11.5% (323, 8% win) | -10.9% (323, 8% win) | -9.3% (323, 8% win) | -8.6% (323, 8% win) | -12.2% (323, 7% win) | -11.5% (323, 8% win) |
| d60_direct | -9.9% (310, 8% win) | -9.3% (310, 8% win) | -7.7% (310, 8% win) | -7.0% (310, 8% win) | -10.9% (310, 7% win) | -10.2% (310, 8% win) |
| d65_direct | -9.9% (242, 10% win) | -9.2% (242, 10% win) | -7.7% (242, 9% win) | -7.0% (242, 9% win) | -10.9% (242, 8% win) | -10.3% (242, 9% win) |
| d70_direct | -11.4% (180, 6% win) | -10.7% (180, 6% win) | -9.2% (180, 6% win) | -8.5% (180, 6% win) | -12.4% (180, 4% win) | -11.8% (180, 5% win) |
| d75_direct | -11.7% (120, 6% win) | -11.0% (120, 6% win) | -9.5% (120, 8% win) | -8.8% (120, 8% win) | -12.9% (120, 5% win) | -12.3% (120, 5% win) |
| d80_direct | -11.8% (74, 4% win) | -11.1% (74, 4% win) | -9.8% (74, 4% win) | -9.1% (74, 4% win) | -13.7% (74, 3% win) | -13.1% (74, 3% win) |
| d45_herstel5 | -10.5% (233, 14% win) | -9.8% (233, 14% win) | -8.1% (233, 14% win) | -7.5% (233, 14% win) | -10.6% (233, 14% win) | -9.9% (233, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (1020, 19% win) | -8.9% (1020, 20% win) | -7.1% (1020, 21% win) | -6.4% (1020, 21% win) | -9.2% (1020, 20% win) | -8.5% (1020, 20% win) |
| d35_direct | -9.7% (1114, 19% win) | -9.0% (1114, 19% win) | -7.3% (1114, 21% win) | -6.6% (1114, 21% win) | -9.5% (1114, 19% win) | -8.8% (1114, 20% win) |
| d40_direct | -10.1% (1205, 19% win) | -9.4% (1205, 19% win) | -7.7% (1205, 20% win) | -7.0% (1205, 20% win) | -10.0% (1205, 18% win) | -9.4% (1205, 19% win) |
| d45_direct | -10.0% (1271, 18% win) | -9.3% (1271, 19% win) | -7.7% (1271, 20% win) | -7.0% (1271, 20% win) | -10.1% (1271, 18% win) | -9.5% (1271, 19% win) |
| d50_direct | -9.8% (1353, 19% win) | -9.1% (1353, 19% win) | -7.4% (1353, 20% win) | -6.8% (1353, 21% win) | -10.0% (1353, 18% win) | -9.4% (1353, 19% win) |
| d55_direct | -8.4% (1428, 19% win) | -7.7% (1428, 19% win) | -6.2% (1428, 20% win) | -5.5% (1428, 20% win) | -9.0% (1428, 18% win) | -8.4% (1428, 19% win) |
| d60_direct | -7.9% (1456, 19% win) | -7.2% (1456, 20% win) | -5.7% (1456, 21% win) | -5.0% (1456, 21% win) | -8.8% (1456, 19% win) | -8.2% (1456, 19% win) |
| d65_direct | -7.2% (1317, 21% win) | -6.5% (1317, 22% win) | -5.0% (1317, 23% win) | -4.3% (1317, 23% win) | -8.4% (1317, 21% win) | -7.8% (1317, 21% win) |
| d70_direct | -6.6% (1199, 24% win) | -5.9% (1199, 24% win) | -4.5% (1199, 25% win) | -3.8% (1199, 25% win) | -8.4% (1199, 23% win) | -7.7% (1199, 24% win) |
| d75_direct | -7.6% (1053, 25% win) | -6.9% (1053, 26% win) | -5.7% (1053, 26% win) | -5.0% (1053, 26% win) | -10.2% (1053, 23% win) | -9.5% (1053, 24% win) |
| d80_direct | -7.6% (938, 27% win) | -6.9% (938, 28% win) | -6.0% (938, 28% win) | -5.3% (938, 28% win) | -11.7% (938, 24% win) | -11.1% (938, 24% win) |
| d45_herstel5 | -7.1% (1056, 23% win) | -6.4% (1056, 23% win) | -4.8% (1056, 24% win) | -4.1% (1056, 24% win) | -7.2% (1056, 23% win) | -6.6% (1056, 23% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.3% (4566, 24% win) | -8.6% (4566, 24% win) | -7.0% (4566, 25% win) | -6.3% (4566, 25% win) | -9.5% (4566, 23% win) | -8.9% (4566, 24% win) |
| d35_direct | -9.4% (4468, 23% win) | -8.7% (4468, 23% win) | -7.1% (4468, 24% win) | -6.4% (4468, 24% win) | -9.8% (4468, 22% win) | -9.2% (4468, 23% win) |
| d40_direct | -9.7% (4369, 22% win) | -9.0% (4369, 22% win) | -7.4% (4369, 23% win) | -6.7% (4369, 23% win) | -10.3% (4369, 21% win) | -9.6% (4369, 22% win) |
| d45_direct | -9.5% (4267, 21% win) | -8.8% (4267, 22% win) | -7.2% (4267, 22% win) | -6.6% (4267, 23% win) | -10.3% (4267, 20% win) | -9.7% (4267, 21% win) |
| d50_direct | -10.0% (4171, 20% win) | -9.3% (4171, 21% win) | -7.8% (4171, 22% win) | -7.1% (4171, 22% win) | -11.0% (4171, 20% win) | -10.4% (4171, 20% win) |
| d55_direct | -9.8% (4018, 20% win) | -9.1% (4018, 20% win) | -7.6% (4018, 21% win) | -7.0% (4018, 21% win) | -11.1% (4018, 19% win) | -10.4% (4018, 19% win) |
| d60_direct | -9.1% (3735, 21% win) | -8.4% (3735, 21% win) | -7.1% (3735, 22% win) | -6.4% (3735, 22% win) | -10.8% (3735, 20% win) | -10.2% (3735, 20% win) |
| d65_direct | -9.0% (3338, 22% win) | -8.3% (3338, 22% win) | -7.1% (3338, 23% win) | -6.4% (3338, 24% win) | -11.2% (3338, 20% win) | -10.6% (3338, 21% win) |
| d70_direct | -8.1% (2959, 24% win) | -7.4% (2959, 25% win) | -6.3% (2959, 25% win) | -5.6% (2959, 26% win) | -11.2% (2959, 22% win) | -10.5% (2959, 23% win) |
| d75_direct | -8.9% (2608, 24% win) | -8.2% (2608, 24% win) | -7.2% (2608, 25% win) | -6.6% (2608, 25% win) | -12.9% (2608, 21% win) | -12.3% (2608, 22% win) |
| d80_direct | -8.9% (2272, 27% win) | -8.2% (2272, 27% win) | -7.7% (2272, 27% win) | -7.0% (2272, 27% win) | -14.9% (2272, 22% win) | -14.3% (2272, 22% win) |
| d45_herstel5 | -9.3% (3512, 25% win) | -8.6% (3512, 25% win) | -7.1% (3512, 26% win) | -6.5% (3512, 27% win) | -10.4% (3512, 24% win) | -9.8% (3512, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.6% (4267, 23% win) | -6.2% (4267, 22% win) | -6.7% (4267, 22% win) |
| schoon | -6.3% (3420, 24% win) | -6.1% (3420, 24% win) | -6.2% (3420, 24% win) |
| bundelgrafiek | -7.8% (847, 17% win) | -6.8% (847, 17% win) | -8.6% (847, 15% win) |
| schoon+houders_ok | -7.0% (1271, 20% win) | -6.6% (1271, 20% win) | -6.1% (1271, 21% win) |
| schoon+houders_ok+final_stretch | -8.9% (513, 12% win) | -7.6% (513, 11% win) | -9.7% (513, 14% win) |
| volledige_screening+schoon | -10.0% (317, 11% win) | -8.8% (317, 9% win) | -10.8% (317, 14% win) |
| volledige_screening+schoon+x_link | -10.2% (239, 11% win) | -8.9% (239, 9% win) | -11.1% (239, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.7% (1832, 30% win); 1,3–2x: -8.1% (1588, 18% win); ≥ 2x (bundelgrafiek): -7.8% (847, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.5% (2757, 29% win); 5–20%: -8.7% (760, 13% win); ≥ 20%: -8.5% (750, 10% win)

**top t.o.v. start:** 2–3x: -6.2% (2390, 22% win); 3–6x: -6.7% (1464, 24% win); ≥ 6x: -8.7% (413, 22% win)

**unieke kopers tot de top:** < 30: -5.4% (2761, 29% win); 30–100: -7.5% (827, 11% win); ≥ 100: -10.0% (679, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.8% (1058, 16% win); 1–2: -5.9% (2033, 25% win); ≥ 3 (trap): -6.7% (1176, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.4% (1027, 12% win); 10–25%: -7.4% (661, 12% win); ≥ 25%: -5.2% (2579, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (3403, 25% win); 30 s–3 min: -8.7% (682, 15% win); ≥ 3 min (langzaam): -9.8% (182, 7% win)

**tijd van start tot top:** < 2 min: -6.3% (3549, 24% win); 2–10 min: -7.4% (573, 16% win); ≥ 10 min: -9.2% (145, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
