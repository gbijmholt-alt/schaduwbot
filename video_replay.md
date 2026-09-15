# Videostrategie op alle trades — 2026-09-15 18:04 UTC

Tokens sinds 2026-09-13 06:04 UTC: 67358 geschikt (≥ 2 uur oud, geen herstart), 51584 met trades, 9087 haalden 2x de startkoers, 6961 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2109 tokens. Houdercheck echt uitgevoerd bij 95% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 391, winkans 12%, EV per trade -8.1% (95%-marge -10.2% tot -6.1%), mediaan -10.4%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 5659, winkans 22%, EV -7.3% (95%-marge -8.8% tot -5.9%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 198, winkans 18%, EV -9.9% (95%-marge -13.0% tot -6.8%).
- **H4** (2026-09-14 22:00 UTC): instap na een dip van 65% vanaf de top; stop op 75% onder de top zolang de winst onder +15% blijft; vanaf +15% een meelopende stop op 10% onder de hoogste koers; schone grafiek en houdercheck in orde. Aanleiding: voorstel van Gerben, 14 sept. Combineert de twee hefbomen die los gemeten het minst slecht waren: dieper instappen (d65-d70 gaf -3,8% tot -4,7% tegen -6,9% bij d45) en eerder winst vastleggen (+10% gaf -5,4% tegen -6,9% bij +45%), maar dan met een meelopende stop zodat een uitschieter niet wordt afgekapt. Filter is 'schoon+houders_ok' en niet de volledige screening, omdat die screening in drie onafhankelijke metingen averechts werkt. Verwachting vooraf, zodat die toetsbaar is: rond -3%, dus nog steeds negatief.. Resultaat: n = 3, winkans 33%, EV -4.2% (95%-marge -9.9% tot +1.6%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 6961 | 38% | 78% | 34% |
| schoon | 5659 | 39% | 78% | 36% |
| bundelgrafiek | 1302 | 34% | 78% | 25% |
| schoon+houders_ok | 391 | 27% | 82% | 7% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -5.6% (7424, 25% win) | -6.4% (7251, 24% win) | -6.7% (7100, 23% win) | -6.1% (6961, 23% win) | -6.2% (6823, 22% win) | -6.4% (6535, 21% win) | -6.3% (5993, 21% win) | -5.6% (5333, 23% win) | -5.7% (4669, 24% win) | -6.2% (4106, 24% win) | -6.2% (3561, 27% win) | -5.9% (5591, 26% win) |
| schoon | -6.4% (6007, 25% win) | -7.0% (5876, 24% win) | -7.0% (5767, 23% win) | -6.3% (5659, 23% win) | -6.1% (5536, 23% win) | -6.4% (5285, 22% win) | -6.3% (4812, 22% win) | -6.0% (4274, 24% win) | -5.7% (3752, 25% win) | -6.0% (3297, 26% win) | -6.3% (2903, 29% win) | -6.2% (4671, 26% win) |
| bundelgrafiek | -2.4% (1417, 27% win) | -3.8% (1375, 26% win) | -5.0% (1333, 22% win) | -5.3% (1302, 20% win) | -6.2% (1287, 18% win) | -6.6% (1250, 17% win) | -6.3% (1181, 16% win) | -3.7% (1059, 18% win) | -5.7% (917, 18% win) | -6.7% (809, 18% win) | -5.8% (658, 21% win) | -4.4% (920, 25% win) |
| schoon+houders_ok | -7.0% (245, 16% win) | -8.8% (288, 14% win) | -8.6% (352, 13% win) | -8.1% (391, 12% win) | -8.8% (436, 11% win) | -8.3% (495, 11% win) | -7.0% (539, 10% win) | -7.3% (496, 10% win) | -6.3% (439, 11% win) | -6.0% (360, 12% win) | -6.4% (281, 12% win) | -4.7% (281, 18% win) |
| schoon+houders_ok+final_stretch | -5.5% (125, 17% win) | -9.6% (151, 11% win) | -8.1% (192, 12% win) | -6.8% (217, 13% win) | -9.0% (252, 9% win) | -8.2% (284, 9% win) | -8.0% (301, 7% win) | -8.3% (247, 6% win) | -5.8% (214, 10% win) | -6.3% (160, 8% win) | -6.0% (112, 8% win) | -4.5% (157, 17% win) |
| volledige_screening+schoon | -4.2% (104, 18% win) | -10.1% (123, 10% win) | -9.4% (148, 10% win) | -8.3% (164, 11% win) | -10.0% (186, 7% win) | -9.6% (198, 7% win) | -8.3% (199, 6% win) | -8.3% (153, 6% win) | -6.5% (123, 8% win) | -6.4% (104, 7% win) | -5.7% (70, 7% win) | -6.8% (116, 12% win) |
| volledige_screening+schoon+x_link | -3.7% (77, 21% win) | -10.4% (87, 12% win) | -9.5% (97, 10% win) | -8.3% (102, 12% win) | -9.8% (112, 10% win) | -9.8% (118, 9% win) | -8.5% (122, 7% win) | -8.8% (107, 8% win) | -7.4% (87, 8% win) | -6.8% (74, 7% win) | -7.0% (51, 4% win) | -7.1% (72, 11% win) |

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
| alle | -6.4% (7424, 30% win) | -7.3% (7251, 28% win) | -7.1% (7100, 27% win) | -6.5% (6961, 27% win) | -6.9% (6823, 27% win) | -7.0% (6535, 26% win) | -7.1% (5993, 26% win) | -6.5% (5333, 28% win) | -6.6% (4669, 29% win) | -7.2% (4106, 31% win) | -7.7% (3561, 33% win) |
| schoon | -6.7% (6007, 29% win) | -7.6% (5876, 28% win) | -7.1% (5767, 28% win) | -6.5% (5659, 28% win) | -6.8% (5536, 28% win) | -6.9% (5285, 28% win) | -7.1% (4812, 28% win) | -6.7% (4274, 29% win) | -6.3% (3752, 31% win) | -6.8% (3297, 33% win) | -7.5% (2903, 35% win) |
| bundelgrafiek | -4.9% (1417, 31% win) | -6.1% (1375, 28% win) | -7.3% (1333, 25% win) | -6.8% (1302, 23% win) | -7.3% (1287, 22% win) | -7.8% (1250, 20% win) | -6.8% (1181, 21% win) | -6.0% (1059, 21% win) | -7.7% (917, 21% win) | -8.8% (809, 22% win) | -8.7% (658, 25% win) |
| schoon+houders_ok | -7.0% (245, 24% win) | -8.5% (288, 23% win) | -8.0% (352, 22% win) | -8.7% (391, 22% win) | -10.1% (436, 19% win) | -8.3% (495, 20% win) | -8.4% (539, 17% win) | -8.6% (496, 20% win) | -7.7% (439, 22% win) | -7.5% (360, 25% win) | -7.1% (281, 26% win) |
| schoon+houders_ok+final_stretch | -6.3% (125, 26% win) | -9.9% (151, 21% win) | -8.7% (192, 22% win) | -10.5% (217, 20% win) | -11.3% (252, 18% win) | -8.6% (284, 20% win) | -10.2% (301, 15% win) | -11.2% (247, 15% win) | -7.7% (214, 22% win) | -7.8% (160, 22% win) | -7.3% (112, 23% win) |
| volledige_screening+schoon | -7.0% (104, 25% win) | -9.9% (123, 20% win) | -10.1% (148, 20% win) | -12.1% (164, 18% win) | -12.5% (186, 15% win) | -9.9% (198, 18% win) | -9.9% (199, 15% win) | -10.1% (153, 17% win) | -8.4% (123, 20% win) | -7.7% (104, 20% win) | -5.6% (70, 24% win) |
| volledige_screening+schoon+x_link | -7.3% (77, 25% win) | -9.8% (87, 18% win) | -11.6% (97, 19% win) | -12.1% (102, 18% win) | -11.4% (112, 17% win) | -8.3% (118, 22% win) | -8.4% (122, 19% win) | -9.5% (107, 19% win) | -9.0% (87, 18% win) | -6.2% (74, 22% win) | -5.1% (51, 26% win) |


## Regel H4: dip 65%, trailing stop vanaf +15% op 10% onder de piek

Tot +15% ligt de stop op hetzelfde niveau als bij de vorige regel — 10%-punt dieper dan de instap — zodat de positie eerst nog kan zakken. Vanaf +15% loopt de stop mee op 10% onder de hoogste koers, en ligt daarmee altijd boven de instapprijs. Geen vaste winstgrens: een uitschieter wordt niet afgekapt.

**Vooraf vastgelegd als H4 op d65 met filter schoon+houders_ok; de rest van deze regel is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.4% (7424, 28% win) | -7.3% (7251, 27% win) | -7.2% (7100, 26% win) | -7.1% (6961, 26% win) | -7.5% (6823, 25% win) | -7.1% (6535, 24% win) | -6.8% (5993, 24% win) | -6.2% (5333, 26% win) | -5.3% (4669, 27% win) | -6.9% (4106, 28% win) | -8.2% (3561, 29% win) |
| schoon | -7.1% (6007, 28% win) | -7.6% (5876, 27% win) | -7.1% (5767, 26% win) | -6.9% (5659, 26% win) | -7.4% (5536, 26% win) | -7.0% (5285, 26% win) | -6.5% (4812, 25% win) | -6.2% (4274, 27% win) | -4.7% (3752, 29% win) | -6.4% (3297, 29% win) | -8.0% (2903, 31% win) |
| bundelgrafiek | -3.8% (1417, 30% win) | -5.9% (1375, 28% win) | -7.4% (1333, 24% win) | -7.8% (1302, 22% win) | -8.1% (1287, 20% win) | -7.6% (1250, 20% win) | -7.9% (1181, 18% win) | -6.3% (1059, 20% win) | -7.7% (917, 20% win) | -8.8% (809, 20% win) | -9.1% (658, 21% win) |
| schoon+houders_ok | -6.4% (245, 26% win) | -8.3% (288, 23% win) | -8.4% (352, 24% win) | -7.9% (391, 23% win) | -10.0% (436, 19% win) | -9.7% (495, 20% win) | -9.2% (539, 18% win) | -7.3% (496, 21% win) | -6.7% (439, 22% win) | -7.4% (360, 23% win) | -8.6% (281, 22% win) |
| schoon+houders_ok+final_stretch | -4.9% (125, 28% win) | -9.3% (151, 22% win) | -8.7% (192, 25% win) | -8.6% (217, 23% win) | -10.2% (252, 19% win) | -10.2% (284, 19% win) | -10.7% (301, 16% win) | -10.1% (247, 19% win) | -8.3% (214, 20% win) | -8.9% (160, 22% win) | -8.9% (112, 20% win) |
| volledige_screening+schoon | -5.4% (104, 27% win) | -9.0% (123, 19% win) | -9.8% (148, 23% win) | -11.6% (164, 21% win) | -12.5% (186, 17% win) | -11.4% (198, 18% win) | -10.2% (199, 17% win) | -10.0% (153, 20% win) | -9.0% (123, 20% win) | -10.2% (104, 19% win) | -7.8% (70, 20% win) |
| volledige_screening+schoon+x_link | -6.2% (77, 26% win) | -8.6% (87, 17% win) | -11.1% (97, 19% win) | -10.6% (102, 22% win) | -11.1% (112, 20% win) | -11.0% (118, 20% win) | -9.5% (122, 20% win) | -9.6% (107, 19% win) | -10.3% (87, 18% win) | -11.5% (74, 18% win) | -6.4% (51, 18% win) |


## Verkennend: winstgrens tegen dipdiepte

Elke winstgrens bij elke instapdiepte, filter `schoon+houders_ok`, stop als in de video. Dit is het raster waar 8 grenzen x 11 dieptes = 88 cellen uit komen. Bij zoveel cellen zit er door toeval altijd een goede tussen, dus **hier telt geen enkele cel als bewijs** — het is bedoeld om te zien of er ergens een gebied is dat consequent beter is, niet om de beste cel te kiezen.

| winstgrens | d30 | d35 | d40 | d45 | d50 | d55 | d60 | d65 | d70 | d75 | d80 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +10% | -8.0% (245) | -8.3% (288) | -8.6% (352) | -7.4% (391) | -8.0% (436) | -7.3% (495) | -6.0% (539) | -6.4% (496) | -6.8% (439) | -6.2% (360) | -6.6% (281) |
| +15% | -8.2% (245) | -8.6% (288) | -8.2% (352) | -7.3% (391) | -8.2% (436) | -7.4% (495) | -6.0% (539) | -6.9% (496) | -6.9% (439) | -6.2% (360) | -6.4% (281) |
| +20% | -7.9% (245) | -8.6% (288) | -8.1% (352) | -7.5% (391) | -8.3% (436) | -7.4% (495) | -6.4% (539) | -7.5% (496) | -7.1% (439) | -6.3% (360) | -6.2% (281) |
| +25% | -7.3% (245) | -8.2% (288) | -8.2% (352) | -7.5% (391) | -8.3% (436) | -7.4% (495) | -6.4% (539) | -7.6% (496) | -7.0% (439) | -6.3% (360) | -6.6% (281) |
| +30% | -6.7% (245) | -8.0% (288) | -8.0% (352) | -7.6% (391) | -8.8% (436) | -7.4% (495) | -6.5% (539) | -7.4% (496) | -7.3% (439) | -6.9% (360) | -6.8% (281) |
| +35% | -7.0% (245) | -8.9% (288) | -8.1% (352) | -7.5% (391) | -8.9% (436) | -7.5% (495) | -6.8% (539) | -7.1% (496) | -6.8% (439) | -6.4% (360) | -6.8% (281) |
| +45% | -7.0% (245) | -8.8% (288) | -8.6% (352) | -8.1% (391) | -8.8% (436) | -8.3% (495) | -7.0% (539) | -7.3% (496) | -6.3% (439) | -6.0% (360) | -6.4% (281) |
| +60% | -7.5% (245) | -9.0% (288) | -8.3% (352) | -7.8% (391) | -8.5% (436) | -8.9% (495) | -7.1% (539) | -6.6% (496) | -6.1% (439) | -6.2% (360) | -6.6% (281) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 164 instappen, mediane hoogste stijging +9.2%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 49% | 27% | -7.0% | 26% |
| +15% | 46% | 24% | -6.9% | 23% |
| +20% | 40% | 20% | -7.0% | 20% |
| +25% | 35% | 17% | -7.4% | 18% |
| +30% | 32% | 15% | -7.4% | 16% |
| +35% | 30% | 14% | -7.0% | 15% |
| +45% | 22% | 9% | -8.3% | 11% |
| +60% | 16% | 7% | -8.5% | 8% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 391 instappen, mediane hoogste stijging +9.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 50% | 26% | -7.4% | 26% |
| +15% | 46% | 21% | -7.3% | 23% |
| +20% | 42% | 18% | -7.5% | 20% |
| +25% | 39% | 16% | -7.5% | 19% |
| +30% | 36% | 14% | -7.6% | 17% |
| +35% | 34% | 12% | -7.5% | 16% |
| +45% | 28% | 9% | -8.1% | 12% |
| +60% | 24% | 8% | -7.8% | 11% |

**filter `alle`** — variant `d45_direct`, 6961 instappen, mediane hoogste stijging +20.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.7% | 30% |
| +15% | 54% | 29% | -5.6% | 28% |
| +20% | 50% | 25% | -5.6% | 27% |
| +25% | 47% | 22% | -5.8% | 26% |
| +30% | 44% | 20% | -5.8% | 25% |
| +35% | 42% | 18% | -5.9% | 24% |
| +45% | 38% | 15% | -6.1% | 23% |
| +60% | 33% | 12% | -6.2% | 21% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -7.3% (104, 18% win) | -6.7% (104, 18% win) | -5.0% (104, 18% win) | -4.2% (104, 18% win) | -7.2% (104, 18% win) | -6.6% (104, 18% win) |
| d35_direct | -13.2% (123, 10% win) | -12.5% (123, 10% win) | -10.8% (123, 10% win) | -10.1% (123, 10% win) | -12.9% (123, 10% win) | -12.3% (123, 10% win) |
| d40_direct | -12.5% (148, 9% win) | -11.8% (148, 10% win) | -10.1% (148, 10% win) | -9.4% (148, 10% win) | -12.4% (148, 9% win) | -11.8% (148, 10% win) |
| d45_direct | -11.3% (164, 10% win) | -10.7% (164, 10% win) | -9.0% (164, 10% win) | -8.3% (164, 11% win) | -11.5% (164, 10% win) | -10.8% (164, 10% win) |
| d50_direct | -12.9% (186, 6% win) | -12.3% (186, 6% win) | -10.6% (186, 7% win) | -10.0% (186, 7% win) | -13.3% (186, 6% win) | -12.7% (186, 6% win) |
| d55_direct | -12.5% (198, 7% win) | -11.9% (198, 7% win) | -10.3% (198, 7% win) | -9.6% (198, 7% win) | -13.1% (198, 7% win) | -12.5% (198, 7% win) |
| d60_direct | -11.2% (199, 6% win) | -10.5% (199, 6% win) | -8.9% (199, 6% win) | -8.3% (199, 6% win) | -11.9% (199, 6% win) | -11.3% (199, 6% win) |
| d65_direct | -11.2% (153, 6% win) | -10.5% (153, 6% win) | -8.9% (153, 6% win) | -8.3% (153, 6% win) | -11.9% (153, 6% win) | -11.3% (153, 6% win) |
| d70_direct | -9.4% (123, 7% win) | -8.7% (123, 7% win) | -7.1% (123, 8% win) | -6.5% (123, 8% win) | -10.2% (123, 7% win) | -9.6% (123, 7% win) |
| d75_direct | -9.3% (104, 7% win) | -8.6% (104, 7% win) | -7.1% (104, 7% win) | -6.4% (104, 7% win) | -10.2% (104, 7% win) | -9.6% (104, 7% win) |
| d80_direct | -8.6% (70, 6% win) | -7.9% (70, 6% win) | -6.4% (70, 6% win) | -5.7% (70, 7% win) | -9.7% (70, 6% win) | -9.0% (70, 6% win) |
| d45_herstel5 | -9.8% (116, 12% win) | -9.1% (116, 12% win) | -7.4% (116, 12% win) | -6.8% (116, 12% win) | -9.8% (116, 12% win) | -9.2% (116, 12% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.1% (245, 16% win) | -9.4% (245, 16% win) | -7.7% (245, 16% win) | -7.0% (245, 16% win) | -9.9% (245, 16% win) | -9.2% (245, 16% win) |
| d35_direct | -11.9% (288, 13% win) | -11.2% (288, 13% win) | -9.5% (288, 14% win) | -8.8% (288, 14% win) | -11.7% (288, 13% win) | -11.1% (288, 14% win) |
| d40_direct | -11.6% (352, 12% win) | -11.0% (352, 13% win) | -9.2% (352, 13% win) | -8.6% (352, 13% win) | -11.6% (352, 12% win) | -10.9% (352, 13% win) |
| d45_direct | -11.2% (391, 11% win) | -10.5% (391, 12% win) | -8.8% (391, 12% win) | -8.1% (391, 12% win) | -11.3% (391, 11% win) | -10.7% (391, 12% win) |
| d50_direct | -11.8% (436, 10% win) | -11.2% (436, 10% win) | -9.5% (436, 10% win) | -8.8% (436, 11% win) | -12.1% (436, 10% win) | -11.5% (436, 10% win) |
| d55_direct | -11.3% (495, 10% win) | -10.6% (495, 10% win) | -9.0% (495, 11% win) | -8.3% (495, 11% win) | -11.7% (495, 10% win) | -11.1% (495, 10% win) |
| d60_direct | -9.9% (539, 9% win) | -9.2% (539, 9% win) | -7.6% (539, 10% win) | -7.0% (539, 10% win) | -10.6% (539, 9% win) | -10.0% (539, 9% win) |
| d65_direct | -10.2% (496, 10% win) | -9.6% (496, 10% win) | -8.0% (496, 10% win) | -7.3% (496, 10% win) | -10.9% (496, 9% win) | -10.3% (496, 10% win) |
| d70_direct | -9.2% (439, 11% win) | -8.5% (439, 11% win) | -6.9% (439, 11% win) | -6.3% (439, 11% win) | -10.1% (439, 11% win) | -9.4% (439, 11% win) |
| d75_direct | -8.8% (360, 11% win) | -8.2% (360, 11% win) | -6.7% (360, 12% win) | -6.0% (360, 12% win) | -9.9% (360, 11% win) | -9.3% (360, 11% win) |
| d80_direct | -9.2% (281, 11% win) | -8.5% (281, 11% win) | -7.0% (281, 12% win) | -6.4% (281, 12% win) | -10.7% (281, 11% win) | -10.0% (281, 11% win) |
| d45_herstel5 | -7.8% (281, 17% win) | -7.1% (281, 18% win) | -5.4% (281, 18% win) | -4.7% (281, 18% win) | -7.7% (281, 17% win) | -7.0% (281, 18% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -8.6% (7424, 24% win) | -7.9% (7424, 24% win) | -6.3% (7424, 25% win) | -5.6% (7424, 25% win) | -9.0% (7424, 23% win) | -8.3% (7424, 24% win) |
| d35_direct | -9.4% (7251, 22% win) | -8.7% (7251, 23% win) | -7.1% (7251, 24% win) | -6.4% (7251, 24% win) | -9.8% (7251, 22% win) | -9.2% (7251, 22% win) |
| d40_direct | -9.6% (7100, 21% win) | -8.9% (7100, 22% win) | -7.3% (7100, 22% win) | -6.7% (7100, 23% win) | -10.2% (7100, 21% win) | -9.6% (7100, 21% win) |
| d45_direct | -9.0% (6961, 21% win) | -8.3% (6961, 21% win) | -6.8% (6961, 22% win) | -6.1% (6961, 23% win) | -9.9% (6961, 20% win) | -9.2% (6961, 21% win) |
| d50_direct | -9.0% (6823, 21% win) | -8.3% (6823, 21% win) | -6.8% (6823, 22% win) | -6.2% (6823, 22% win) | -10.2% (6823, 20% win) | -9.5% (6823, 20% win) |
| d55_direct | -9.2% (6535, 20% win) | -8.5% (6535, 20% win) | -7.1% (6535, 21% win) | -6.4% (6535, 21% win) | -10.7% (6535, 19% win) | -10.0% (6535, 19% win) |
| d60_direct | -9.0% (5993, 20% win) | -8.3% (5993, 20% win) | -7.0% (5993, 21% win) | -6.3% (5993, 21% win) | -10.8% (5993, 19% win) | -10.2% (5993, 19% win) |
| d65_direct | -8.2% (5333, 21% win) | -7.5% (5333, 22% win) | -6.3% (5333, 22% win) | -5.6% (5333, 23% win) | -10.5% (5333, 20% win) | -9.9% (5333, 20% win) |
| d70_direct | -8.2% (4669, 23% win) | -7.4% (4669, 23% win) | -6.3% (4669, 23% win) | -5.7% (4669, 24% win) | -11.2% (4669, 20% win) | -10.6% (4669, 21% win) |
| d75_direct | -8.5% (4106, 24% win) | -7.8% (4106, 24% win) | -6.8% (4106, 24% win) | -6.2% (4106, 24% win) | -12.4% (4106, 21% win) | -11.8% (4106, 21% win) |
| d80_direct | -8.2% (3561, 26% win) | -7.5% (3561, 26% win) | -6.9% (3561, 27% win) | -6.2% (3561, 27% win) | -13.8% (3561, 23% win) | -13.2% (3561, 23% win) |
| d45_herstel5 | -8.8% (5591, 25% win) | -8.1% (5591, 25% win) | -6.6% (5591, 26% win) | -5.9% (5591, 26% win) | -9.9% (5591, 24% win) | -9.2% (5591, 24% win) |


## Wat kost de uitvoering echt?

Wij rekenen met 0.001 SOL vaste kosten per transactie. De video van 14 sept gebruikt een tip van 0,02 SOL plus 0,001 prioriteitsfee — twintig keer zoveel. Een vaste fee werkt lineair door: elke extra T SOL per kant verlaagt het rendement met 2T gedeeld door de inzet. Onderstaande EV's zijn daarmee exact doorgerekend, niet opnieuw gesimuleerd. Filter `schoon+houders_ok`, videoregel, PumpPortal.

| extra vaste fee per transactie | inzet 0.05 SOL | inzet 0.2 SOL | inzet 1.0 SOL |
|---|---|---|---|
| +0.0 SOL | -10.5% | -8.1% | -10.7% |
| +0.005 SOL | -30.5% | -13.1% | -11.6% |
| +0.01 SOL | -50.5% | -18.1% | -12.7% |
| +0.02 SOL | -90.5% | -28.1% | -14.6% |

Bij 0,05 SOL inzet eet een tip van 0,02 SOL per kant 84% van de positie op. Een strategie met een randje van een paar procent bestaat bij die instellingen simpelweg niet; bij 1 SOL kost hij 4,2%. Dit verandert onze conclusie niet — de EV was al negatief — maar het laat zien dat kleine inzetten bij deze uitvoering sowieso kansloos zijn, en dat onze eigen cijfers aan de gunstige kant staan.



## Uitstapregels vergeleken (dip 45%, direct)

'Gespreid' is vier gelijke plakjes op +10%, +20%, +30% en +45%, allemaal met dezelfde stop — het advies uit de KOL-video om niet in één keer te verkopen. Dat is rekenkundig het gewogen gemiddelde van de vier losse grenzen, dus het kan de verwachting niet redden; het verandert alleen de spreiding.

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) | gespreid |
|---|---|---|---|---|
| alle | -6.1% (6961, 23% win) | -5.9% (6961, 22% win) | -7.6% (6961, 21% win) | -5.8% (6961, 26% win) |
| schoon | -6.3% (5659, 23% win) | -6.1% (5659, 23% win) | -7.3% (5659, 22% win) | -5.9% (5659, 26% win) |
| bundelgrafiek | -5.3% (1302, 20% win) | -5.2% (1302, 20% win) | -8.6% (1302, 18% win) | -5.2% (1302, 22% win) |
| schoon+houders_ok | -8.1% (391, 12% win) | -7.8% (391, 10% win) | -10.7% (391, 14% win) | -7.7% (391, 19% win) |
| schoon+houders_ok+final_stretch | -6.8% (217, 13% win) | -7.1% (217, 9% win) | -12.1% (217, 14% win) | -6.7% (217, 20% win) |
| volledige_screening+schoon | -8.3% (164, 11% win) | -9.0% (164, 6% win) | -15.4% (164, 11% win) | -7.4% (164, 19% win) |
| volledige_screening+schoon+x_link | -8.3% (102, 12% win) | -9.2% (102, 7% win) | -14.9% (102, 10% win) | -7.7% (102, 19% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.6% (2835, 28% win); 1,3–2x: -6.9% (2823, 19% win); ≥ 2x (bundelgrafiek): -5.3% (1303, 20% win)

**aandeel supply gekocht in creatieblok:** < 5%: -4.7% (4079, 30% win); 5–20%: -8.1% (1169, 13% win); ≥ 20%: -8.0% (1713, 13% win)

**top t.o.v. start:** 2–3x: -5.7% (4001, 21% win); 3–6x: -6.8% (2286, 24% win); ≥ 6x: -5.7% (674, 25% win)

**unieke kopers tot de top:** < 30: -5.1% (4148, 29% win); 30–100: -6.7% (1589, 13% win); ≥ 100: -8.6% (1224, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -5.8% (1759, 16% win); 1–2: -6.5% (3344, 24% win); ≥ 3 (trap): -5.6% (1858, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -7.8% (1855, 15% win); 10–25%: -8.7% (1273, 11% win); ≥ 25%: -4.4% (3833, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.7% (5336, 26% win); 30 s–3 min: -7.1% (1280, 13% win); ≥ 3 min (langzaam): -7.9% (345, 11% win)

**tijd van start tot top:** < 2 min: -5.8% (5612, 25% win); 2–10 min: -7.9% (1084, 14% win); ≥ 10 min: -5.4% (265, 13% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
