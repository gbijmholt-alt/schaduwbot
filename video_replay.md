# Videostrategie op alle trades — 2026-09-13 13:21 UTC

Tokens sinds 2026-09-11 08:47 UTC: 37644 geschikt (≥ 2 uur oud, geen herstart), 29997 met trades, 5690 haalden 2x de startkoers, 4317 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1332 tokens. Houdercheck echt uitgevoerd bij 89% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1277, winkans 20%, EV per trade -7.0% (95%-marge -8.8% tot -5.2%), mediaan -10.6%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2976, winkans 24%, EV -6.9% (95%-marge -8.8% tot -5.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 17, winkans 12%, EV -10.0% (95%-marge -17.1% tot -2.8%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4317 | 40% | 76% | 37% |
| schoon | 3465 | 43% | 76% | 40% |
| bundelgrafiek | 852 | 30% | 78% | 25% |
| schoon+houders_ok | 1277 | 38% | 79% | 26% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.2% (4622, 25% win) | -6.3% (4523, 24% win) | -6.7% (4424, 23% win) | -6.6% (4317, 23% win) | -7.2% (4220, 22% win) | -7.0% (4062, 21% win) | -6.4% (3773, 22% win) | -6.3% (3370, 24% win) | -5.5% (2984, 26% win) | -6.6% (2632, 25% win) | -7.1% (2292, 27% win) | -6.5% (3547, 26% win) |
| schoon | -6.0% (3714, 26% win) | -5.9% (3642, 26% win) | -6.3% (3559, 25% win) | -6.3% (3465, 24% win) | -6.7% (3391, 23% win) | -6.8% (3258, 23% win) | -6.1% (2998, 24% win) | -5.4% (2668, 26% win) | -4.9% (2388, 28% win) | -6.1% (2116, 27% win) | -6.7% (1870, 29% win) | -6.0% (2973, 27% win) |
| bundelgrafiek | -7.0% (908, 22% win) | -8.4% (881, 19% win) | -8.4% (865, 18% win) | -8.0% (852, 16% win) | -9.2% (829, 15% win) | -7.5% (804, 15% win) | -7.7% (775, 15% win) | -9.6% (702, 15% win) | -8.0% (596, 18% win) | -8.7% (516, 18% win) | -8.9% (422, 19% win) | -9.0% (574, 22% win) |
| schoon+houders_ok | -6.4% (1022, 21% win) | -6.6% (1117, 21% win) | -7.0% (1209, 20% win) | -7.0% (1277, 20% win) | -6.8% (1360, 21% win) | -5.5% (1436, 20% win) | -5.1% (1466, 21% win) | -4.4% (1329, 23% win) | -3.9% (1207, 25% win) | -5.0% (1061, 26% win) | -5.4% (944, 28% win) | -4.1% (1060, 24% win) |
| schoon+houders_ok+final_stretch | -7.6% (429, 16% win) | -7.0% (466, 15% win) | -7.9% (496, 13% win) | -8.9% (517, 12% win) | -8.7% (537, 10% win) | -7.6% (557, 10% win) | -6.8% (543, 10% win) | -6.0% (417, 11% win) | -7.5% (311, 9% win) | -7.6% (203, 9% win) | -5.4% (124, 12% win) | -6.0% (399, 15% win) |
| volledige_screening+schoon | -7.7% (295, 15% win) | -6.4% (306, 16% win) | -8.4% (311, 14% win) | -10.1% (320, 11% win) | -9.9% (325, 9% win) | -8.6% (326, 8% win) | -7.1% (313, 8% win) | -7.0% (244, 9% win) | -8.5% (182, 6% win) | -8.8% (122, 7% win) | -9.1% (75, 4% win) | -7.5% (234, 14% win) |
| volledige_screening+schoon+x_link | -8.3% (230, 16% win) | -5.3% (239, 19% win) | -8.7% (239, 15% win) | -10.2% (242, 11% win) | -10.1% (240, 9% win) | -9.4% (240, 8% win) | -8.5% (233, 7% win) | -8.5% (181, 6% win) | -8.6% (136, 4% win) | -8.7% (95, 6% win) | -8.7% (59, 2% win) | -7.9% (170, 13% win) |

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
| alle | -5.8% (4622, 30% win) | -5.8% (4523, 29% win) | -6.1% (4424, 28% win) | -6.4% (4317, 28% win) | -7.4% (4220, 26% win) | -6.8% (4062, 26% win) | -6.4% (3773, 27% win) | -6.6% (3370, 28% win) | -6.2% (2984, 31% win) | -6.6% (2632, 32% win) | -7.7% (2292, 33% win) |
| schoon | -5.6% (3714, 31% win) | -5.3% (3642, 31% win) | -5.9% (3559, 30% win) | -6.2% (3465, 30% win) | -7.3% (3391, 27% win) | -6.9% (3258, 27% win) | -6.2% (2998, 29% win) | -6.1% (2668, 31% win) | -5.6% (2388, 34% win) | -5.9% (2116, 34% win) | -7.0% (1870, 35% win) |
| bundelgrafiek | -6.5% (908, 26% win) | -7.6% (881, 24% win) | -7.0% (865, 22% win) | -7.2% (852, 21% win) | -7.7% (829, 20% win) | -6.5% (804, 20% win) | -7.0% (775, 18% win) | -8.7% (702, 17% win) | -8.6% (596, 20% win) | -9.3% (516, 22% win) | -10.8% (422, 23% win) |
| schoon+houders_ok | -6.3% (1022, 28% win) | -6.3% (1117, 28% win) | -6.4% (1209, 28% win) | -6.8% (1277, 28% win) | -7.0% (1360, 27% win) | -5.6% (1436, 27% win) | -4.9% (1466, 28% win) | -4.8% (1329, 30% win) | -3.8% (1207, 34% win) | -4.7% (1061, 34% win) | -6.9% (944, 34% win) |
| schoon+houders_ok+final_stretch | -7.0% (429, 24% win) | -6.7% (466, 24% win) | -7.0% (496, 24% win) | -9.0% (517, 21% win) | -10.3% (537, 17% win) | -9.2% (557, 18% win) | -6.3% (543, 21% win) | -6.8% (417, 22% win) | -8.4% (311, 23% win) | -7.7% (203, 25% win) | -6.7% (124, 25% win) |
| volledige_screening+schoon | -7.0% (295, 25% win) | -6.5% (306, 24% win) | -7.4% (311, 25% win) | -10.2% (320, 20% win) | -11.5% (325, 16% win) | -10.7% (326, 17% win) | -7.3% (313, 18% win) | -8.3% (244, 18% win) | -11.4% (182, 16% win) | -11.0% (122, 16% win) | -12.5% (75, 12% win) |
| volledige_screening+schoon+x_link | -7.2% (230, 25% win) | -5.8% (239, 26% win) | -7.5% (239, 24% win) | -10.7% (242, 19% win) | -12.3% (240, 13% win) | -10.9% (240, 15% win) | -7.9% (233, 16% win) | -8.6% (181, 17% win) | -10.0% (136, 17% win) | -11.2% (95, 16% win) | -12.5% (59, 8% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 320 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 47% | 23% | -8.4% | 25% |
| +15% | 41% | 18% | -8.6% | 21% |
| +20% | 38% | 16% | -8.6% | 18% |
| +25% | 33% | 13% | -9.0% | 16% |
| +30% | 31% | 12% | -9.1% | 15% |
| +35% | 28% | 11% | -9.2% | 13% |
| +45% | 24% | 8% | -10.1% | 11% |
| +60% | 20% | 7% | -9.9% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1277 instappen, mediane hoogste stijging +21.3%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 33% | -5.5% | 31% |
| +15% | 54% | 28% | -5.6% | 28% |
| +20% | 51% | 24% | -5.7% | 26% |
| +25% | 48% | 21% | -6.0% | 24% |
| +30% | 45% | 20% | -6.1% | 24% |
| +35% | 42% | 17% | -6.3% | 22% |
| +45% | 37% | 14% | -7.0% | 20% |
| +60% | 32% | 11% | -6.9% | 19% |

**filter `alle`** — variant `d45_direct`, 4317 instappen, mediane hoogste stijging +22.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.9% | 30% |
| +15% | 55% | 30% | -6.1% | 28% |
| +20% | 52% | 27% | -6.3% | 26% |
| +25% | 49% | 24% | -6.3% | 26% |
| +30% | 46% | 21% | -6.4% | 25% |
| +35% | 43% | 19% | -6.6% | 24% |
| +45% | 39% | 16% | -6.6% | 23% |
| +60% | 35% | 13% | -6.6% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.8% (295, 14% win) | -10.1% (295, 14% win) | -8.4% (295, 15% win) | -7.7% (295, 15% win) | -10.8% (295, 14% win) | -10.2% (295, 14% win) |
| d35_direct | -9.4% (306, 16% win) | -8.7% (306, 16% win) | -7.0% (306, 16% win) | -6.4% (306, 16% win) | -9.5% (306, 16% win) | -8.9% (306, 16% win) |
| d40_direct | -11.4% (311, 13% win) | -10.7% (311, 13% win) | -9.0% (311, 14% win) | -8.4% (311, 14% win) | -11.5% (311, 12% win) | -10.9% (311, 13% win) |
| d45_direct | -13.1% (320, 10% win) | -12.4% (320, 10% win) | -10.7% (320, 11% win) | -10.1% (320, 11% win) | -13.2% (320, 9% win) | -12.6% (320, 10% win) |
| d50_direct | -12.9% (325, 9% win) | -12.2% (325, 9% win) | -10.6% (325, 9% win) | -9.9% (325, 9% win) | -13.3% (325, 8% win) | -12.7% (325, 8% win) |
| d55_direct | -11.6% (326, 8% win) | -10.9% (326, 8% win) | -9.3% (326, 8% win) | -8.6% (326, 8% win) | -12.2% (326, 7% win) | -11.6% (326, 8% win) |
| d60_direct | -10.0% (313, 8% win) | -9.3% (313, 8% win) | -7.7% (313, 8% win) | -7.1% (313, 8% win) | -10.9% (313, 7% win) | -10.2% (313, 8% win) |
| d65_direct | -9.9% (244, 9% win) | -9.2% (244, 9% win) | -7.7% (244, 9% win) | -7.0% (244, 9% win) | -10.9% (244, 8% win) | -10.3% (244, 9% win) |
| d70_direct | -11.4% (182, 6% win) | -10.7% (182, 6% win) | -9.2% (182, 6% win) | -8.5% (182, 6% win) | -12.4% (182, 4% win) | -11.8% (182, 5% win) |
| d75_direct | -11.7% (122, 6% win) | -11.0% (122, 6% win) | -9.5% (122, 7% win) | -8.8% (122, 7% win) | -12.9% (122, 5% win) | -12.3% (122, 5% win) |
| d80_direct | -11.8% (75, 4% win) | -11.1% (75, 4% win) | -9.8% (75, 4% win) | -9.1% (75, 4% win) | -13.7% (75, 3% win) | -13.1% (75, 3% win) |
| d45_herstel5 | -10.5% (234, 14% win) | -9.8% (234, 14% win) | -8.2% (234, 14% win) | -7.5% (234, 14% win) | -10.6% (234, 14% win) | -10.0% (234, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (1022, 19% win) | -8.9% (1022, 20% win) | -7.1% (1022, 20% win) | -6.4% (1022, 21% win) | -9.2% (1022, 20% win) | -8.5% (1022, 20% win) |
| d35_direct | -9.7% (1117, 19% win) | -9.0% (1117, 19% win) | -7.3% (1117, 21% win) | -6.6% (1117, 21% win) | -9.5% (1117, 19% win) | -8.9% (1117, 20% win) |
| d40_direct | -10.1% (1209, 18% win) | -9.4% (1209, 19% win) | -7.7% (1209, 20% win) | -7.0% (1209, 20% win) | -10.1% (1209, 18% win) | -9.4% (1209, 19% win) |
| d45_direct | -10.1% (1277, 18% win) | -9.4% (1277, 19% win) | -7.7% (1277, 20% win) | -7.0% (1277, 20% win) | -10.1% (1277, 18% win) | -9.5% (1277, 19% win) |
| d50_direct | -9.8% (1360, 19% win) | -9.1% (1360, 19% win) | -7.5% (1360, 20% win) | -6.8% (1360, 21% win) | -10.1% (1360, 18% win) | -9.4% (1360, 19% win) |
| d55_direct | -8.4% (1436, 19% win) | -7.7% (1436, 19% win) | -6.2% (1436, 20% win) | -5.5% (1436, 20% win) | -9.0% (1436, 18% win) | -8.4% (1436, 19% win) |
| d60_direct | -8.0% (1466, 19% win) | -7.3% (1466, 20% win) | -5.7% (1466, 21% win) | -5.1% (1466, 21% win) | -8.8% (1466, 19% win) | -8.2% (1466, 19% win) |
| d65_direct | -7.3% (1329, 21% win) | -6.6% (1329, 21% win) | -5.1% (1329, 22% win) | -4.4% (1329, 23% win) | -8.5% (1329, 20% win) | -7.8% (1329, 21% win) |
| d70_direct | -6.6% (1207, 24% win) | -5.9% (1207, 24% win) | -4.6% (1207, 25% win) | -3.9% (1207, 25% win) | -8.4% (1207, 23% win) | -7.8% (1207, 23% win) |
| d75_direct | -7.6% (1061, 25% win) | -6.9% (1061, 25% win) | -5.7% (1061, 26% win) | -5.0% (1061, 26% win) | -10.2% (1061, 23% win) | -9.6% (1061, 23% win) |
| d80_direct | -7.7% (944, 27% win) | -7.0% (944, 28% win) | -6.1% (944, 28% win) | -5.4% (944, 28% win) | -11.7% (944, 24% win) | -11.1% (944, 24% win) |
| d45_herstel5 | -7.2% (1060, 23% win) | -6.5% (1060, 23% win) | -4.8% (1060, 24% win) | -4.1% (1060, 24% win) | -7.3% (1060, 23% win) | -6.6% (1060, 23% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.2% (4622, 24% win) | -8.5% (4622, 24% win) | -6.9% (4622, 25% win) | -6.2% (4622, 25% win) | -9.5% (4622, 23% win) | -8.8% (4622, 24% win) |
| d35_direct | -9.3% (4523, 23% win) | -8.6% (4523, 23% win) | -7.0% (4523, 24% win) | -6.3% (4523, 24% win) | -9.7% (4523, 22% win) | -9.1% (4523, 23% win) |
| d40_direct | -9.7% (4424, 22% win) | -9.0% (4424, 22% win) | -7.4% (4424, 23% win) | -6.7% (4424, 23% win) | -10.3% (4424, 21% win) | -9.6% (4424, 22% win) |
| d45_direct | -9.5% (4317, 21% win) | -8.9% (4317, 22% win) | -7.3% (4317, 22% win) | -6.6% (4317, 23% win) | -10.4% (4317, 20% win) | -9.7% (4317, 21% win) |
| d50_direct | -10.0% (4220, 20% win) | -9.4% (4220, 21% win) | -7.9% (4220, 21% win) | -7.2% (4220, 22% win) | -11.1% (4220, 20% win) | -10.4% (4220, 20% win) |
| d55_direct | -9.8% (4062, 20% win) | -9.1% (4062, 20% win) | -7.6% (4062, 21% win) | -7.0% (4062, 21% win) | -11.1% (4062, 19% win) | -10.5% (4062, 19% win) |
| d60_direct | -9.1% (3773, 21% win) | -8.5% (3773, 21% win) | -7.1% (3773, 22% win) | -6.4% (3773, 22% win) | -10.9% (3773, 20% win) | -10.2% (3773, 20% win) |
| d65_direct | -8.9% (3370, 22% win) | -8.2% (3370, 22% win) | -7.0% (3370, 23% win) | -6.3% (3370, 24% win) | -11.2% (3370, 20% win) | -10.5% (3370, 21% win) |
| d70_direct | -8.1% (2984, 24% win) | -7.3% (2984, 25% win) | -6.2% (2984, 25% win) | -5.5% (2984, 26% win) | -11.1% (2984, 22% win) | -10.5% (2984, 23% win) |
| d75_direct | -8.9% (2632, 24% win) | -8.2% (2632, 24% win) | -7.3% (2632, 25% win) | -6.6% (2632, 25% win) | -13.0% (2632, 21% win) | -12.4% (2632, 22% win) |
| d80_direct | -9.0% (2292, 27% win) | -8.3% (2292, 27% win) | -7.8% (2292, 27% win) | -7.1% (2292, 27% win) | -14.9% (2292, 22% win) | -14.3% (2292, 22% win) |
| d45_herstel5 | -9.3% (3547, 25% win) | -8.7% (3547, 25% win) | -7.2% (3547, 26% win) | -6.5% (3547, 26% win) | -10.4% (3547, 24% win) | -9.8% (3547, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.6% (4317, 23% win) | -6.3% (4317, 22% win) | -6.8% (4317, 22% win) |
| schoon | -6.3% (3465, 24% win) | -6.1% (3465, 24% win) | -6.3% (3465, 24% win) |
| bundelgrafiek | -8.0% (852, 16% win) | -6.9% (852, 16% win) | -8.8% (852, 15% win) |
| schoon+houders_ok | -7.0% (1277, 20% win) | -6.6% (1277, 20% win) | -6.2% (1277, 21% win) |
| schoon+houders_ok+final_stretch | -8.9% (517, 12% win) | -7.6% (517, 11% win) | -9.7% (517, 14% win) |
| volledige_screening+schoon | -10.1% (320, 11% win) | -8.8% (320, 9% win) | -10.9% (320, 14% win) |
| volledige_screening+schoon+x_link | -10.2% (242, 11% win) | -8.9% (242, 9% win) | -11.2% (242, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.8% (1852, 29% win); 1,3–2x: -8.1% (1613, 18% win); ≥ 2x (bundelgrafiek): -8.0% (852, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.6% (2785, 29% win); 5–20%: -8.8% (775, 13% win); ≥ 20%: -8.4% (757, 10% win)

**top t.o.v. start:** 2–3x: -6.2% (2421, 22% win); 3–6x: -6.7% (1482, 24% win); ≥ 6x: -8.8% (414, 22% win)

**unieke kopers tot de top:** < 30: -5.5% (2786, 29% win); 30–100: -7.5% (846, 11% win); ≥ 100: -10.0% (685, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.8% (1069, 16% win); 1–2: -6.0% (2056, 25% win); ≥ 3 (trap): -6.7% (1192, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.3% (1046, 12% win); 10–25%: -7.4% (666, 12% win); ≥ 25%: -5.4% (2605, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.1% (3442, 25% win); 30 s–3 min: -8.7% (689, 15% win); ≥ 3 min (langzaam): -9.9% (186, 7% win)

**tijd van start tot top:** < 2 min: -6.4% (3586, 24% win); 2–10 min: -7.4% (585, 16% win); ≥ 10 min: -9.3% (146, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
