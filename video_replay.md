# Videostrategie op alle trades — 2026-09-13 11:43 UTC

Tokens sinds 2026-09-11 08:47 UTC: 36341 geschikt (≥ 2 uur oud, geen herstart), 29142 met trades, 5571 haalden 2x de startkoers, 4236 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1299 tokens. Houdercheck echt uitgevoerd bij 89% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1263, winkans 20%, EV per trade -7.0% (95%-marge -8.8% tot -5.2%), mediaan -10.6%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2903, winkans 24%, EV -6.8% (95%-marge -8.7% tot -4.8%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 10, winkans 10%, EV -11.1% (95%-marge -19.9% tot -2.3%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4236 | 40% | 76% | 37% |
| schoon | 3392 | 43% | 76% | 40% |
| bundelgrafiek | 844 | 30% | 78% | 25% |
| schoon+houders_ok | 1263 | 38% | 79% | 26% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.3% (4527, 25% win) | -6.4% (4433, 24% win) | -6.8% (4336, 23% win) | -6.6% (4236, 23% win) | -7.2% (4141, 22% win) | -7.0% (3988, 21% win) | -6.4% (3707, 22% win) | -6.4% (3313, 24% win) | -5.5% (2936, 26% win) | -6.5% (2591, 25% win) | -7.0% (2256, 27% win) | -6.6% (3486, 26% win) |
| schoon | -6.2% (3633, 26% win) | -5.9% (3564, 26% win) | -6.4% (3481, 25% win) | -6.3% (3392, 24% win) | -6.7% (3320, 24% win) | -6.9% (3192, 23% win) | -6.1% (2939, 24% win) | -5.6% (2618, 26% win) | -4.9% (2345, 28% win) | -6.1% (2080, 27% win) | -6.6% (1838, 29% win) | -6.1% (2918, 27% win) |
| bundelgrafiek | -7.1% (894, 22% win) | -8.3% (869, 19% win) | -8.2% (855, 18% win) | -7.8% (844, 17% win) | -9.2% (821, 15% win) | -7.4% (796, 15% win) | -7.6% (768, 15% win) | -9.5% (695, 15% win) | -8.1% (591, 17% win) | -8.4% (511, 18% win) | -8.5% (418, 19% win) | -8.9% (568, 22% win) |
| schoon+houders_ok | -6.5% (1010, 21% win) | -6.6% (1105, 21% win) | -7.0% (1196, 20% win) | -7.0% (1263, 20% win) | -6.8% (1345, 21% win) | -5.5% (1419, 21% win) | -5.0% (1446, 21% win) | -4.3% (1307, 23% win) | -3.9% (1190, 26% win) | -5.0% (1050, 26% win) | -5.3% (935, 29% win) | -4.1% (1050, 24% win) |
| schoon+houders_ok+final_stretch | -7.7% (420, 16% win) | -7.1% (458, 15% win) | -8.0% (487, 13% win) | -9.0% (508, 12% win) | -8.8% (528, 10% win) | -7.6% (548, 10% win) | -6.7% (532, 10% win) | -5.9% (407, 12% win) | -7.4% (303, 9% win) | -7.6% (199, 9% win) | -5.3% (121, 12% win) | -6.0% (393, 15% win) |
| volledige_screening+schoon | -7.6% (288, 16% win) | -6.4% (299, 16% win) | -8.4% (303, 14% win) | -10.0% (313, 11% win) | -9.8% (318, 9% win) | -8.5% (319, 8% win) | -7.0% (307, 8% win) | -7.0% (240, 9% win) | -8.5% (178, 6% win) | -8.8% (119, 8% win) | -9.1% (73, 4% win) | -7.4% (230, 14% win) |
| volledige_screening+schoon+x_link | -8.2% (224, 16% win) | -5.3% (233, 19% win) | -8.7% (232, 15% win) | -10.1% (236, 11% win) | -10.1% (234, 9% win) | -9.3% (234, 8% win) | -8.5% (227, 7% win) | -8.5% (177, 6% win) | -8.6% (132, 4% win) | -8.7% (92, 6% win) | -8.7% (57, 2% win) | -7.8% (167, 13% win) |

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
| alle | -5.9% (4527, 30% win) | -5.8% (4433, 29% win) | -6.1% (4336, 28% win) | -6.3% (4236, 28% win) | -7.4% (4141, 26% win) | -6.8% (3988, 26% win) | -6.4% (3707, 27% win) | -6.7% (3313, 28% win) | -6.1% (2936, 31% win) | -6.5% (2591, 32% win) | -7.7% (2256, 33% win) |
| schoon | -5.7% (3633, 31% win) | -5.4% (3564, 31% win) | -5.9% (3481, 30% win) | -6.1% (3392, 30% win) | -7.3% (3320, 27% win) | -6.9% (3192, 28% win) | -6.2% (2939, 30% win) | -6.2% (2618, 31% win) | -5.5% (2345, 34% win) | -5.9% (2080, 34% win) | -7.1% (1838, 35% win) |
| bundelgrafiek | -6.6% (894, 26% win) | -7.6% (869, 24% win) | -6.8% (855, 22% win) | -7.1% (844, 21% win) | -7.6% (821, 20% win) | -6.5% (796, 20% win) | -6.9% (768, 18% win) | -8.7% (695, 17% win) | -8.6% (591, 20% win) | -9.0% (511, 22% win) | -10.3% (418, 23% win) |
| schoon+houders_ok | -6.4% (1010, 28% win) | -6.3% (1105, 28% win) | -6.3% (1196, 28% win) | -6.8% (1263, 28% win) | -7.1% (1345, 27% win) | -5.5% (1419, 28% win) | -4.8% (1446, 28% win) | -4.7% (1307, 30% win) | -3.7% (1190, 34% win) | -4.5% (1050, 35% win) | -6.9% (935, 34% win) |
| schoon+houders_ok+final_stretch | -7.1% (420, 24% win) | -6.8% (458, 24% win) | -7.0% (487, 24% win) | -9.0% (508, 21% win) | -10.5% (528, 17% win) | -9.3% (548, 18% win) | -6.1% (532, 21% win) | -6.7% (407, 22% win) | -8.2% (303, 23% win) | -7.5% (199, 26% win) | -6.9% (121, 25% win) |
| volledige_screening+schoon | -6.9% (288, 25% win) | -6.7% (299, 24% win) | -7.5% (303, 25% win) | -10.2% (313, 21% win) | -11.6% (318, 16% win) | -10.8% (319, 17% win) | -7.2% (307, 19% win) | -8.3% (240, 18% win) | -11.4% (178, 16% win) | -11.0% (119, 17% win) | -13.0% (73, 11% win) |
| volledige_screening+schoon+x_link | -7.1% (224, 26% win) | -5.9% (233, 26% win) | -7.5% (232, 25% win) | -10.6% (236, 20% win) | -12.3% (234, 14% win) | -10.8% (234, 15% win) | -7.8% (227, 17% win) | -8.7% (177, 16% win) | -9.9% (132, 17% win) | -11.2% (92, 16% win) | -13.1% (57, 7% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 313 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 24% | -8.3% | 25% |
| +15% | 42% | 18% | -8.5% | 21% |
| +20% | 39% | 16% | -8.5% | 18% |
| +25% | 34% | 13% | -8.9% | 16% |
| +30% | 31% | 12% | -9.0% | 15% |
| +35% | 28% | 11% | -9.1% | 14% |
| +45% | 24% | 8% | -10.0% | 11% |
| +60% | 21% | 7% | -9.8% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1263 instappen, mediane hoogste stijging +21.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.4% | 31% |
| +15% | 54% | 28% | -5.6% | 28% |
| +20% | 51% | 24% | -5.7% | 26% |
| +25% | 48% | 22% | -5.9% | 24% |
| +30% | 45% | 20% | -6.1% | 24% |
| +35% | 42% | 17% | -6.3% | 22% |
| +45% | 38% | 14% | -7.0% | 20% |
| +60% | 32% | 11% | -6.9% | 19% |

**filter `alle`** — variant `d45_direct`, 4236 instappen, mediane hoogste stijging +23.0%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.8% | 30% |
| +15% | 55% | 30% | -6.1% | 28% |
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
| d30_direct | -10.7% (288, 14% win) | -10.0% (288, 15% win) | -8.3% (288, 15% win) | -7.6% (288, 16% win) | -10.7% (288, 14% win) | -10.1% (288, 14% win) |
| d35_direct | -9.4% (299, 16% win) | -8.8% (299, 16% win) | -7.1% (299, 16% win) | -6.4% (299, 16% win) | -9.6% (299, 16% win) | -8.9% (299, 16% win) |
| d40_direct | -11.4% (303, 13% win) | -10.8% (303, 13% win) | -9.1% (303, 14% win) | -8.4% (303, 14% win) | -11.6% (303, 12% win) | -10.9% (303, 13% win) |
| d45_direct | -13.0% (313, 10% win) | -12.3% (313, 10% win) | -10.6% (313, 11% win) | -10.0% (313, 11% win) | -13.1% (313, 10% win) | -12.5% (313, 10% win) |
| d50_direct | -12.8% (318, 9% win) | -12.1% (318, 9% win) | -10.5% (318, 9% win) | -9.8% (318, 9% win) | -13.2% (318, 8% win) | -12.6% (318, 8% win) |
| d55_direct | -11.5% (319, 8% win) | -10.8% (319, 8% win) | -9.2% (319, 8% win) | -8.5% (319, 8% win) | -12.1% (319, 7% win) | -11.5% (319, 8% win) |
| d60_direct | -9.9% (307, 8% win) | -9.2% (307, 8% win) | -7.7% (307, 8% win) | -7.0% (307, 8% win) | -10.8% (307, 7% win) | -10.2% (307, 8% win) |
| d65_direct | -9.9% (240, 10% win) | -9.2% (240, 10% win) | -7.7% (240, 9% win) | -7.0% (240, 9% win) | -10.9% (240, 8% win) | -10.2% (240, 9% win) |
| d70_direct | -11.4% (178, 6% win) | -10.7% (178, 6% win) | -9.2% (178, 6% win) | -8.5% (178, 6% win) | -12.4% (178, 4% win) | -11.8% (178, 5% win) |
| d75_direct | -11.7% (119, 6% win) | -11.0% (119, 6% win) | -9.5% (119, 8% win) | -8.8% (119, 8% win) | -12.9% (119, 5% win) | -12.3% (119, 5% win) |
| d80_direct | -11.8% (73, 4% win) | -11.1% (73, 4% win) | -9.8% (73, 4% win) | -9.1% (73, 4% win) | -13.7% (73, 3% win) | -13.1% (73, 3% win) |
| d45_herstel5 | -10.4% (230, 14% win) | -9.8% (230, 14% win) | -8.1% (230, 14% win) | -7.4% (230, 14% win) | -10.5% (230, 14% win) | -9.8% (230, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (1010, 20% win) | -8.9% (1010, 20% win) | -7.1% (1010, 21% win) | -6.5% (1010, 21% win) | -9.2% (1010, 20% win) | -8.6% (1010, 20% win) |
| d35_direct | -9.7% (1105, 19% win) | -9.0% (1105, 19% win) | -7.3% (1105, 21% win) | -6.6% (1105, 21% win) | -9.5% (1105, 19% win) | -8.8% (1105, 20% win) |
| d40_direct | -10.1% (1196, 19% win) | -9.4% (1196, 19% win) | -7.7% (1196, 20% win) | -7.0% (1196, 20% win) | -10.0% (1196, 19% win) | -9.4% (1196, 19% win) |
| d45_direct | -10.0% (1263, 18% win) | -9.3% (1263, 19% win) | -7.7% (1263, 20% win) | -7.0% (1263, 20% win) | -10.1% (1263, 18% win) | -9.5% (1263, 19% win) |
| d50_direct | -9.8% (1345, 19% win) | -9.1% (1345, 19% win) | -7.5% (1345, 20% win) | -6.8% (1345, 21% win) | -10.1% (1345, 18% win) | -9.4% (1345, 19% win) |
| d55_direct | -8.4% (1419, 19% win) | -7.7% (1419, 19% win) | -6.1% (1419, 20% win) | -5.5% (1419, 21% win) | -9.0% (1419, 18% win) | -8.3% (1419, 19% win) |
| d60_direct | -7.9% (1446, 20% win) | -7.2% (1446, 20% win) | -5.7% (1446, 21% win) | -5.0% (1446, 21% win) | -8.8% (1446, 19% win) | -8.1% (1446, 20% win) |
| d65_direct | -7.2% (1307, 21% win) | -6.5% (1307, 22% win) | -5.0% (1307, 23% win) | -4.3% (1307, 23% win) | -8.4% (1307, 21% win) | -7.8% (1307, 21% win) |
| d70_direct | -6.6% (1190, 24% win) | -5.9% (1190, 25% win) | -4.5% (1190, 25% win) | -3.9% (1190, 26% win) | -8.4% (1190, 23% win) | -7.8% (1190, 24% win) |
| d75_direct | -7.6% (1050, 25% win) | -6.9% (1050, 26% win) | -5.7% (1050, 26% win) | -5.0% (1050, 26% win) | -10.1% (1050, 23% win) | -9.5% (1050, 24% win) |
| d80_direct | -7.6% (935, 27% win) | -6.9% (935, 28% win) | -6.0% (935, 28% win) | -5.3% (935, 29% win) | -11.6% (935, 24% win) | -11.0% (935, 25% win) |
| d45_herstel5 | -7.2% (1050, 23% win) | -6.5% (1050, 23% win) | -4.8% (1050, 24% win) | -4.1% (1050, 24% win) | -7.3% (1050, 23% win) | -6.6% (1050, 23% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.3% (4527, 24% win) | -8.6% (4527, 24% win) | -7.0% (4527, 25% win) | -6.3% (4527, 25% win) | -9.6% (4527, 23% win) | -8.9% (4527, 24% win) |
| d35_direct | -9.4% (4433, 23% win) | -8.7% (4433, 23% win) | -7.1% (4433, 24% win) | -6.4% (4433, 24% win) | -9.8% (4433, 22% win) | -9.1% (4433, 23% win) |
| d40_direct | -9.7% (4336, 22% win) | -9.0% (4336, 22% win) | -7.4% (4336, 23% win) | -6.8% (4336, 23% win) | -10.3% (4336, 21% win) | -9.6% (4336, 22% win) |
| d45_direct | -9.5% (4236, 21% win) | -8.8% (4236, 22% win) | -7.3% (4236, 22% win) | -6.6% (4236, 23% win) | -10.3% (4236, 20% win) | -9.7% (4236, 21% win) |
| d50_direct | -10.0% (4141, 20% win) | -9.4% (4141, 21% win) | -7.8% (4141, 22% win) | -7.2% (4141, 22% win) | -11.1% (4141, 20% win) | -10.4% (4141, 20% win) |
| d55_direct | -9.8% (3988, 20% win) | -9.1% (3988, 20% win) | -7.6% (3988, 21% win) | -7.0% (3988, 21% win) | -11.1% (3988, 19% win) | -10.5% (3988, 19% win) |
| d60_direct | -9.1% (3707, 21% win) | -8.5% (3707, 21% win) | -7.1% (3707, 22% win) | -6.4% (3707, 22% win) | -10.9% (3707, 20% win) | -10.2% (3707, 20% win) |
| d65_direct | -9.0% (3313, 22% win) | -8.3% (3313, 22% win) | -7.1% (3313, 23% win) | -6.4% (3313, 24% win) | -11.2% (3313, 20% win) | -10.6% (3313, 21% win) |
| d70_direct | -8.1% (2936, 24% win) | -7.3% (2936, 25% win) | -6.2% (2936, 25% win) | -5.5% (2936, 26% win) | -11.1% (2936, 22% win) | -10.5% (2936, 23% win) |
| d75_direct | -8.8% (2591, 24% win) | -8.1% (2591, 24% win) | -7.2% (2591, 25% win) | -6.5% (2591, 25% win) | -12.9% (2591, 21% win) | -12.3% (2591, 22% win) |
| d80_direct | -8.9% (2256, 26% win) | -8.2% (2256, 27% win) | -7.6% (2256, 27% win) | -7.0% (2256, 27% win) | -14.8% (2256, 22% win) | -14.2% (2256, 22% win) |
| d45_herstel5 | -9.4% (3486, 25% win) | -8.7% (3486, 25% win) | -7.2% (3486, 26% win) | -6.6% (3486, 26% win) | -10.5% (3486, 24% win) | -9.9% (3486, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.6% (4236, 23% win) | -6.2% (4236, 22% win) | -6.7% (4236, 22% win) |
| schoon | -6.3% (3392, 24% win) | -6.1% (3392, 24% win) | -6.2% (3392, 24% win) |
| bundelgrafiek | -7.8% (844, 17% win) | -6.8% (844, 17% win) | -8.6% (844, 15% win) |
| schoon+houders_ok | -7.0% (1263, 20% win) | -6.6% (1263, 20% win) | -6.2% (1263, 21% win) |
| schoon+houders_ok+final_stretch | -9.0% (508, 12% win) | -7.7% (508, 11% win) | -9.7% (508, 14% win) |
| volledige_screening+schoon | -10.0% (313, 11% win) | -8.7% (313, 9% win) | -10.7% (313, 14% win) |
| volledige_screening+schoon+x_link | -10.1% (236, 11% win) | -8.8% (236, 9% win) | -11.0% (236, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.7% (1818, 29% win); 1,3–2x: -8.1% (1574, 18% win); ≥ 2x (bundelgrafiek): -7.8% (844, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.5% (2738, 29% win); 5–20%: -8.8% (754, 13% win); ≥ 20%: -8.5% (744, 10% win)

**top t.o.v. start:** 2–3x: -6.1% (2375, 22% win); 3–6x: -6.8% (1450, 24% win); ≥ 6x: -8.6% (411, 22% win)

**unieke kopers tot de top:** < 30: -5.4% (2745, 29% win); 30–100: -7.5% (818, 11% win); ≥ 100: -10.1% (673, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.8% (1054, 16% win); 1–2: -5.8% (2018, 25% win); ≥ 3 (trap): -6.7% (1164, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.4% (1015, 11% win); 10–25%: -7.4% (657, 12% win); ≥ 25%: -5.2% (2564, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (3380, 25% win); 30 s–3 min: -8.7% (676, 15% win); ≥ 3 min (langzaam): -9.7% (180, 7% win)

**tijd van start tot top:** < 2 min: -6.3% (3526, 24% win); 2–10 min: -7.5% (566, 16% win); ≥ 10 min: -9.2% (144, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
