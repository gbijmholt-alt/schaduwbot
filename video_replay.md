# Videostrategie op alle trades — 2026-09-15 20:07 UTC

Tokens sinds 2026-09-13 08:07 UTC: 70021 geschikt (≥ 2 uur oud, geen herstart), 53536 met trades, 9484 haalden 2x de startkoers, 7292 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2206 tokens. Houdercheck echt uitgevoerd bij 95% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 382, winkans 13%, EV per trade -8.1% (95%-marge -10.2% tot -6.1%), mediaan -10.3%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 5913, winkans 22%, EV -7.3% (95%-marge -8.6% tot -5.9%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 193, winkans 19%, EV -9.8% (95%-marge -12.9% tot -6.6%).
- **H4** (2026-09-14 22:00 UTC): instap na een dip van 65% vanaf de top; stop op 75% onder de top zolang de winst onder +15% blijft; vanaf +15% een meelopende stop op 10% onder de hoogste koers; schone grafiek en houdercheck in orde. Aanleiding: voorstel van Gerben, 14 sept. Combineert de twee hefbomen die los gemeten het minst slecht waren: dieper instappen (d65-d70 gaf -3,8% tot -4,7% tegen -6,9% bij d45) en eerder winst vastleggen (+10% gaf -5,4% tegen -6,9% bij +45%), maar dan met een meelopende stop zodat een uitschieter niet wordt afgekapt. Filter is 'schoon+houders_ok' en niet de volledige screening, omdat die screening in drie onafhankelijke metingen averechts werkt. Verwachting vooraf, zodat die toetsbaar is: rond -3%, dus nog steeds negatief.. Resultaat: n = 3, winkans 33%, EV -4.2% (95%-marge -9.9% tot +1.6%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 7292 | 38% | 79% | 33% |
| schoon | 5913 | 39% | 79% | 36% |
| bundelgrafiek | 1379 | 34% | 78% | 24% |
| schoon+houders_ok | 382 | 27% | 82% | 6% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -5.6% (7769, 26% win) | -6.3% (7593, 24% win) | -6.5% (7439, 23% win) | -6.1% (7292, 22% win) | -6.2% (7145, 22% win) | -6.5% (6841, 21% win) | -6.4% (6272, 21% win) | -5.5% (5591, 23% win) | -5.8% (4898, 23% win) | -6.3% (4303, 24% win) | -6.2% (3720, 27% win) | -6.0% (5838, 26% win) |
| schoon | -6.4% (6270, 25% win) | -7.0% (6137, 24% win) | -6.9% (6027, 23% win) | -6.3% (5913, 23% win) | -6.2% (5783, 23% win) | -6.4% (5521, 22% win) | -6.3% (5025, 22% win) | -5.9% (4471, 24% win) | -5.8% (3927, 25% win) | -6.2% (3448, 26% win) | -6.3% (3030, 29% win) | -6.3% (4864, 26% win) |
| bundelgrafiek | -2.4% (1499, 27% win) | -3.7% (1456, 26% win) | -5.1% (1412, 22% win) | -5.4% (1379, 20% win) | -6.4% (1362, 18% win) | -6.8% (1320, 16% win) | -6.6% (1247, 16% win) | -4.1% (1120, 18% win) | -5.9% (971, 17% win) | -6.9% (855, 17% win) | -5.9% (690, 20% win) | -4.8% (974, 25% win) |
| schoon+houders_ok | -7.6% (234, 16% win) | -9.3% (279, 13% win) | -8.6% (344, 13% win) | -8.1% (382, 13% win) | -8.6% (424, 11% win) | -8.2% (479, 11% win) | -6.9% (522, 10% win) | -7.2% (482, 10% win) | -6.0% (426, 12% win) | -5.6% (353, 12% win) | -5.9% (275, 12% win) | -4.7% (274, 19% win) |
| schoon+houders_ok+final_stretch | -5.6% (119, 17% win) | -9.6% (145, 11% win) | -8.2% (186, 12% win) | -6.8% (211, 13% win) | -8.8% (244, 9% win) | -8.0% (276, 9% win) | -8.0% (293, 8% win) | -8.5% (240, 6% win) | -5.7% (209, 10% win) | -6.3% (159, 8% win) | -6.0% (111, 8% win) | -4.5% (153, 16% win) |
| volledige_screening+schoon | -4.2% (98, 18% win) | -10.1% (117, 10% win) | -9.7% (142, 10% win) | -8.5% (159, 11% win) | -9.9% (181, 7% win) | -9.5% (193, 7% win) | -8.2% (194, 6% win) | -8.6% (150, 6% win) | -6.4% (121, 8% win) | -6.3% (103, 7% win) | -5.6% (69, 7% win) | -7.0% (113, 12% win) |
| volledige_screening+schoon+x_link | -3.8% (73, 20% win) | -10.3% (83, 12% win) | -9.3% (93, 11% win) | -8.5% (98, 11% win) | -9.7% (108, 10% win) | -9.7% (114, 10% win) | -8.5% (118, 8% win) | -9.3% (104, 7% win) | -7.4% (85, 8% win) | -6.7% (73, 7% win) | -6.9% (50, 4% win) | -7.5% (69, 10% win) |

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
| alle | -6.3% (7769, 30% win) | -7.2% (7593, 28% win) | -7.0% (7439, 27% win) | -6.6% (7292, 27% win) | -6.9% (7145, 26% win) | -7.0% (6841, 26% win) | -7.2% (6272, 26% win) | -6.5% (5591, 27% win) | -6.5% (4898, 29% win) | -7.2% (4303, 30% win) | -7.7% (3720, 33% win) |
| schoon | -6.7% (6270, 29% win) | -7.4% (6137, 28% win) | -7.0% (6027, 28% win) | -6.6% (5913, 28% win) | -6.7% (5783, 28% win) | -6.8% (5521, 27% win) | -7.2% (5025, 27% win) | -6.5% (4471, 29% win) | -6.2% (3927, 31% win) | -6.9% (3448, 33% win) | -7.5% (3030, 35% win) |
| bundelgrafiek | -5.1% (1499, 31% win) | -6.2% (1456, 28% win) | -7.4% (1412, 25% win) | -6.8% (1379, 23% win) | -7.5% (1362, 21% win) | -8.0% (1320, 20% win) | -7.2% (1247, 20% win) | -6.4% (1120, 20% win) | -7.6% (971, 21% win) | -8.7% (855, 21% win) | -8.5% (690, 25% win) |
| schoon+houders_ok | -7.6% (234, 24% win) | -8.8% (279, 23% win) | -8.2% (344, 22% win) | -8.7% (382, 22% win) | -9.6% (424, 19% win) | -8.3% (479, 20% win) | -8.4% (522, 17% win) | -8.7% (482, 20% win) | -8.1% (426, 22% win) | -7.3% (353, 25% win) | -6.7% (275, 26% win) |
| schoon+houders_ok+final_stretch | -6.1% (119, 26% win) | -10.1% (145, 21% win) | -8.8% (186, 22% win) | -10.6% (211, 20% win) | -10.9% (244, 18% win) | -8.5% (276, 20% win) | -10.1% (293, 15% win) | -11.3% (240, 15% win) | -7.6% (209, 22% win) | -7.8% (159, 23% win) | -7.2% (111, 23% win) |
| volledige_screening+schoon | -6.8% (98, 26% win) | -10.1% (117, 20% win) | -10.3% (142, 20% win) | -12.2% (159, 18% win) | -12.4% (181, 16% win) | -9.8% (193, 19% win) | -10.2% (194, 15% win) | -10.4% (150, 17% win) | -8.4% (121, 21% win) | -7.7% (103, 20% win) | -5.5% (69, 25% win) |
| volledige_screening+schoon+x_link | -7.2% (73, 25% win) | -9.7% (83, 19% win) | -11.5% (93, 18% win) | -12.3% (98, 17% win) | -11.2% (108, 18% win) | -8.1% (114, 23% win) | -8.7% (118, 19% win) | -9.9% (104, 18% win) | -9.0% (85, 19% win) | -6.2% (73, 22% win) | -5.1% (50, 26% win) |


## Regel H4: dip 65%, trailing stop vanaf +15% op 10% onder de piek

Tot +15% ligt de stop op hetzelfde niveau als bij de vorige regel — 10%-punt dieper dan de instap — zodat de positie eerst nog kan zakken. Vanaf +15% loopt de stop mee op 10% onder de hoogste koers, en ligt daarmee altijd boven de instapprijs. Geen vaste winstgrens: een uitschieter wordt niet afgekapt.

**Vooraf vastgelegd als H4 op d65 met filter schoon+houders_ok; de rest van deze regel is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.4% (7769, 28% win) | -7.2% (7593, 27% win) | -7.1% (7439, 26% win) | -7.1% (7292, 25% win) | -7.4% (7145, 25% win) | -7.1% (6841, 24% win) | -6.9% (6272, 24% win) | -5.9% (5591, 26% win) | -5.0% (4898, 27% win) | -6.7% (4303, 28% win) | -8.0% (3720, 29% win) |
| schoon | -7.0% (6270, 28% win) | -7.5% (6137, 27% win) | -7.0% (6027, 26% win) | -7.0% (5913, 26% win) | -7.2% (5783, 26% win) | -6.9% (5521, 26% win) | -6.6% (5025, 25% win) | -5.8% (4471, 27% win) | -4.4% (3927, 29% win) | -6.3% (3448, 30% win) | -7.9% (3030, 31% win) |
| bundelgrafiek | -3.8% (1499, 30% win) | -5.9% (1456, 28% win) | -7.4% (1412, 24% win) | -7.7% (1379, 22% win) | -8.3% (1362, 20% win) | -7.7% (1320, 19% win) | -8.1% (1247, 18% win) | -6.6% (1120, 19% win) | -7.7% (971, 19% win) | -8.5% (855, 20% win) | -8.6% (690, 21% win) |
| schoon+houders_ok | -6.9% (234, 25% win) | -8.6% (279, 23% win) | -8.4% (344, 24% win) | -7.8% (382, 22% win) | -9.5% (424, 19% win) | -9.6% (479, 20% win) | -9.2% (522, 18% win) | -7.1% (482, 22% win) | -7.2% (426, 22% win) | -7.2% (353, 23% win) | -8.2% (275, 23% win) |
| schoon+houders_ok+final_stretch | -4.6% (119, 29% win) | -9.4% (145, 22% win) | -8.6% (186, 25% win) | -8.5% (211, 23% win) | -9.8% (244, 20% win) | -10.1% (276, 20% win) | -10.7% (293, 16% win) | -10.1% (240, 19% win) | -8.3% (209, 21% win) | -8.9% (159, 22% win) | -8.9% (111, 21% win) |
| volledige_screening+schoon | -5.1% (98, 28% win) | -9.1% (117, 19% win) | -9.7% (142, 23% win) | -11.6% (159, 21% win) | -12.4% (181, 17% win) | -11.3% (193, 18% win) | -10.4% (194, 16% win) | -10.2% (150, 19% win) | -9.1% (121, 21% win) | -10.3% (103, 19% win) | -7.8% (69, 20% win) |
| volledige_screening+schoon+x_link | -6.0% (73, 26% win) | -8.4% (83, 18% win) | -10.7% (93, 19% win) | -10.5% (98, 21% win) | -10.9% (108, 20% win) | -10.8% (114, 20% win) | -9.9% (118, 20% win) | -10.0% (104, 18% win) | -10.4% (85, 19% win) | -11.5% (73, 18% win) | -6.3% (50, 18% win) |


## Verkennend: winstgrens tegen dipdiepte

Elke winstgrens bij elke instapdiepte, filter `schoon+houders_ok`, stop als in de video. Dit is het raster waar 8 grenzen x 11 dieptes = 88 cellen uit komen. Bij zoveel cellen zit er door toeval altijd een goede tussen, dus **hier telt geen enkele cel als bewijs** — het is bedoeld om te zien of er ergens een gebied is dat consequent beter is, niet om de beste cel te kiezen.

| winstgrens | d30 | d35 | d40 | d45 | d50 | d55 | d60 | d65 | d70 | d75 | d80 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +10% | -8.1% (234) | -8.6% (279) | -8.8% (344) | -7.6% (382) | -7.8% (424) | -7.5% (479) | -6.0% (522) | -6.5% (482) | -6.8% (426) | -5.8% (353) | -6.3% (275) |
| +15% | -8.4% (234) | -8.8% (279) | -8.4% (344) | -7.5% (382) | -7.9% (424) | -7.4% (479) | -6.0% (522) | -7.0% (482) | -6.9% (426) | -5.8% (353) | -6.1% (275) |
| +20% | -8.2% (234) | -8.8% (279) | -8.3% (344) | -7.7% (382) | -8.0% (424) | -7.5% (479) | -6.5% (522) | -7.5% (482) | -6.9% (426) | -5.9% (353) | -6.0% (275) |
| +25% | -7.5% (234) | -8.3% (279) | -8.4% (344) | -7.5% (382) | -8.0% (424) | -7.4% (479) | -6.5% (522) | -7.6% (482) | -6.8% (426) | -5.9% (353) | -6.4% (275) |
| +30% | -6.8% (234) | -8.1% (279) | -8.2% (344) | -7.6% (382) | -8.5% (424) | -7.4% (479) | -6.6% (522) | -7.4% (482) | -7.1% (426) | -6.5% (353) | -6.3% (275) |
| +35% | -7.3% (234) | -9.1% (279) | -8.1% (344) | -7.5% (382) | -8.6% (424) | -7.5% (479) | -6.8% (522) | -7.0% (482) | -6.6% (426) | -6.0% (353) | -6.3% (275) |
| +45% | -7.6% (234) | -9.3% (279) | -8.6% (344) | -8.1% (382) | -8.6% (424) | -8.2% (479) | -6.9% (522) | -7.2% (482) | -6.0% (426) | -5.6% (353) | -5.9% (275) |
| +60% | -8.1% (234) | -9.5% (279) | -8.4% (344) | -7.9% (382) | -8.2% (424) | -8.8% (479) | -7.0% (522) | -6.5% (482) | -5.9% (426) | -5.9% (353) | -6.1% (275) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 159 instappen, mediane hoogste stijging +9.0%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 49% | 26% | -7.5% | 24% |
| +15% | 46% | 23% | -7.2% | 23% |
| +20% | 40% | 20% | -7.3% | 20% |
| +25% | 35% | 17% | -7.5% | 18% |
| +30% | 32% | 14% | -7.5% | 16% |
| +35% | 30% | 14% | -7.1% | 15% |
| +45% | 21% | 9% | -8.5% | 11% |
| +60% | 16% | 6% | -8.7% | 8% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 382 instappen, mediane hoogste stijging +9.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 50% | 25% | -7.6% | 25% |
| +15% | 47% | 20% | -7.5% | 22% |
| +20% | 42% | 18% | -7.7% | 20% |
| +25% | 39% | 16% | -7.5% | 19% |
| +30% | 36% | 14% | -7.6% | 17% |
| +35% | 34% | 13% | -7.5% | 16% |
| +45% | 28% | 9% | -8.1% | 13% |
| +60% | 24% | 8% | -7.9% | 11% |

**filter `alle`** — variant `d45_direct`, 7292 instappen, mediane hoogste stijging +20.0%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.7% | 29% |
| +15% | 54% | 28% | -5.6% | 28% |
| +20% | 50% | 25% | -5.7% | 27% |
| +25% | 47% | 22% | -5.8% | 26% |
| +30% | 44% | 20% | -5.9% | 25% |
| +35% | 42% | 18% | -6.0% | 24% |
| +45% | 38% | 15% | -6.1% | 22% |
| +60% | 33% | 12% | -6.2% | 21% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -7.3% (98, 18% win) | -6.7% (98, 18% win) | -5.0% (98, 18% win) | -4.2% (98, 18% win) | -7.2% (98, 18% win) | -6.6% (98, 18% win) |
| d35_direct | -13.1% (117, 10% win) | -12.5% (117, 10% win) | -10.7% (117, 10% win) | -10.1% (117, 10% win) | -12.9% (117, 10% win) | -12.2% (117, 10% win) |
| d40_direct | -12.7% (142, 8% win) | -12.0% (142, 9% win) | -10.3% (142, 10% win) | -9.7% (142, 10% win) | -12.6% (142, 8% win) | -12.0% (142, 9% win) |
| d45_direct | -11.5% (159, 9% win) | -10.8% (159, 10% win) | -9.1% (159, 10% win) | -8.5% (159, 11% win) | -11.6% (159, 9% win) | -11.0% (159, 10% win) |
| d50_direct | -12.9% (181, 7% win) | -12.2% (181, 7% win) | -10.5% (181, 7% win) | -9.9% (181, 7% win) | -13.2% (181, 7% win) | -12.6% (181, 7% win) |
| d55_direct | -12.5% (193, 7% win) | -11.8% (193, 7% win) | -10.2% (193, 7% win) | -9.5% (193, 7% win) | -13.0% (193, 7% win) | -12.4% (193, 7% win) |
| d60_direct | -11.2% (194, 6% win) | -10.5% (194, 6% win) | -8.9% (194, 6% win) | -8.2% (194, 6% win) | -11.9% (194, 6% win) | -11.3% (194, 6% win) |
| d65_direct | -11.5% (150, 6% win) | -10.8% (150, 6% win) | -9.2% (150, 6% win) | -8.6% (150, 6% win) | -12.2% (150, 5% win) | -11.6% (150, 6% win) |
| d70_direct | -9.3% (121, 7% win) | -8.7% (121, 7% win) | -7.1% (121, 8% win) | -6.4% (121, 8% win) | -10.2% (121, 7% win) | -9.5% (121, 7% win) |
| d75_direct | -9.2% (103, 7% win) | -8.6% (103, 7% win) | -7.0% (103, 7% win) | -6.3% (103, 7% win) | -10.2% (103, 7% win) | -9.5% (103, 7% win) |
| d80_direct | -8.5% (69, 6% win) | -7.8% (69, 6% win) | -6.3% (69, 6% win) | -5.6% (69, 7% win) | -9.6% (69, 6% win) | -9.0% (69, 6% win) |
| d45_herstel5 | -10.1% (113, 12% win) | -9.4% (113, 12% win) | -7.7% (113, 12% win) | -7.0% (113, 12% win) | -10.0% (113, 12% win) | -9.4% (113, 12% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.7% (234, 15% win) | -10.0% (234, 15% win) | -8.3% (234, 16% win) | -7.6% (234, 16% win) | -10.5% (234, 15% win) | -9.8% (234, 16% win) |
| d35_direct | -12.4% (279, 13% win) | -11.7% (279, 13% win) | -10.0% (279, 13% win) | -9.3% (279, 13% win) | -12.2% (279, 13% win) | -11.6% (279, 13% win) |
| d40_direct | -11.7% (344, 12% win) | -11.0% (344, 13% win) | -9.3% (344, 13% win) | -8.6% (344, 13% win) | -11.6% (344, 12% win) | -11.0% (344, 13% win) |
| d45_direct | -11.2% (382, 11% win) | -10.5% (382, 12% win) | -8.8% (382, 12% win) | -8.1% (382, 13% win) | -11.3% (382, 11% win) | -10.7% (382, 12% win) |
| d50_direct | -11.5% (424, 10% win) | -10.9% (424, 10% win) | -9.2% (424, 11% win) | -8.6% (424, 11% win) | -11.8% (424, 10% win) | -11.2% (424, 10% win) |
| d55_direct | -11.2% (479, 10% win) | -10.5% (479, 10% win) | -8.9% (479, 11% win) | -8.2% (479, 11% win) | -11.7% (479, 10% win) | -11.0% (479, 10% win) |
| d60_direct | -9.8% (522, 9% win) | -9.2% (522, 9% win) | -7.6% (522, 10% win) | -6.9% (522, 10% win) | -10.5% (522, 9% win) | -9.9% (522, 9% win) |
| d65_direct | -10.1% (482, 10% win) | -9.4% (482, 10% win) | -7.9% (482, 10% win) | -7.2% (482, 10% win) | -10.8% (482, 9% win) | -10.2% (482, 10% win) |
| d70_direct | -8.9% (426, 11% win) | -8.2% (426, 11% win) | -6.7% (426, 12% win) | -6.0% (426, 12% win) | -9.8% (426, 11% win) | -9.2% (426, 11% win) |
| d75_direct | -8.5% (353, 11% win) | -7.8% (353, 11% win) | -6.3% (353, 12% win) | -5.6% (353, 12% win) | -9.5% (353, 11% win) | -8.9% (353, 11% win) |
| d80_direct | -8.6% (275, 11% win) | -8.0% (275, 12% win) | -6.5% (275, 12% win) | -5.9% (275, 12% win) | -10.2% (275, 12% win) | -9.5% (275, 12% win) |
| d45_herstel5 | -7.7% (274, 18% win) | -7.0% (274, 18% win) | -5.3% (274, 19% win) | -4.7% (274, 19% win) | -7.7% (274, 18% win) | -7.0% (274, 18% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -8.6% (7769, 24% win) | -7.9% (7769, 24% win) | -6.3% (7769, 25% win) | -5.6% (7769, 26% win) | -8.9% (7769, 23% win) | -8.3% (7769, 24% win) |
| d35_direct | -9.3% (7593, 22% win) | -8.6% (7593, 23% win) | -7.0% (7593, 24% win) | -6.3% (7593, 24% win) | -9.8% (7593, 22% win) | -9.1% (7593, 22% win) |
| d40_direct | -9.5% (7439, 21% win) | -8.8% (7439, 22% win) | -7.2% (7439, 22% win) | -6.5% (7439, 23% win) | -10.1% (7439, 21% win) | -9.5% (7439, 21% win) |
| d45_direct | -9.0% (7292, 21% win) | -8.3% (7292, 21% win) | -6.8% (7292, 22% win) | -6.1% (7292, 22% win) | -9.9% (7292, 20% win) | -9.3% (7292, 21% win) |
| d50_direct | -9.1% (7145, 20% win) | -8.4% (7145, 21% win) | -6.9% (7145, 21% win) | -6.2% (7145, 22% win) | -10.2% (7145, 20% win) | -9.6% (7145, 20% win) |
| d55_direct | -9.2% (6841, 20% win) | -8.6% (6841, 20% win) | -7.1% (6841, 21% win) | -6.5% (6841, 21% win) | -10.7% (6841, 19% win) | -10.0% (6841, 19% win) |
| d60_direct | -9.1% (6272, 20% win) | -8.4% (6272, 20% win) | -7.0% (6272, 21% win) | -6.4% (6272, 21% win) | -10.9% (6272, 18% win) | -10.3% (6272, 19% win) |
| d65_direct | -8.1% (5591, 21% win) | -7.4% (5591, 22% win) | -6.2% (5591, 22% win) | -5.5% (5591, 23% win) | -10.5% (5591, 20% win) | -9.8% (5591, 20% win) |
| d70_direct | -8.3% (4898, 22% win) | -7.6% (4898, 22% win) | -6.5% (4898, 23% win) | -5.8% (4898, 23% win) | -11.3% (4898, 20% win) | -10.7% (4898, 20% win) |
| d75_direct | -8.6% (4303, 23% win) | -7.9% (4303, 23% win) | -7.0% (4303, 24% win) | -6.3% (4303, 24% win) | -12.6% (4303, 21% win) | -11.9% (4303, 21% win) |
| d80_direct | -8.2% (3720, 26% win) | -7.5% (3720, 26% win) | -6.9% (3720, 27% win) | -6.2% (3720, 27% win) | -13.8% (3720, 23% win) | -13.2% (3720, 23% win) |
| d45_herstel5 | -8.9% (5838, 24% win) | -8.2% (5838, 25% win) | -6.7% (5838, 26% win) | -6.0% (5838, 26% win) | -9.9% (5838, 24% win) | -9.3% (5838, 24% win) |


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
| alle | -6.1% (7292, 22% win) | -5.9% (7292, 22% win) | -7.5% (7292, 21% win) | -5.9% (7292, 25% win) |
| schoon | -6.3% (5913, 23% win) | -6.1% (5913, 22% win) | -7.3% (5913, 22% win) | -6.0% (5913, 26% win) |
| bundelgrafiek | -5.4% (1379, 20% win) | -5.4% (1379, 20% win) | -8.7% (1379, 18% win) | -5.4% (1379, 22% win) |
| schoon+houders_ok | -8.1% (382, 13% win) | -7.7% (382, 10% win) | -10.7% (382, 14% win) | -7.8% (382, 19% win) |
| schoon+houders_ok+final_stretch | -6.8% (211, 13% win) | -6.9% (211, 10% win) | -12.0% (211, 14% win) | -6.9% (211, 20% win) |
| volledige_screening+schoon | -8.5% (159, 11% win) | -8.9% (159, 6% win) | -15.4% (159, 11% win) | -7.7% (159, 19% win) |
| volledige_screening+schoon+x_link | -8.5% (98, 11% win) | -9.0% (98, 7% win) | -14.9% (98, 9% win) | -8.2% (98, 18% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.6% (2940, 28% win); 1,3–2x: -6.9% (2972, 18% win); ≥ 2x (bundelgrafiek): -5.5% (1380, 20% win)

**aandeel supply gekocht in creatieblok:** < 5%: -4.7% (4220, 30% win); 5–20%: -8.1% (1222, 13% win); ≥ 20%: -8.1% (1850, 12% win)

**top t.o.v. start:** 2–3x: -5.8% (4155, 21% win); 3–6x: -6.8% (2420, 24% win); ≥ 6x: -5.7% (717, 25% win)

**unieke kopers tot de top:** < 30: -5.1% (4314, 29% win); 30–100: -6.9% (1671, 13% win); ≥ 100: -8.8% (1307, 14% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.0% (1865, 16% win); 1–2: -6.5% (3495, 24% win); ≥ 3 (trap): -5.5% (1932, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -7.8% (1962, 14% win); 10–25%: -8.7% (1356, 11% win); ≥ 25%: -4.4% (3974, 30% win)

**duur van top naar dip:** < 30 s (crash): -5.8% (5606, 25% win); 30 s–3 min: -7.1% (1335, 13% win); ≥ 3 min (langzaam): -8.4% (351, 10% win)

**tijd van start tot top:** < 2 min: -5.8% (5876, 24% win); 2–10 min: -8.3% (1142, 14% win); ≥ 10 min: -5.6% (274, 13% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
