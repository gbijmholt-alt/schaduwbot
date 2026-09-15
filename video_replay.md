# Videostrategie op alle trades — 2026-09-15 21:09 UTC

Tokens sinds 2026-09-13 09:09 UTC: 71175 geschikt (≥ 2 uur oud, geen herstart), 54456 met trades, 9675 haalden 2x de startkoers, 7451 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2240 tokens. Houdercheck echt uitgevoerd bij 95% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 373, winkans 13%, EV per trade -8.0% (95%-marge -10.1% tot -6.0%), mediaan -10.1%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 6042, winkans 22%, EV -7.3% (95%-marge -8.7% tot -6.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 190, winkans 19%, EV -9.6% (95%-marge -12.8% tot -6.4%).
- **H4** (2026-09-14 22:00 UTC): instap na een dip van 65% vanaf de top; stop op 75% onder de top zolang de winst onder +15% blijft; vanaf +15% een meelopende stop op 10% onder de hoogste koers; schone grafiek en houdercheck in orde. Aanleiding: voorstel van Gerben, 14 sept. Combineert de twee hefbomen die los gemeten het minst slecht waren: dieper instappen (d65-d70 gaf -3,8% tot -4,7% tegen -6,9% bij d45) en eerder winst vastleggen (+10% gaf -5,4% tegen -6,9% bij +45%), maar dan met een meelopende stop zodat een uitschieter niet wordt afgekapt. Filter is 'schoon+houders_ok' en niet de volledige screening, omdat die screening in drie onafhankelijke metingen averechts werkt. Verwachting vooraf, zodat die toetsbaar is: rond -3%, dus nog steeds negatief.. Resultaat: n = 3, winkans 33%, EV -4.2% (95%-marge -9.9% tot +1.6%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 7451 | 38% | 79% | 33% |
| schoon | 6042 | 39% | 79% | 35% |
| bundelgrafiek | 1409 | 34% | 78% | 24% |
| schoon+houders_ok | 373 | 26% | 82% | 7% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -5.6% (7939, 25% win) | -6.4% (7760, 24% win) | -6.6% (7599, 23% win) | -6.2% (7451, 22% win) | -6.3% (7304, 22% win) | -6.5% (6996, 21% win) | -6.3% (6413, 21% win) | -5.4% (5705, 22% win) | -5.7% (4984, 23% win) | -6.0% (4373, 24% win) | -6.0% (3778, 27% win) | -6.2% (5958, 26% win) |
| schoon | -6.4% (6407, 25% win) | -7.0% (6272, 24% win) | -6.9% (6157, 23% win) | -6.3% (6042, 23% win) | -6.2% (5913, 23% win) | -6.4% (5648, 22% win) | -6.3% (5141, 22% win) | -5.8% (4564, 24% win) | -5.7% (3995, 25% win) | -5.8% (3505, 26% win) | -6.1% (3078, 29% win) | -6.4% (4962, 26% win) |
| bundelgrafiek | -2.6% (1532, 27% win) | -3.9% (1488, 26% win) | -5.2% (1442, 22% win) | -5.7% (1409, 20% win) | -6.6% (1391, 17% win) | -6.8% (1348, 16% win) | -6.6% (1272, 16% win) | -3.9% (1141, 18% win) | -5.5% (989, 17% win) | -6.7% (868, 17% win) | -5.8% (700, 20% win) | -5.0% (996, 25% win) |
| schoon+houders_ok | -7.5% (227, 16% win) | -9.4% (270, 13% win) | -8.7% (335, 13% win) | -8.0% (373, 13% win) | -8.4% (416, 11% win) | -8.3% (471, 11% win) | -6.8% (511, 10% win) | -7.4% (473, 10% win) | -6.5% (416, 11% win) | -5.6% (349, 12% win) | -5.7% (273, 12% win) | -4.2% (267, 19% win) |
| schoon+houders_ok+final_stretch | -5.4% (115, 17% win) | -9.5% (140, 11% win) | -8.0% (181, 13% win) | -6.4% (206, 14% win) | -8.4% (239, 10% win) | -7.9% (271, 10% win) | -7.9% (287, 8% win) | -8.8% (236, 6% win) | -6.2% (204, 10% win) | -6.3% (158, 8% win) | -6.0% (111, 8% win) | -4.0% (149, 17% win) |
| volledige_screening+schoon | -4.2% (95, 19% win) | -10.1% (114, 10% win) | -9.5% (139, 10% win) | -8.3% (156, 11% win) | -9.7% (178, 7% win) | -9.5% (190, 7% win) | -8.2% (191, 6% win) | -8.9% (147, 5% win) | -7.2% (118, 8% win) | -6.3% (102, 7% win) | -5.6% (69, 7% win) | -6.9% (110, 12% win) |
| volledige_screening+schoon+x_link | -3.7% (72, 21% win) | -10.3% (82, 12% win) | -9.4% (92, 11% win) | -8.4% (97, 11% win) | -9.6% (107, 10% win) | -9.6% (113, 10% win) | -8.5% (117, 8% win) | -9.3% (103, 7% win) | -7.3% (84, 8% win) | -6.7% (72, 7% win) | -6.9% (50, 4% win) | -7.5% (68, 10% win) |

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
| alle | -6.4% (7939, 29% win) | -7.2% (7760, 28% win) | -7.2% (7599, 27% win) | -6.7% (7451, 27% win) | -6.9% (7304, 26% win) | -7.1% (6996, 26% win) | -7.1% (6413, 26% win) | -6.4% (5705, 27% win) | -6.3% (4984, 29% win) | -7.0% (4373, 31% win) | -7.5% (3778, 33% win) |
| schoon | -6.7% (6407, 29% win) | -7.4% (6272, 28% win) | -7.1% (6157, 28% win) | -6.6% (6042, 28% win) | -6.7% (5913, 27% win) | -6.9% (5648, 27% win) | -7.1% (5141, 27% win) | -6.4% (4564, 29% win) | -6.1% (3995, 31% win) | -6.6% (3505, 33% win) | -7.3% (3078, 35% win) |
| bundelgrafiek | -5.2% (1532, 30% win) | -6.2% (1488, 28% win) | -7.5% (1442, 24% win) | -7.1% (1409, 23% win) | -7.7% (1391, 21% win) | -7.9% (1348, 20% win) | -7.2% (1272, 20% win) | -6.2% (1141, 20% win) | -7.4% (989, 21% win) | -8.4% (868, 22% win) | -8.3% (700, 25% win) |
| schoon+houders_ok | -7.5% (227, 24% win) | -9.0% (270, 22% win) | -8.3% (335, 22% win) | -8.8% (373, 21% win) | -9.5% (416, 19% win) | -8.3% (471, 20% win) | -8.4% (511, 17% win) | -8.7% (473, 20% win) | -8.5% (416, 21% win) | -7.6% (349, 24% win) | -6.4% (273, 27% win) |
| schoon+houders_ok+final_stretch | -6.2% (115, 26% win) | -10.7% (140, 20% win) | -8.8% (181, 22% win) | -10.3% (206, 20% win) | -10.6% (239, 19% win) | -8.4% (271, 20% win) | -10.2% (287, 15% win) | -11.4% (236, 15% win) | -8.1% (204, 21% win) | -7.8% (158, 23% win) | -7.2% (111, 23% win) |
| volledige_screening+schoon | -7.0% (95, 25% win) | -10.6% (114, 18% win) | -10.2% (139, 20% win) | -12.2% (156, 17% win) | -12.2% (178, 16% win) | -9.6% (190, 19% win) | -10.2% (191, 15% win) | -10.6% (147, 16% win) | -8.9% (118, 20% win) | -7.7% (102, 21% win) | -5.5% (69, 25% win) |
| volledige_screening+schoon+x_link | -7.1% (72, 25% win) | -10.1% (82, 18% win) | -11.5% (92, 18% win) | -12.7% (97, 16% win) | -11.2% (107, 18% win) | -7.9% (113, 23% win) | -8.6% (117, 19% win) | -9.7% (103, 18% win) | -8.8% (84, 19% win) | -6.2% (72, 22% win) | -5.1% (50, 26% win) |


## Regel H4: dip 65%, trailing stop vanaf +15% op 10% onder de piek

Tot +15% ligt de stop op hetzelfde niveau als bij de vorige regel — 10%-punt dieper dan de instap — zodat de positie eerst nog kan zakken. Vanaf +15% loopt de stop mee op 10% onder de hoogste koers, en ligt daarmee altijd boven de instapprijs. Geen vaste winstgrens: een uitschieter wordt niet afgekapt.

**Vooraf vastgelegd als H4 op d65 met filter schoon+houders_ok; de rest van deze regel is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.5% (7939, 28% win) | -7.2% (7760, 27% win) | -7.2% (7599, 26% win) | -7.1% (7451, 25% win) | -7.4% (7304, 25% win) | -7.2% (6996, 24% win) | -6.9% (6413, 24% win) | -5.8% (5705, 26% win) | -4.9% (4984, 27% win) | -6.5% (4373, 28% win) | -7.8% (3778, 29% win) |
| schoon | -7.0% (6407, 28% win) | -7.5% (6272, 27% win) | -7.1% (6157, 26% win) | -7.0% (6042, 26% win) | -7.2% (5913, 26% win) | -7.1% (5648, 25% win) | -6.6% (5141, 25% win) | -5.7% (4564, 27% win) | -4.3% (3995, 29% win) | -6.0% (3505, 30% win) | -7.7% (3078, 31% win) |
| bundelgrafiek | -3.9% (1532, 30% win) | -6.0% (1488, 28% win) | -7.5% (1442, 24% win) | -7.9% (1409, 21% win) | -8.4% (1391, 20% win) | -7.5% (1348, 19% win) | -8.0% (1272, 18% win) | -6.3% (1141, 19% win) | -7.3% (989, 19% win) | -8.3% (868, 20% win) | -8.4% (700, 22% win) |
| schoon+houders_ok | -6.7% (227, 25% win) | -8.6% (270, 23% win) | -8.3% (335, 24% win) | -7.7% (373, 22% win) | -9.4% (416, 19% win) | -9.5% (471, 20% win) | -9.2% (511, 18% win) | -7.1% (473, 21% win) | -7.7% (416, 21% win) | -7.4% (349, 23% win) | -8.0% (273, 23% win) |
| schoon+houders_ok+final_stretch | -4.3% (115, 30% win) | -9.3% (140, 21% win) | -8.5% (181, 25% win) | -8.1% (206, 23% win) | -9.5% (239, 20% win) | -10.0% (271, 20% win) | -10.7% (287, 16% win) | -10.2% (236, 19% win) | -8.7% (204, 20% win) | -8.9% (158, 22% win) | -8.9% (111, 21% win) |
| volledige_screening+schoon | -4.9% (95, 28% win) | -9.0% (114, 18% win) | -9.6% (139, 24% win) | -11.4% (156, 20% win) | -12.4% (178, 17% win) | -11.2% (190, 18% win) | -10.4% (191, 16% win) | -10.3% (147, 19% win) | -9.7% (118, 20% win) | -10.3% (102, 20% win) | -7.8% (69, 20% win) |
| volledige_screening+schoon+x_link | -5.9% (72, 26% win) | -8.6% (82, 17% win) | -10.8% (92, 20% win) | -10.7% (97, 21% win) | -11.0% (107, 20% win) | -10.7% (113, 20% win) | -9.8% (117, 20% win) | -9.8% (103, 18% win) | -10.3% (84, 19% win) | -11.6% (72, 18% win) | -6.3% (50, 18% win) |


## Verkennend: winstgrens tegen dipdiepte

Elke winstgrens bij elke instapdiepte, filter `schoon+houders_ok`, stop als in de video. Dit is het raster waar 8 grenzen x 11 dieptes = 88 cellen uit komen. Bij zoveel cellen zit er door toeval altijd een goede tussen, dus **hier telt geen enkele cel als bewijs** — het is bedoeld om te zien of er ergens een gebied is dat consequent beter is, niet om de beste cel te kiezen.

| winstgrens | d30 | d35 | d40 | d45 | d50 | d55 | d60 | d65 | d70 | d75 | d80 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +10% | -8.1% (227) | -8.8% (270) | -9.0% (335) | -7.6% (373) | -7.7% (416) | -7.5% (471) | -6.0% (511) | -6.6% (473) | -7.0% (416) | -5.9% (349) | -6.1% (273) |
| +15% | -8.3% (227) | -9.0% (270) | -8.5% (335) | -7.4% (373) | -7.8% (416) | -7.4% (471) | -6.0% (511) | -7.1% (473) | -7.1% (416) | -5.8% (349) | -5.9% (273) |
| +20% | -8.1% (227) | -9.1% (270) | -8.5% (335) | -7.6% (373) | -7.9% (416) | -7.4% (471) | -6.4% (511) | -7.6% (473) | -7.2% (416) | -6.0% (349) | -5.8% (273) |
| +25% | -7.4% (227) | -8.6% (270) | -8.6% (335) | -7.5% (373) | -7.9% (416) | -7.4% (471) | -6.4% (511) | -7.7% (473) | -7.1% (416) | -6.0% (349) | -6.2% (273) |
| +30% | -6.7% (227) | -8.4% (270) | -8.3% (335) | -7.6% (373) | -8.4% (416) | -7.4% (471) | -6.5% (511) | -7.5% (473) | -7.4% (416) | -6.7% (349) | -6.2% (273) |
| +35% | -7.2% (227) | -9.3% (270) | -8.2% (335) | -7.4% (373) | -8.4% (416) | -7.5% (471) | -6.8% (511) | -7.1% (473) | -7.0% (416) | -6.2% (349) | -6.1% (273) |
| +45% | -7.5% (227) | -9.4% (270) | -8.7% (335) | -8.0% (373) | -8.4% (416) | -8.3% (471) | -6.8% (511) | -7.4% (473) | -6.5% (416) | -5.6% (349) | -5.7% (273) |
| +60% | -8.0% (227) | -9.6% (270) | -8.2% (335) | -7.5% (373) | -8.1% (416) | -8.9% (471) | -6.9% (511) | -6.5% (473) | -6.2% (416) | -5.9% (349) | -5.9% (273) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 156 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 26% | -7.5% | 24% |
| +15% | 45% | 23% | -7.2% | 22% |
| +20% | 38% | 19% | -7.3% | 19% |
| +25% | 34% | 17% | -7.4% | 17% |
| +30% | 31% | 14% | -7.5% | 15% |
| +35% | 29% | 14% | -6.9% | 15% |
| +45% | 20% | 9% | -8.3% | 11% |
| +60% | 15% | 6% | -8.5% | 8% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 373 instappen, mediane hoogste stijging +9.2%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 49% | 25% | -7.6% | 25% |
| +15% | 46% | 20% | -7.4% | 22% |
| +20% | 42% | 17% | -7.6% | 20% |
| +25% | 38% | 16% | -7.5% | 19% |
| +30% | 36% | 14% | -7.6% | 17% |
| +35% | 33% | 13% | -7.4% | 16% |
| +45% | 27% | 9% | -8.0% | 13% |
| +60% | 24% | 8% | -7.5% | 12% |

**filter `alle`** — variant `d45_direct`, 7451 instappen, mediane hoogste stijging +19.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.8% | 29% |
| +15% | 53% | 28% | -5.7% | 28% |
| +20% | 50% | 25% | -5.7% | 27% |
| +25% | 47% | 22% | -5.9% | 26% |
| +30% | 44% | 20% | -6.0% | 25% |
| +35% | 42% | 18% | -6.0% | 24% |
| +45% | 38% | 15% | -6.2% | 22% |
| +60% | 32% | 12% | -6.3% | 21% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -7.2% (95, 19% win) | -6.5% (95, 19% win) | -4.9% (95, 19% win) | -4.2% (95, 19% win) | -7.1% (95, 19% win) | -6.5% (95, 19% win) |
| d35_direct | -13.2% (114, 10% win) | -12.6% (114, 10% win) | -10.8% (114, 10% win) | -10.1% (114, 10% win) | -13.0% (114, 10% win) | -12.3% (114, 10% win) |
| d40_direct | -12.6% (139, 9% win) | -11.9% (139, 9% win) | -10.2% (139, 10% win) | -9.5% (139, 10% win) | -12.5% (139, 9% win) | -11.9% (139, 9% win) |
| d45_direct | -11.3% (156, 10% win) | -10.6% (156, 10% win) | -8.9% (156, 10% win) | -8.3% (156, 11% win) | -11.4% (156, 10% win) | -10.8% (156, 10% win) |
| d50_direct | -12.6% (178, 7% win) | -12.0% (178, 7% win) | -10.3% (178, 7% win) | -9.7% (178, 7% win) | -13.0% (178, 7% win) | -12.3% (178, 7% win) |
| d55_direct | -12.4% (190, 7% win) | -11.7% (190, 7% win) | -10.1% (190, 7% win) | -9.5% (190, 7% win) | -13.0% (190, 7% win) | -12.3% (190, 7% win) |
| d60_direct | -11.1% (191, 6% win) | -10.4% (191, 6% win) | -8.8% (191, 6% win) | -8.2% (191, 6% win) | -11.8% (191, 6% win) | -11.2% (191, 6% win) |
| d65_direct | -11.8% (147, 5% win) | -11.1% (147, 5% win) | -9.6% (147, 5% win) | -8.9% (147, 5% win) | -12.5% (147, 5% win) | -11.9% (147, 5% win) |
| d70_direct | -10.1% (118, 7% win) | -9.4% (118, 7% win) | -7.9% (118, 8% win) | -7.2% (118, 8% win) | -10.9% (118, 7% win) | -10.2% (118, 7% win) |
| d75_direct | -9.2% (102, 7% win) | -8.6% (102, 7% win) | -7.0% (102, 7% win) | -6.3% (102, 7% win) | -10.1% (102, 7% win) | -9.5% (102, 7% win) |
| d80_direct | -8.5% (69, 6% win) | -7.8% (69, 6% win) | -6.3% (69, 6% win) | -5.6% (69, 7% win) | -9.6% (69, 6% win) | -9.0% (69, 6% win) |
| d45_herstel5 | -10.0% (110, 12% win) | -9.3% (110, 12% win) | -7.6% (110, 12% win) | -6.9% (110, 12% win) | -10.0% (110, 12% win) | -9.3% (110, 12% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.6% (227, 16% win) | -10.0% (227, 16% win) | -8.2% (227, 16% win) | -7.5% (227, 16% win) | -10.4% (227, 16% win) | -9.8% (227, 16% win) |
| d35_direct | -12.5% (270, 13% win) | -11.8% (270, 13% win) | -10.1% (270, 13% win) | -9.4% (270, 13% win) | -12.3% (270, 13% win) | -11.7% (270, 13% win) |
| d40_direct | -11.7% (335, 12% win) | -11.1% (335, 13% win) | -9.3% (335, 13% win) | -8.7% (335, 13% win) | -11.7% (335, 12% win) | -11.0% (335, 13% win) |
| d45_direct | -11.1% (373, 11% win) | -10.4% (373, 12% win) | -8.7% (373, 12% win) | -8.0% (373, 13% win) | -11.2% (373, 11% win) | -10.5% (373, 12% win) |
| d50_direct | -11.4% (416, 10% win) | -10.7% (416, 10% win) | -9.1% (416, 11% win) | -8.4% (416, 11% win) | -11.7% (416, 10% win) | -11.1% (416, 10% win) |
| d55_direct | -11.2% (471, 10% win) | -10.6% (471, 10% win) | -8.9% (471, 11% win) | -8.3% (471, 11% win) | -11.7% (471, 10% win) | -11.1% (471, 10% win) |
| d60_direct | -9.8% (511, 10% win) | -9.1% (511, 10% win) | -7.5% (511, 10% win) | -6.8% (511, 10% win) | -10.5% (511, 9% win) | -9.8% (511, 10% win) |
| d65_direct | -10.3% (473, 9% win) | -9.6% (473, 9% win) | -8.1% (473, 10% win) | -7.4% (473, 10% win) | -11.0% (473, 9% win) | -10.4% (473, 10% win) |
| d70_direct | -9.4% (416, 11% win) | -8.7% (416, 11% win) | -7.2% (416, 11% win) | -6.5% (416, 11% win) | -10.3% (416, 10% win) | -9.7% (416, 11% win) |
| d75_direct | -8.5% (349, 11% win) | -7.8% (349, 11% win) | -6.3% (349, 12% win) | -5.6% (349, 12% win) | -9.5% (349, 11% win) | -8.9% (349, 11% win) |
| d80_direct | -8.5% (273, 11% win) | -7.8% (273, 12% win) | -6.3% (273, 12% win) | -5.7% (273, 12% win) | -10.0% (273, 12% win) | -9.3% (273, 12% win) |
| d45_herstel5 | -7.2% (267, 18% win) | -6.6% (267, 19% win) | -4.9% (267, 19% win) | -4.2% (267, 19% win) | -7.2% (267, 18% win) | -6.6% (267, 19% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -8.6% (7939, 24% win) | -8.0% (7939, 24% win) | -6.3% (7939, 25% win) | -5.6% (7939, 25% win) | -9.0% (7939, 23% win) | -8.3% (7939, 24% win) |
| d35_direct | -9.4% (7760, 22% win) | -8.7% (7760, 23% win) | -7.1% (7760, 23% win) | -6.4% (7760, 24% win) | -9.8% (7760, 22% win) | -9.2% (7760, 22% win) |
| d40_direct | -9.5% (7599, 21% win) | -8.9% (7599, 22% win) | -7.3% (7599, 22% win) | -6.6% (7599, 23% win) | -10.2% (7599, 21% win) | -9.6% (7599, 21% win) |
| d45_direct | -9.1% (7451, 21% win) | -8.4% (7451, 21% win) | -6.9% (7451, 22% win) | -6.2% (7451, 22% win) | -10.0% (7451, 20% win) | -9.4% (7451, 21% win) |
| d50_direct | -9.2% (7304, 20% win) | -8.5% (7304, 20% win) | -7.0% (7304, 21% win) | -6.3% (7304, 22% win) | -10.3% (7304, 20% win) | -9.7% (7304, 20% win) |
| d55_direct | -9.3% (6996, 19% win) | -8.6% (6996, 20% win) | -7.2% (6996, 21% win) | -6.5% (6996, 21% win) | -10.7% (6996, 19% win) | -10.1% (6996, 19% win) |
| d60_direct | -9.0% (6413, 20% win) | -8.4% (6413, 20% win) | -7.0% (6413, 21% win) | -6.3% (6413, 21% win) | -10.9% (6413, 18% win) | -10.2% (6413, 19% win) |
| d65_direct | -8.0% (5705, 21% win) | -7.3% (5705, 22% win) | -6.1% (5705, 22% win) | -5.4% (5705, 22% win) | -10.4% (5705, 20% win) | -9.7% (5705, 20% win) |
| d70_direct | -8.2% (4984, 22% win) | -7.5% (4984, 22% win) | -6.4% (4984, 23% win) | -5.7% (4984, 23% win) | -11.2% (4984, 20% win) | -10.6% (4984, 20% win) |
| d75_direct | -8.3% (4373, 24% win) | -7.6% (4373, 24% win) | -6.7% (4373, 24% win) | -6.0% (4373, 24% win) | -12.3% (4373, 21% win) | -11.7% (4373, 21% win) |
| d80_direct | -8.0% (3778, 26% win) | -7.3% (3778, 26% win) | -6.7% (3778, 27% win) | -6.0% (3778, 27% win) | -13.6% (3778, 23% win) | -13.0% (3778, 23% win) |
| d45_herstel5 | -9.0% (5958, 24% win) | -8.4% (5958, 25% win) | -6.9% (5958, 26% win) | -6.2% (5958, 26% win) | -10.1% (5958, 24% win) | -9.4% (5958, 24% win) |


## Wat kost de uitvoering echt?

Wij rekenen met 0.001 SOL vaste kosten per transactie. De video van 14 sept gebruikt een tip van 0,02 SOL plus 0,001 prioriteitsfee — twintig keer zoveel. Een vaste fee werkt lineair door: elke extra T SOL per kant verlaagt het rendement met 2T gedeeld door de inzet. Onderstaande EV's zijn daarmee exact doorgerekend, niet opnieuw gesimuleerd. Filter `schoon+houders_ok`, videoregel, PumpPortal.

| extra vaste fee per transactie | inzet 0.05 SOL | inzet 0.2 SOL | inzet 1.0 SOL |
|---|---|---|---|
| +0.0 SOL | -10.4% | -8.0% | -10.5% |
| +0.005 SOL | -30.4% | -13.0% | -11.5% |
| +0.01 SOL | -50.4% | -18.0% | -12.5% |
| +0.02 SOL | -90.4% | -28.0% | -14.5% |

Bij 0,05 SOL inzet eet een tip van 0,02 SOL per kant 84% van de positie op. Een strategie met een randje van een paar procent bestaat bij die instellingen simpelweg niet; bij 1 SOL kost hij 4,2%. Dit verandert onze conclusie niet — de EV was al negatief — maar het laat zien dat kleine inzetten bij deze uitvoering sowieso kansloos zijn, en dat onze eigen cijfers aan de gunstige kant staan.



## Uitstapregels vergeleken (dip 45%, direct)

'Gespreid' is vier gelijke plakjes op +10%, +20%, +30% en +45%, allemaal met dezelfde stop — het advies uit de KOL-video om niet in één keer te verkopen. Dat is rekenkundig het gewogen gemiddelde van de vier losse grenzen, dus het kan de verwachting niet redden; het verandert alleen de spreiding.

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) | gespreid |
|---|---|---|---|---|
| alle | -6.2% (7451, 22% win) | -6.0% (7451, 22% win) | -7.6% (7451, 21% win) | -5.9% (7451, 25% win) |
| schoon | -6.3% (6042, 23% win) | -6.1% (6042, 22% win) | -7.3% (6042, 22% win) | -6.0% (6042, 26% win) |
| bundelgrafiek | -5.7% (1409, 20% win) | -5.7% (1409, 19% win) | -8.9% (1409, 18% win) | -5.6% (1409, 22% win) |
| schoon+houders_ok | -8.0% (373, 13% win) | -7.6% (373, 10% win) | -10.5% (373, 14% win) | -7.7% (373, 19% win) |
| schoon+houders_ok+final_stretch | -6.4% (206, 14% win) | -6.6% (206, 10% win) | -11.6% (206, 14% win) | -6.5% (206, 20% win) |
| volledige_screening+schoon | -8.3% (156, 11% win) | -8.8% (156, 6% win) | -15.3% (156, 11% win) | -7.7% (156, 19% win) |
| volledige_screening+schoon+x_link | -8.4% (97, 11% win) | -9.0% (97, 7% win) | -15.0% (97, 9% win) | -8.4% (97, 18% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (2978, 28% win); 1,3–2x: -7.0% (3063, 18% win); ≥ 2x (bundelgrafiek): -5.7% (1410, 20% win)

**aandeel supply gekocht in creatieblok:** < 5%: -4.8% (4262, 30% win); 5–20%: -8.3% (1250, 13% win); ≥ 20%: -8.0% (1939, 13% win)

**top t.o.v. start:** 2–3x: -5.9% (4257, 21% win); 3–6x: -6.9% (2468, 24% win); ≥ 6x: -5.9% (726, 24% win)

**unieke kopers tot de top:** < 30: -5.2% (4379, 29% win); 30–100: -6.9% (1716, 13% win); ≥ 100: -8.6% (1356, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.2% (1923, 16% win); 1–2: -6.6% (3568, 24% win); ≥ 3 (trap): -5.6% (1960, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -7.8% (2021, 14% win); 10–25%: -8.7% (1415, 11% win); ≥ 25%: -4.5% (4015, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.9% (5735, 25% win); 30 s–3 min: -6.9% (1365, 14% win); ≥ 3 min (langzaam): -8.5% (351, 10% win)

**tijd van start tot top:** < 2 min: -5.8% (6010, 24% win); 2–10 min: -8.4% (1162, 14% win); ≥ 10 min: -5.8% (279, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
