# Videostrategie op alle trades — 2026-09-13 20:55 UTC

Tokens sinds 2026-09-11 08:47 UTC: 45934 geschikt (≥ 2 uur oud, geen herstart), 35989 met trades, 6620 haalden 2x de startkoers, 5075 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1586 tokens. Houdercheck echt uitgevoerd bij 90% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1379, winkans 20%, EV per trade -7.1% (95%-marge -8.8% tot -5.4%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 3560, winkans 24%, EV -6.6% (95%-marge -8.4% tot -4.8%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 74, winkans 19%, EV -9.2% (95%-marge -14.2% tot -4.1%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 5075 | 40% | 77% | 36% |
| schoon | 4049 | 43% | 76% | 40% |
| bundelgrafiek | 1026 | 29% | 79% | 24% |
| schoon+houders_ok | 1379 | 37% | 79% | 25% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.1% (5421, 25% win) | -6.4% (5311, 24% win) | -6.7% (5197, 23% win) | -6.2% (5075, 23% win) | -6.6% (4967, 22% win) | -6.6% (4790, 21% win) | -6.1% (4450, 22% win) | -6.0% (3983, 24% win) | -5.5% (3524, 25% win) | -6.3% (3096, 25% win) | -6.8% (2686, 27% win) | -5.9% (4160, 27% win) |
| schoon | -6.0% (4325, 26% win) | -6.1% (4247, 25% win) | -6.4% (4155, 24% win) | -5.9% (4049, 24% win) | -6.0% (3966, 24% win) | -6.5% (3816, 23% win) | -5.7% (3514, 24% win) | -5.2% (3138, 26% win) | -4.9% (2802, 27% win) | -5.8% (2477, 27% win) | -6.6% (2185, 29% win) | -5.6% (3483, 27% win) |
| bundelgrafiek | -6.5% (1096, 23% win) | -7.7% (1064, 20% win) | -8.0% (1042, 18% win) | -7.4% (1026, 17% win) | -8.9% (1001, 15% win) | -7.2% (974, 15% win) | -7.7% (936, 16% win) | -9.3% (845, 14% win) | -7.8% (722, 17% win) | -8.5% (619, 17% win) | -7.7% (501, 19% win) | -7.8% (677, 24% win) |
| schoon+houders_ok | -6.4% (1091, 21% win) | -6.9% (1196, 20% win) | -7.2% (1303, 20% win) | -7.1% (1379, 20% win) | -6.8% (1476, 20% win) | -5.6% (1567, 20% win) | -5.2% (1602, 20% win) | -4.8% (1465, 22% win) | -4.3% (1330, 24% win) | -5.2% (1166, 25% win) | -5.5% (1023, 27% win) | -4.4% (1137, 23% win) |
| schoon+houders_ok+final_stretch | -7.1% (463, 17% win) | -7.3% (506, 15% win) | -8.1% (546, 12% win) | -8.8% (574, 12% win) | -8.6% (604, 10% win) | -7.6% (631, 10% win) | -7.0% (620, 10% win) | -6.5% (490, 11% win) | -7.7% (374, 8% win) | -7.9% (253, 8% win) | -5.6% (157, 11% win) | -6.0% (445, 15% win) |
| volledige_screening+schoon | -7.0% (325, 16% win) | -7.0% (340, 15% win) | -8.7% (351, 13% win) | -9.8% (367, 11% win) | -9.4% (379, 9% win) | -8.5% (383, 8% win) | -7.4% (371, 8% win) | -7.2% (295, 9% win) | -8.6% (225, 6% win) | -8.9% (160, 6% win) | -8.3% (103, 5% win) | -7.2% (270, 14% win) |
| volledige_screening+schoon+x_link | -7.5% (251, 17% win) | -6.0% (263, 18% win) | -8.9% (267, 14% win) | -9.9% (272, 11% win) | -9.8% (272, 9% win) | -9.2% (276, 8% win) | -8.7% (270, 7% win) | -8.6% (216, 7% win) | -8.8% (163, 5% win) | -9.0% (118, 5% win) | -9.2% (76, 1% win) | -7.4% (195, 14% win) |

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
| alle | -5.9% (5421, 30% win) | -6.3% (5311, 29% win) | -6.3% (5197, 28% win) | -6.2% (5075, 28% win) | -7.0% (4967, 26% win) | -6.5% (4790, 26% win) | -6.3% (4450, 27% win) | -6.5% (3983, 28% win) | -6.3% (3524, 31% win) | -6.4% (3096, 32% win) | -7.6% (2686, 33% win) |
| schoon | -5.8% (4325, 31% win) | -6.0% (4247, 30% win) | -6.2% (4155, 30% win) | -6.1% (4049, 29% win) | -6.9% (3966, 28% win) | -6.6% (3816, 28% win) | -6.2% (3514, 29% win) | -5.8% (3138, 31% win) | -5.6% (2802, 34% win) | -5.8% (2477, 34% win) | -7.0% (2185, 35% win) |
| bundelgrafiek | -6.4% (1096, 27% win) | -7.4% (1064, 24% win) | -6.9% (1042, 22% win) | -6.9% (1026, 20% win) | -7.5% (1001, 20% win) | -6.3% (974, 20% win) | -7.0% (936, 18% win) | -9.0% (845, 16% win) | -8.8% (722, 20% win) | -8.8% (619, 22% win) | -10.3% (501, 23% win) |
| schoon+houders_ok | -6.4% (1091, 28% win) | -6.5% (1196, 28% win) | -6.5% (1303, 27% win) | -6.8% (1379, 28% win) | -7.1% (1476, 26% win) | -5.8% (1567, 27% win) | -5.2% (1602, 27% win) | -5.1% (1465, 29% win) | -4.4% (1330, 32% win) | -4.8% (1166, 34% win) | -6.7% (1023, 34% win) |
| schoon+houders_ok+final_stretch | -6.9% (463, 25% win) | -7.1% (506, 24% win) | -7.3% (546, 23% win) | -9.0% (574, 21% win) | -10.3% (604, 17% win) | -9.3% (631, 18% win) | -6.9% (620, 20% win) | -7.3% (490, 21% win) | -8.5% (374, 22% win) | -7.0% (253, 26% win) | -4.9% (157, 27% win) |
| volledige_screening+schoon | -7.1% (325, 25% win) | -7.3% (340, 24% win) | -8.2% (351, 24% win) | -10.3% (367, 20% win) | -11.3% (379, 17% win) | -10.4% (383, 17% win) | -8.0% (371, 18% win) | -8.4% (295, 19% win) | -11.1% (225, 16% win) | -9.6% (160, 19% win) | -8.3% (103, 19% win) |
| volledige_screening+schoon+x_link | -7.1% (251, 26% win) | -6.4% (263, 25% win) | -8.4% (267, 23% win) | -10.8% (272, 19% win) | -12.1% (272, 14% win) | -10.5% (276, 16% win) | -7.9% (270, 17% win) | -8.5% (216, 18% win) | -10.0% (163, 17% win) | -9.2% (118, 20% win) | -8.9% (76, 17% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 367 instappen, mediane hoogste stijging +8.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 25% | -7.8% | 26% |
| +15% | 43% | 20% | -8.0% | 22% |
| +20% | 40% | 18% | -7.9% | 20% |
| +25% | 34% | 15% | -8.4% | 17% |
| +30% | 32% | 13% | -8.6% | 16% |
| +35% | 29% | 12% | -8.6% | 14% |
| +45% | 24% | 8% | -9.8% | 11% |
| +60% | 20% | 6% | -9.6% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1379 instappen, mediane hoogste stijging +20.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 33% | -5.4% | 31% |
| +15% | 54% | 27% | -5.6% | 28% |
| +20% | 51% | 24% | -5.7% | 26% |
| +25% | 47% | 21% | -5.9% | 24% |
| +30% | 45% | 19% | -6.1% | 24% |
| +35% | 42% | 17% | -6.3% | 22% |
| +45% | 37% | 13% | -7.1% | 20% |
| +60% | 32% | 11% | -6.9% | 18% |

**filter `alle`** — variant `d45_direct`, 5075 instappen, mediane hoogste stijging +22.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.6% | 30% |
| +15% | 55% | 30% | -5.7% | 28% |
| +20% | 52% | 27% | -5.9% | 27% |
| +25% | 49% | 24% | -5.9% | 26% |
| +30% | 46% | 21% | -6.0% | 25% |
| +35% | 43% | 19% | -6.1% | 24% |
| +45% | 39% | 16% | -6.2% | 23% |
| +60% | 35% | 13% | -6.1% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.0% (325, 15% win) | -9.3% (325, 15% win) | -7.6% (325, 16% win) | -7.0% (325, 16% win) | -10.0% (325, 15% win) | -9.4% (325, 15% win) |
| d35_direct | -10.1% (340, 15% win) | -9.4% (340, 15% win) | -7.7% (340, 15% win) | -7.0% (340, 15% win) | -10.1% (340, 15% win) | -9.4% (340, 15% win) |
| d40_direct | -11.7% (351, 12% win) | -11.1% (351, 12% win) | -9.4% (351, 13% win) | -8.7% (351, 13% win) | -11.8% (351, 12% win) | -11.2% (351, 12% win) |
| d45_direct | -12.8% (367, 10% win) | -12.2% (367, 10% win) | -10.5% (367, 11% win) | -9.8% (367, 11% win) | -13.0% (367, 10% win) | -12.4% (367, 10% win) |
| d50_direct | -12.4% (379, 8% win) | -11.7% (379, 8% win) | -10.1% (379, 9% win) | -9.4% (379, 9% win) | -12.8% (379, 8% win) | -12.2% (379, 8% win) |
| d55_direct | -11.5% (383, 8% win) | -10.8% (383, 8% win) | -9.2% (383, 8% win) | -8.5% (383, 8% win) | -12.0% (383, 7% win) | -11.4% (383, 8% win) |
| d60_direct | -10.3% (371, 8% win) | -9.6% (371, 8% win) | -8.1% (371, 8% win) | -7.4% (371, 8% win) | -11.2% (371, 6% win) | -10.5% (371, 8% win) |
| d65_direct | -10.1% (295, 10% win) | -9.4% (295, 10% win) | -7.9% (295, 9% win) | -7.2% (295, 9% win) | -11.1% (295, 8% win) | -10.4% (295, 9% win) |
| d70_direct | -11.5% (225, 5% win) | -10.8% (225, 5% win) | -9.3% (225, 6% win) | -8.6% (225, 6% win) | -12.4% (225, 4% win) | -11.8% (225, 5% win) |
| d75_direct | -11.8% (160, 5% win) | -11.1% (160, 5% win) | -9.6% (160, 6% win) | -8.9% (160, 6% win) | -12.8% (160, 4% win) | -12.2% (160, 4% win) |
| d80_direct | -11.0% (103, 5% win) | -10.3% (103, 5% win) | -8.9% (103, 5% win) | -8.3% (103, 5% win) | -12.6% (103, 4% win) | -12.0% (103, 4% win) |
| d45_herstel5 | -10.2% (270, 14% win) | -9.6% (270, 14% win) | -7.9% (270, 14% win) | -7.2% (270, 14% win) | -10.3% (270, 14% win) | -9.7% (270, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (1091, 19% win) | -8.9% (1091, 20% win) | -7.1% (1091, 20% win) | -6.4% (1091, 21% win) | -9.2% (1091, 20% win) | -8.5% (1091, 20% win) |
| d35_direct | -10.0% (1196, 19% win) | -9.3% (1196, 19% win) | -7.5% (1196, 20% win) | -6.9% (1196, 20% win) | -9.7% (1196, 19% win) | -9.1% (1196, 19% win) |
| d40_direct | -10.2% (1303, 18% win) | -9.5% (1303, 18% win) | -7.8% (1303, 19% win) | -7.2% (1303, 20% win) | -10.2% (1303, 18% win) | -9.5% (1303, 18% win) |
| d45_direct | -10.1% (1379, 18% win) | -9.4% (1379, 18% win) | -7.8% (1379, 19% win) | -7.1% (1379, 20% win) | -10.2% (1379, 18% win) | -9.5% (1379, 18% win) |
| d50_direct | -9.8% (1476, 18% win) | -9.1% (1476, 18% win) | -7.5% (1476, 19% win) | -6.8% (1476, 20% win) | -10.1% (1476, 18% win) | -9.4% (1476, 18% win) |
| d55_direct | -8.5% (1567, 18% win) | -7.8% (1567, 18% win) | -6.3% (1567, 19% win) | -5.6% (1567, 20% win) | -9.1% (1567, 18% win) | -8.5% (1567, 18% win) |
| d60_direct | -8.1% (1602, 19% win) | -7.4% (1602, 19% win) | -5.9% (1602, 20% win) | -5.2% (1602, 20% win) | -9.0% (1602, 18% win) | -8.3% (1602, 19% win) |
| d65_direct | -7.7% (1465, 20% win) | -7.0% (1465, 20% win) | -5.5% (1465, 21% win) | -4.8% (1465, 22% win) | -8.8% (1465, 20% win) | -8.2% (1465, 20% win) |
| d70_direct | -7.1% (1330, 22% win) | -6.4% (1330, 23% win) | -5.0% (1330, 23% win) | -4.3% (1330, 24% win) | -8.8% (1330, 22% win) | -8.2% (1330, 22% win) |
| d75_direct | -7.8% (1166, 24% win) | -7.1% (1166, 24% win) | -5.9% (1166, 24% win) | -5.2% (1166, 25% win) | -10.2% (1166, 22% win) | -9.6% (1166, 22% win) |
| d80_direct | -7.8% (1023, 26% win) | -7.1% (1023, 26% win) | -6.2% (1023, 27% win) | -5.5% (1023, 27% win) | -11.6% (1023, 23% win) | -11.0% (1023, 23% win) |
| d45_herstel5 | -7.4% (1137, 22% win) | -6.7% (1137, 22% win) | -5.1% (1137, 23% win) | -4.4% (1137, 23% win) | -7.5% (1137, 22% win) | -6.9% (1137, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.1% (5421, 24% win) | -8.5% (5421, 24% win) | -6.8% (5421, 25% win) | -6.1% (5421, 25% win) | -9.4% (5421, 24% win) | -8.7% (5421, 24% win) |
| d35_direct | -9.4% (5311, 23% win) | -8.7% (5311, 23% win) | -7.1% (5311, 24% win) | -6.4% (5311, 24% win) | -9.8% (5311, 22% win) | -9.2% (5311, 23% win) |
| d40_direct | -9.6% (5197, 22% win) | -8.9% (5197, 22% win) | -7.4% (5197, 23% win) | -6.7% (5197, 23% win) | -10.2% (5197, 21% win) | -9.6% (5197, 22% win) |
| d45_direct | -9.1% (5075, 21% win) | -8.4% (5075, 22% win) | -6.9% (5075, 22% win) | -6.2% (5075, 23% win) | -10.0% (5075, 21% win) | -9.3% (5075, 21% win) |
| d50_direct | -9.4% (4967, 21% win) | -8.7% (4967, 21% win) | -7.2% (4967, 22% win) | -6.6% (4967, 22% win) | -10.5% (4967, 20% win) | -9.8% (4967, 20% win) |
| d55_direct | -9.4% (4790, 20% win) | -8.8% (4790, 20% win) | -7.3% (4790, 21% win) | -6.6% (4790, 21% win) | -10.8% (4790, 19% win) | -10.1% (4790, 19% win) |
| d60_direct | -8.8% (4450, 21% win) | -8.2% (4450, 21% win) | -6.8% (4450, 22% win) | -6.1% (4450, 22% win) | -10.6% (4450, 20% win) | -9.9% (4450, 20% win) |
| d65_direct | -8.7% (3983, 22% win) | -8.0% (3983, 22% win) | -6.7% (3983, 23% win) | -6.0% (3983, 24% win) | -10.9% (3983, 20% win) | -10.3% (3983, 21% win) |
| d70_direct | -8.0% (3524, 24% win) | -7.3% (3524, 24% win) | -6.2% (3524, 25% win) | -5.5% (3524, 25% win) | -11.0% (3524, 22% win) | -10.4% (3524, 23% win) |
| d75_direct | -8.6% (3096, 24% win) | -7.9% (3096, 24% win) | -7.0% (3096, 25% win) | -6.3% (3096, 25% win) | -12.6% (3096, 21% win) | -12.0% (3096, 22% win) |
| d80_direct | -8.8% (2686, 26% win) | -8.1% (2686, 27% win) | -7.5% (2686, 27% win) | -6.8% (2686, 27% win) | -14.5% (2686, 22% win) | -13.9% (2686, 22% win) |
| d45_herstel5 | -8.8% (4160, 25% win) | -8.1% (4160, 26% win) | -6.6% (4160, 26% win) | -5.9% (4160, 27% win) | -9.9% (4160, 24% win) | -9.3% (4160, 25% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.2% (5075, 23% win) | -5.9% (5075, 23% win) | -6.5% (5075, 22% win) |
| schoon | -5.9% (4049, 24% win) | -5.8% (4049, 24% win) | -6.2% (4049, 24% win) |
| bundelgrafiek | -7.4% (1026, 17% win) | -6.5% (1026, 17% win) | -7.6% (1026, 15% win) |
| schoon+houders_ok | -7.1% (1379, 20% win) | -6.7% (1379, 19% win) | -6.4% (1379, 20% win) |
| schoon+houders_ok+final_stretch | -8.8% (574, 12% win) | -7.6% (574, 11% win) | -9.7% (574, 14% win) |
| volledige_screening+schoon | -9.8% (367, 11% win) | -8.8% (367, 9% win) | -10.8% (367, 14% win) |
| volledige_screening+schoon+x_link | -9.9% (272, 11% win) | -8.8% (272, 9% win) | -10.9% (272, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.4% (2160, 29% win); 1,3–2x: -7.7% (1889, 19% win); ≥ 2x (bundelgrafiek): -7.4% (1026, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.3% (3214, 29% win); 5–20%: -8.5% (882, 13% win); ≥ 20%: -7.3% (979, 11% win)

**top t.o.v. start:** 2–3x: -6.1% (2825, 22% win); 3–6x: -6.0% (1757, 24% win); ≥ 6x: -7.7% (493, 24% win)

**unieke kopers tot de top:** < 30: -5.3% (3207, 29% win); 30–100: -6.8% (1045, 12% win); ≥ 100: -9.1% (823, 13% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.8% (1259, 16% win); 1–2: -5.8% (2405, 25% win); ≥ 3 (trap): -6.5% (1411, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.6% (1238, 12% win); 10–25%: -7.5% (829, 12% win); ≥ 25%: -4.9% (3008, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.5% (4002, 25% win); 30 s–3 min: -8.3% (851, 15% win); ≥ 3 min (langzaam): -10.3% (222, 8% win)

**tijd van start tot top:** < 2 min: -5.9% (4172, 24% win); 2–10 min: -7.4% (722, 16% win); ≥ 10 min: -9.9% (181, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
