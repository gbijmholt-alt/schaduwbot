# Videostrategie op alle trades — 2026-09-16 00:16 UTC

Tokens sinds 2026-09-13 12:16 UTC: 75134 geschikt (≥ 2 uur oud, geen herstart), 57959 met trades, 10498 haalden 2x de startkoers, 8161 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2403 tokens. Houdercheck echt uitgevoerd bij 95% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 342, winkans 14%, EV per trade -7.6% (95%-marge -9.8% tot -5.5%), mediaan -9.9%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 6594, winkans 21%, EV -7.1% (95%-marge -8.5% tot -5.7%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 172, winkans 19%, EV -9.9% (95%-marge -13.3% tot -6.5%).
- **H4** (2026-09-14 22:00 UTC): instap na een dip van 65% vanaf de top; stop op 75% onder de top zolang de winst onder +15% blijft; vanaf +15% een meelopende stop op 10% onder de hoogste koers; schone grafiek en houdercheck in orde. Aanleiding: voorstel van Gerben, 14 sept. Combineert de twee hefbomen die los gemeten het minst slecht waren: dieper instappen (d65-d70 gaf -3,8% tot -4,7% tegen -6,9% bij d45) en eerder winst vastleggen (+10% gaf -5,4% tegen -6,9% bij +45%), maar dan met een meelopende stop zodat een uitschieter niet wordt afgekapt. Filter is 'schoon+houders_ok' en niet de volledige screening, omdat die screening in drie onafhankelijke metingen averechts werkt. Verwachting vooraf, zodat die toetsbaar is: rond -3%, dus nog steeds negatief.. Resultaat: n = 3, winkans 33%, EV -4.2% (95%-marge -9.9% tot +1.6%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 8161 | 38% | 79% | 32% |
| schoon | 6594 | 39% | 79% | 34% |
| bundelgrafiek | 1567 | 33% | 79% | 23% |
| schoon+houders_ok | 342 | 27% | 81% | 7% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -5.9% (8676, 25% win) | -6.6% (8490, 24% win) | -6.8% (8322, 22% win) | -6.3% (8161, 22% win) | -6.4% (8002, 21% win) | -6.5% (7657, 21% win) | -6.3% (7019, 21% win) | -5.6% (6231, 22% win) | -5.9% (5433, 23% win) | -6.1% (4737, 24% win) | -6.1% (4065, 27% win) | -6.1% (6523, 26% win) |
| schoon | -6.6% (6982, 25% win) | -7.2% (6840, 23% win) | -7.1% (6718, 23% win) | -6.3% (6594, 23% win) | -6.3% (6453, 22% win) | -6.5% (6157, 22% win) | -6.2% (5603, 22% win) | -5.9% (4960, 23% win) | -6.0% (4332, 24% win) | -6.0% (3786, 26% win) | -6.2% (3308, 28% win) | -6.2% (5408, 26% win) |
| bundelgrafiek | -3.1% (1694, 26% win) | -4.4% (1650, 25% win) | -5.5% (1604, 22% win) | -6.1% (1567, 20% win) | -6.7% (1549, 17% win) | -6.6% (1500, 17% win) | -6.7% (1416, 16% win) | -4.2% (1271, 18% win) | -5.6% (1101, 17% win) | -6.4% (951, 17% win) | -5.6% (757, 20% win) | -5.2% (1115, 25% win) |
| schoon+houders_ok | -8.3% (204, 16% win) | -9.3% (246, 14% win) | -8.6% (306, 13% win) | -7.6% (342, 14% win) | -8.3% (382, 11% win) | -8.2% (430, 11% win) | -6.6% (467, 10% win) | -7.1% (429, 10% win) | -6.4% (382, 12% win) | -5.1% (324, 13% win) | -6.3% (254, 12% win) | -3.4% (243, 20% win) |
| schoon+houders_ok+final_stretch | -6.7% (100, 16% win) | -9.3% (125, 12% win) | -7.9% (162, 12% win) | -5.6% (186, 14% win) | -8.2% (218, 10% win) | -7.7% (248, 10% win) | -7.8% (263, 8% win) | -8.7% (213, 6% win) | -5.8% (185, 11% win) | -5.9% (145, 8% win) | -5.7% (103, 9% win) | -3.2% (134, 18% win) |
| volledige_screening+schoon | -4.5% (82, 18% win) | -10.0% (100, 11% win) | -9.8% (122, 9% win) | -7.2% (139, 12% win) | -9.3% (160, 8% win) | -9.0% (172, 8% win) | -8.1% (175, 6% win) | -8.9% (133, 5% win) | -7.1% (105, 8% win) | -5.9% (92, 8% win) | -5.2% (63, 8% win) | -5.7% (98, 13% win) |
| volledige_screening+schoon+x_link | -3.5% (61, 21% win) | -10.0% (71, 13% win) | -9.6% (80, 10% win) | -7.1% (85, 13% win) | -9.2% (94, 12% win) | -8.9% (100, 11% win) | -7.9% (104, 9% win) | -9.3% (92, 6% win) | -7.2% (72, 8% win) | -6.2% (63, 8% win) | -6.4% (44, 4% win) | -5.9% (59, 12% win) |

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
| alle | -6.6% (8676, 29% win) | -7.3% (8490, 28% win) | -7.3% (8322, 27% win) | -6.8% (8161, 27% win) | -6.9% (8002, 26% win) | -7.1% (7657, 26% win) | -7.1% (7019, 26% win) | -6.3% (6231, 27% win) | -6.2% (5433, 29% win) | -6.8% (4737, 31% win) | -7.5% (4065, 33% win) |
| schoon | -6.9% (6982, 29% win) | -7.5% (6840, 28% win) | -7.2% (6718, 28% win) | -6.6% (6594, 28% win) | -6.7% (6453, 27% win) | -6.9% (6157, 27% win) | -7.0% (5603, 27% win) | -6.3% (4960, 29% win) | -6.0% (4332, 31% win) | -6.6% (3786, 33% win) | -7.4% (3308, 35% win) |
| bundelgrafiek | -5.4% (1694, 30% win) | -6.7% (1650, 28% win) | -7.6% (1604, 24% win) | -7.4% (1567, 23% win) | -7.7% (1549, 21% win) | -7.8% (1500, 20% win) | -7.5% (1416, 21% win) | -6.2% (1271, 21% win) | -6.8% (1101, 21% win) | -7.7% (951, 22% win) | -7.8% (757, 25% win) |
| schoon+houders_ok | -7.9% (204, 24% win) | -8.9% (246, 23% win) | -8.6% (306, 22% win) | -8.6% (342, 22% win) | -9.7% (382, 19% win) | -8.2% (430, 20% win) | -8.3% (467, 18% win) | -8.5% (429, 20% win) | -8.1% (382, 22% win) | -7.3% (324, 24% win) | -6.9% (254, 27% win) |
| schoon+houders_ok+final_stretch | -7.0% (100, 27% win) | -10.7% (125, 21% win) | -9.5% (162, 22% win) | -9.9% (186, 22% win) | -11.1% (218, 18% win) | -8.6% (248, 20% win) | -10.2% (263, 15% win) | -11.2% (213, 16% win) | -7.2% (185, 23% win) | -6.9% (145, 24% win) | -6.5% (103, 24% win) |
| volledige_screening+schoon | -7.2% (82, 27% win) | -10.8% (100, 19% win) | -11.2% (122, 19% win) | -11.5% (139, 19% win) | -12.7% (160, 16% win) | -9.9% (172, 19% win) | -10.2% (175, 15% win) | -10.5% (133, 16% win) | -8.4% (105, 21% win) | -7.1% (92, 22% win) | -4.5% (63, 25% win) |
| volledige_screening+schoon+x_link | -7.2% (61, 26% win) | -10.0% (71, 20% win) | -12.1% (80, 19% win) | -12.0% (85, 19% win) | -11.8% (94, 18% win) | -7.6% (100, 24% win) | -8.2% (104, 20% win) | -9.8% (92, 18% win) | -8.3% (72, 21% win) | -5.0% (63, 24% win) | -3.6% (44, 27% win) |


## Regel H4: dip 65%, trailing stop vanaf +15% op 10% onder de piek

Tot +15% ligt de stop op hetzelfde niveau als bij de vorige regel — 10%-punt dieper dan de instap — zodat de positie eerst nog kan zakken. Vanaf +15% loopt de stop mee op 10% onder de hoogste koers, en ligt daarmee altijd boven de instapprijs. Geen vaste winstgrens: een uitschieter wordt niet afgekapt.

**Vooraf vastgelegd als H4 op d65 met filter schoon+houders_ok; de rest van deze regel is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.6% (8676, 28% win) | -7.3% (8490, 27% win) | -7.1% (8322, 26% win) | -6.9% (8161, 25% win) | -7.2% (8002, 25% win) | -7.1% (7657, 24% win) | -6.8% (7019, 24% win) | -5.9% (6231, 26% win) | -4.8% (5433, 27% win) | -6.2% (4737, 28% win) | -7.8% (4065, 29% win) |
| schoon | -7.2% (6982, 28% win) | -7.5% (6840, 27% win) | -6.9% (6718, 26% win) | -6.6% (6594, 26% win) | -7.0% (6453, 26% win) | -7.0% (6157, 25% win) | -6.5% (5603, 25% win) | -5.8% (4960, 27% win) | -4.4% (4332, 29% win) | -5.9% (3786, 30% win) | -7.8% (3308, 31% win) |
| bundelgrafiek | -4.4% (1694, 29% win) | -6.4% (1650, 27% win) | -7.7% (1604, 24% win) | -8.2% (1567, 21% win) | -8.2% (1549, 20% win) | -7.2% (1500, 20% win) | -8.0% (1416, 18% win) | -5.9% (1271, 20% win) | -6.3% (1101, 20% win) | -7.4% (951, 20% win) | -8.0% (757, 22% win) |
| schoon+houders_ok | -7.1% (204, 26% win) | -8.4% (246, 23% win) | -8.3% (306, 24% win) | -7.4% (342, 23% win) | -9.4% (382, 19% win) | -9.6% (430, 20% win) | -8.8% (467, 18% win) | -6.8% (429, 22% win) | -7.0% (382, 22% win) | -7.1% (324, 23% win) | -8.6% (254, 22% win) |
| schoon+houders_ok+final_stretch | -5.2% (100, 30% win) | -9.4% (125, 22% win) | -8.8% (162, 26% win) | -7.7% (186, 24% win) | -9.7% (218, 19% win) | -10.2% (248, 19% win) | -10.5% (263, 16% win) | -10.1% (213, 20% win) | -7.9% (185, 20% win) | -8.1% (145, 23% win) | -8.3% (103, 20% win) |
| volledige_screening+schoon | -4.6% (82, 29% win) | -9.2% (100, 18% win) | -10.1% (122, 24% win) | -11.0% (139, 22% win) | -12.6% (160, 17% win) | -11.5% (172, 18% win) | -10.3% (175, 16% win) | -10.7% (133, 20% win) | -9.3% (105, 20% win) | -9.9% (92, 20% win) | -6.8% (63, 21% win) |
| volledige_screening+schoon+x_link | -5.6% (61, 28% win) | -8.8% (71, 17% win) | -11.0% (80, 21% win) | -10.3% (85, 22% win) | -11.3% (94, 20% win) | -10.5% (100, 22% win) | -9.5% (104, 21% win) | -10.5% (92, 18% win) | -9.9% (72, 19% win) | -11.2% (63, 18% win) | -4.8% (44, 18% win) |


## Verkennend: winstgrens tegen dipdiepte

Elke winstgrens bij elke instapdiepte, filter `schoon+houders_ok`, stop als in de video. Dit is het raster waar 8 grenzen x 11 dieptes = 88 cellen uit komen. Bij zoveel cellen zit er door toeval altijd een goede tussen, dus **hier telt geen enkele cel als bewijs** — het is bedoeld om te zien of er ergens een gebied is dat consequent beter is, niet om de beste cel te kiezen.

| winstgrens | d30 | d35 | d40 | d45 | d50 | d55 | d60 | d65 | d70 | d75 | d80 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +10% | -8.1% (204) | -8.5% (246) | -9.1% (306) | -7.5% (342) | -7.6% (382) | -7.4% (430) | -5.7% (467) | -6.6% (429) | -7.0% (382) | -5.5% (324) | -6.0% (254) |
| +15% | -8.4% (204) | -8.9% (246) | -8.8% (306) | -7.3% (342) | -7.7% (382) | -7.2% (430) | -5.7% (467) | -7.0% (429) | -7.0% (382) | -5.4% (324) | -6.0% (254) |
| +20% | -8.3% (204) | -9.1% (246) | -8.9% (306) | -7.5% (342) | -7.8% (382) | -7.3% (430) | -6.2% (467) | -7.5% (429) | -7.2% (382) | -5.6% (324) | -6.1% (254) |
| +25% | -8.0% (204) | -8.5% (246) | -9.0% (306) | -7.2% (342) | -7.9% (382) | -7.2% (430) | -6.2% (467) | -7.6% (429) | -7.0% (382) | -5.6% (324) | -6.6% (254) |
| +30% | -7.3% (204) | -8.2% (246) | -8.6% (306) | -7.3% (342) | -8.4% (382) | -7.2% (430) | -6.4% (467) | -7.5% (429) | -7.3% (382) | -6.3% (324) | -6.4% (254) |
| +35% | -7.8% (204) | -9.2% (246) | -8.5% (306) | -7.0% (342) | -8.4% (382) | -7.3% (430) | -6.4% (467) | -7.1% (429) | -6.9% (382) | -5.8% (324) | -6.5% (254) |
| +45% | -8.3% (204) | -9.3% (246) | -8.6% (306) | -7.6% (342) | -8.3% (382) | -8.2% (430) | -6.6% (467) | -7.1% (429) | -6.4% (382) | -5.1% (324) | -6.3% (254) |
| +60% | -8.3% (204) | -9.0% (246) | -7.7% (306) | -7.1% (342) | -8.0% (382) | -8.8% (430) | -6.6% (467) | -6.2% (429) | -6.1% (382) | -5.5% (324) | -6.5% (254) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 139 instappen, mediane hoogste stijging +9.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 50% | 27% | -7.0% | 25% |
| +15% | 47% | 24% | -6.6% | 23% |
| +20% | 40% | 20% | -6.7% | 20% |
| +25% | 36% | 18% | -6.5% | 19% |
| +30% | 33% | 16% | -6.4% | 17% |
| +35% | 31% | 16% | -5.7% | 17% |
| +45% | 22% | 10% | -7.2% | 12% |
| +60% | 16% | 7% | -7.5% | 9% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 342 instappen, mediane hoogste stijging +10.3%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 50% | 25% | -7.5% | 26% |
| +15% | 47% | 20% | -7.3% | 23% |
| +20% | 43% | 18% | -7.5% | 20% |
| +25% | 40% | 16% | -7.2% | 19% |
| +30% | 37% | 15% | -7.3% | 18% |
| +35% | 34% | 13% | -7.0% | 17% |
| +45% | 29% | 10% | -7.6% | 14% |
| +60% | 25% | 8% | -7.1% | 12% |

**filter `alle`** — variant `d45_direct`, 8161 instappen, mediane hoogste stijging +19.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -6.0% | 29% |
| +15% | 53% | 28% | -5.9% | 28% |
| +20% | 50% | 24% | -6.0% | 26% |
| +25% | 47% | 22% | -6.1% | 25% |
| +30% | 44% | 20% | -6.2% | 24% |
| +35% | 42% | 18% | -6.2% | 24% |
| +45% | 38% | 15% | -6.3% | 22% |
| +60% | 32% | 12% | -6.4% | 20% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -7.6% (82, 18% win) | -6.9% (82, 18% win) | -5.2% (82, 18% win) | -4.5% (82, 18% win) | -7.5% (82, 18% win) | -6.8% (82, 18% win) |
| d35_direct | -13.0% (100, 11% win) | -12.4% (100, 11% win) | -10.6% (100, 11% win) | -10.0% (100, 11% win) | -12.8% (100, 11% win) | -12.1% (100, 11% win) |
| d40_direct | -12.8% (122, 8% win) | -12.2% (122, 9% win) | -10.4% (122, 9% win) | -9.8% (122, 9% win) | -12.7% (122, 8% win) | -12.1% (122, 9% win) |
| d45_direct | -10.2% (139, 11% win) | -9.6% (139, 12% win) | -7.9% (139, 12% win) | -7.2% (139, 12% win) | -10.4% (139, 11% win) | -9.8% (139, 12% win) |
| d50_direct | -12.3% (160, 8% win) | -11.6% (160, 8% win) | -10.0% (160, 8% win) | -9.3% (160, 8% win) | -12.7% (160, 8% win) | -12.0% (160, 8% win) |
| d55_direct | -11.9% (172, 8% win) | -11.2% (172, 8% win) | -9.6% (172, 8% win) | -9.0% (172, 8% win) | -12.5% (172, 8% win) | -11.9% (172, 8% win) |
| d60_direct | -11.0% (175, 6% win) | -10.3% (175, 6% win) | -8.7% (175, 6% win) | -8.1% (175, 6% win) | -11.8% (175, 6% win) | -11.2% (175, 6% win) |
| d65_direct | -11.8% (133, 5% win) | -11.1% (133, 5% win) | -9.5% (133, 5% win) | -8.9% (133, 5% win) | -12.5% (133, 4% win) | -11.9% (133, 5% win) |
| d70_direct | -10.0% (105, 7% win) | -9.3% (105, 7% win) | -7.7% (105, 8% win) | -7.1% (105, 8% win) | -10.8% (105, 7% win) | -10.1% (105, 7% win) |
| d75_direct | -8.8% (92, 8% win) | -8.1% (92, 8% win) | -6.6% (92, 8% win) | -5.9% (92, 8% win) | -9.7% (92, 8% win) | -9.1% (92, 8% win) |
| d80_direct | -8.0% (63, 6% win) | -7.3% (63, 6% win) | -5.9% (63, 6% win) | -5.2% (63, 8% win) | -9.2% (63, 6% win) | -8.5% (63, 6% win) |
| d45_herstel5 | -8.8% (98, 13% win) | -8.1% (98, 13% win) | -6.4% (98, 13% win) | -5.7% (98, 13% win) | -8.8% (98, 13% win) | -8.2% (98, 13% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -11.4% (204, 15% win) | -10.7% (204, 15% win) | -9.0% (204, 16% win) | -8.3% (204, 16% win) | -11.1% (204, 15% win) | -10.5% (204, 16% win) |
| d35_direct | -12.4% (246, 13% win) | -11.7% (246, 13% win) | -10.0% (246, 14% win) | -9.3% (246, 14% win) | -12.1% (246, 13% win) | -11.5% (246, 14% win) |
| d40_direct | -11.7% (306, 12% win) | -11.0% (306, 13% win) | -9.3% (306, 13% win) | -8.6% (306, 13% win) | -11.6% (306, 12% win) | -10.9% (306, 13% win) |
| d45_direct | -10.7% (342, 12% win) | -10.0% (342, 12% win) | -8.3% (342, 13% win) | -7.6% (342, 14% win) | -10.8% (342, 12% win) | -10.1% (342, 13% win) |
| d50_direct | -11.3% (382, 10% win) | -10.6% (382, 10% win) | -9.0% (382, 11% win) | -8.3% (382, 11% win) | -11.6% (382, 10% win) | -11.0% (382, 11% win) |
| d55_direct | -11.1% (430, 10% win) | -10.4% (430, 10% win) | -8.8% (430, 11% win) | -8.2% (430, 11% win) | -11.6% (430, 10% win) | -10.9% (430, 10% win) |
| d60_direct | -9.5% (467, 10% win) | -8.8% (467, 10% win) | -7.3% (467, 10% win) | -6.6% (467, 10% win) | -10.2% (467, 10% win) | -9.6% (467, 10% win) |
| d65_direct | -10.1% (429, 10% win) | -9.4% (429, 10% win) | -7.8% (429, 10% win) | -7.1% (429, 10% win) | -10.8% (429, 10% win) | -10.1% (429, 10% win) |
| d70_direct | -9.3% (382, 11% win) | -8.6% (382, 11% win) | -7.1% (382, 12% win) | -6.4% (382, 12% win) | -10.2% (382, 11% win) | -9.5% (382, 11% win) |
| d75_direct | -8.0% (324, 12% win) | -7.3% (324, 12% win) | -5.8% (324, 13% win) | -5.1% (324, 13% win) | -9.1% (324, 12% win) | -8.4% (324, 12% win) |
| d80_direct | -9.1% (254, 11% win) | -8.4% (254, 11% win) | -6.9% (254, 12% win) | -6.3% (254, 12% win) | -10.5% (254, 11% win) | -9.9% (254, 11% win) |
| d45_herstel5 | -6.5% (243, 19% win) | -5.8% (243, 20% win) | -4.1% (243, 20% win) | -3.4% (243, 20% win) | -6.5% (243, 19% win) | -5.8% (243, 20% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -8.9% (8676, 23% win) | -8.2% (8676, 24% win) | -6.6% (8676, 24% win) | -5.9% (8676, 25% win) | -9.2% (8676, 23% win) | -8.6% (8676, 23% win) |
| d35_direct | -9.6% (8490, 22% win) | -8.9% (8490, 22% win) | -7.3% (8490, 23% win) | -6.6% (8490, 24% win) | -10.1% (8490, 21% win) | -9.4% (8490, 22% win) |
| d40_direct | -9.7% (8322, 21% win) | -9.0% (8322, 21% win) | -7.5% (8322, 22% win) | -6.8% (8322, 22% win) | -10.4% (8322, 20% win) | -9.7% (8322, 21% win) |
| d45_direct | -9.2% (8161, 20% win) | -8.5% (8161, 21% win) | -7.0% (8161, 22% win) | -6.3% (8161, 22% win) | -10.1% (8161, 20% win) | -9.4% (8161, 20% win) |
| d50_direct | -9.2% (8002, 20% win) | -8.6% (8002, 20% win) | -7.1% (8002, 21% win) | -6.4% (8002, 21% win) | -10.4% (8002, 19% win) | -9.8% (8002, 20% win) |
| d55_direct | -9.3% (7657, 19% win) | -8.6% (7657, 20% win) | -7.2% (7657, 20% win) | -6.5% (7657, 21% win) | -10.8% (7657, 19% win) | -10.1% (7657, 19% win) |
| d60_direct | -9.0% (7019, 20% win) | -8.4% (7019, 20% win) | -7.0% (7019, 21% win) | -6.3% (7019, 21% win) | -10.8% (7019, 18% win) | -10.2% (7019, 19% win) |
| d65_direct | -8.2% (6231, 21% win) | -7.5% (6231, 21% win) | -6.2% (6231, 22% win) | -5.6% (6231, 22% win) | -10.5% (6231, 19% win) | -9.9% (6231, 20% win) |
| d70_direct | -8.4% (5433, 22% win) | -7.7% (5433, 22% win) | -6.6% (5433, 22% win) | -5.9% (5433, 23% win) | -11.4% (5433, 20% win) | -10.8% (5433, 20% win) |
| d75_direct | -8.4% (4737, 23% win) | -7.7% (4737, 24% win) | -6.8% (4737, 24% win) | -6.1% (4737, 24% win) | -12.3% (4737, 21% win) | -11.7% (4737, 21% win) |
| d80_direct | -8.0% (4065, 26% win) | -7.3% (4065, 26% win) | -6.7% (4065, 26% win) | -6.1% (4065, 27% win) | -13.7% (4065, 23% win) | -13.1% (4065, 23% win) |
| d45_herstel5 | -8.9% (6523, 24% win) | -8.2% (6523, 24% win) | -6.8% (6523, 25% win) | -6.1% (6523, 26% win) | -10.0% (6523, 23% win) | -9.3% (6523, 24% win) |


## Wat kost de uitvoering echt?

Wij rekenen met 0.001 SOL vaste kosten per transactie. De video van 14 sept gebruikt een tip van 0,02 SOL plus 0,001 prioriteitsfee — twintig keer zoveel. Een vaste fee werkt lineair door: elke extra T SOL per kant verlaagt het rendement met 2T gedeeld door de inzet. Onderstaande EV's zijn daarmee exact doorgerekend, niet opnieuw gesimuleerd. Filter `schoon+houders_ok`, videoregel, PumpPortal.

| extra vaste fee per transactie | inzet 0.05 SOL | inzet 0.2 SOL | inzet 1.0 SOL |
|---|---|---|---|
| +0.0 SOL | -10.0% | -7.6% | -10.1% |
| +0.005 SOL | -30.0% | -12.6% | -11.1% |
| +0.01 SOL | -50.0% | -17.6% | -12.1% |
| +0.02 SOL | -90.0% | -27.6% | -14.1% |

Bij 0,05 SOL inzet eet een tip van 0,02 SOL per kant 84% van de positie op. Een strategie met een randje van een paar procent bestaat bij die instellingen simpelweg niet; bij 1 SOL kost hij 4,2%. Dit verandert onze conclusie niet — de EV was al negatief — maar het laat zien dat kleine inzetten bij deze uitvoering sowieso kansloos zijn, en dat onze eigen cijfers aan de gunstige kant staan.



## Uitstapregels vergeleken (dip 45%, direct)

'Gespreid' is vier gelijke plakjes op +10%, +20%, +30% en +45%, allemaal met dezelfde stop — het advies uit de KOL-video om niet in één keer te verkopen. Dat is rekenkundig het gewogen gemiddelde van de vier losse grenzen, dus het kan de verwachting niet redden; het verandert alleen de spreiding.

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) | gespreid |
|---|---|---|---|---|
| alle | -6.3% (8161, 22% win) | -6.0% (8161, 22% win) | -7.5% (8161, 21% win) | -6.1% (8161, 25% win) |
| schoon | -6.3% (6594, 23% win) | -6.0% (6594, 22% win) | -7.1% (6594, 21% win) | -6.1% (6594, 26% win) |
| bundelgrafiek | -6.1% (1567, 20% win) | -5.9% (1567, 19% win) | -9.2% (1567, 18% win) | -6.0% (1567, 22% win) |
| schoon+houders_ok | -7.6% (342, 14% win) | -7.4% (342, 10% win) | -10.5% (342, 14% win) | -7.5% (342, 20% win) |
| schoon+houders_ok+final_stretch | -5.6% (186, 14% win) | -6.2% (186, 10% win) | -11.2% (186, 14% win) | -6.1% (186, 20% win) |
| volledige_screening+schoon | -7.2% (139, 12% win) | -8.1% (139, 6% win) | -14.8% (139, 12% win) | -6.8% (139, 20% win) |
| volledige_screening+schoon+x_link | -7.1% (85, 13% win) | -8.0% (85, 8% win) | -14.2% (85, 11% win) | -7.5% (85, 19% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.5% (3212, 27% win); 1,3–2x: -7.1% (3381, 18% win); ≥ 2x (bundelgrafiek): -6.2% (1568, 20% win)

**aandeel supply gekocht in creatieblok:** < 5%: -4.7% (4608, 29% win); 5–20%: -8.3% (1403, 13% win); ≥ 20%: -8.2% (2150, 12% win)

**top t.o.v. start:** 2–3x: -5.9% (4670, 21% win); 3–6x: -6.9% (2693, 24% win); ≥ 6x: -6.1% (798, 24% win)

**unieke kopers tot de top:** < 30: -5.2% (4743, 28% win); 30–100: -6.9% (1925, 14% win); ≥ 100: -8.7% (1493, 13% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.7% (2172, 15% win); 1–2: -6.5% (3905, 24% win); ≥ 3 (trap): -5.4% (2084, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -7.8% (2248, 14% win); 10–25%: -8.6% (1656, 11% win); ≥ 25%: -4.6% (4257, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (6300, 25% win); 30 s–3 min: -7.0% (1478, 14% win); ≥ 3 min (langzaam): -8.3% (383, 11% win)

**tijd van start tot top:** < 2 min: -5.8% (6607, 24% win); 2–10 min: -8.8% (1238, 14% win); ≥ 10 min: -6.2% (316, 13% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
