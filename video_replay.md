# Videostrategie op alle trades — 2026-09-15 09:38 UTC

Tokens sinds 2026-09-11 08:47 UTC: 91247 geschikt (≥ 2 uur oud, geen herstart), 70718 met trades, 12759 haalden 2x de startkoers, 9746 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 2978 tokens. Houdercheck echt uitgevoerd bij 93% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1630, winkans 19%, EV per trade -7.2% (95%-marge -8.7% tot -5.7%), mediaan -10.4%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 7373, winkans 22%, EV -7.1% (95%-marge -8.3% tot -5.8%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 198, winkans 18%, EV -9.9% (95%-marge -13.0% tot -6.8%).
- **H4** (2026-09-14 22:00 UTC): instap na een dip van 65% vanaf de top; stop op 75% onder de top zolang de winst onder +15% blijft; vanaf +15% een meelopende stop op 10% onder de hoogste koers; schone grafiek en houdercheck in orde. Aanleiding: voorstel van Gerben, 14 sept. Combineert de twee hefbomen die los gemeten het minst slecht waren: dieper instappen (d65-d70 gaf -3,8% tot -4,7% tegen -6,9% bij d45) en eerder winst vastleggen (+10% gaf -5,4% tegen -6,9% bij +45%), maar dan met een meelopende stop zodat een uitschieter niet wordt afgekapt. Filter is 'schoon+houders_ok' en niet de volledige screening, omdat die screening in drie onafhankelijke metingen averechts werkt. Verwachting vooraf, zodat die toetsbaar is: rond -3%, dus nog steeds negatief.. Resultaat: nog geen trades.

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 9746 | 39% | 77% | 35% |
| schoon | 7862 | 41% | 77% | 38% |
| bundelgrafiek | 1884 | 32% | 77% | 25% |
| schoon+houders_ok | 1630 | 35% | 80% | 22% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.1% (10404, 25% win) | -6.6% (10180, 24% win) | -7.0% (9957, 23% win) | -6.6% (9746, 22% win) | -6.9% (9542, 22% win) | -7.0% (9164, 21% win) | -6.6% (8475, 21% win) | -6.3% (7541, 23% win) | -5.8% (6640, 24% win) | -6.6% (5838, 25% win) | -6.7% (5065, 28% win) | -6.4% (7932, 26% win) |
| schoon | -6.4% (8379, 25% win) | -6.6% (8214, 24% win) | -6.9% (8038, 23% win) | -6.5% (7862, 23% win) | -6.6% (7693, 23% win) | -6.9% (7367, 22% win) | -6.4% (6759, 23% win) | -6.1% (6001, 24% win) | -5.4% (5321, 26% win) | -6.1% (4693, 26% win) | -6.3% (4138, 29% win) | -6.3% (6626, 26% win) |
| bundelgrafiek | -4.9% (2025, 25% win) | -6.5% (1966, 23% win) | -7.3% (1919, 20% win) | -7.0% (1884, 18% win) | -8.1% (1849, 16% win) | -7.6% (1797, 16% win) | -7.4% (1716, 16% win) | -7.2% (1540, 16% win) | -7.4% (1319, 18% win) | -8.7% (1145, 18% win) | -8.2% (927, 21% win) | -6.5% (1306, 24% win) |
| schoon+houders_ok | -6.7% (1234, 20% win) | -7.2% (1372, 19% win) | -7.4% (1524, 19% win) | -7.2% (1630, 19% win) | -7.2% (1755, 18% win) | -6.2% (1882, 18% win) | -5.5% (1951, 18% win) | -5.1% (1772, 20% win) | -4.5% (1600, 22% win) | -5.1% (1393, 23% win) | -5.5% (1205, 25% win) | -4.1% (1313, 23% win) |
| schoon+houders_ok+final_stretch | -7.3% (534, 16% win) | -7.6% (597, 14% win) | -8.0% (665, 13% win) | -8.2% (712, 12% win) | -8.6% (765, 10% win) | -7.7% (816, 10% win) | -7.2% (817, 9% win) | -6.9% (640, 9% win) | -6.9% (505, 10% win) | -7.0% (355, 8% win) | -5.6% (231, 10% win) | -5.5% (541, 16% win) |
| volledige_screening+schoon | -6.9% (382, 16% win) | -7.4% (412, 15% win) | -8.9% (439, 12% win) | -9.4% (467, 11% win) | -9.8% (494, 9% win) | -8.9% (507, 8% win) | -7.5% (497, 8% win) | -7.7% (386, 8% win) | -8.0% (295, 6% win) | -7.7% (220, 7% win) | -7.4% (142, 6% win) | -7.2% (339, 13% win) |
| volledige_screening+schoon+x_link | -7.2% (295, 17% win) | -6.6% (314, 18% win) | -9.0% (323, 13% win) | -9.6% (332, 11% win) | -9.9% (340, 9% win) | -9.4% (346, 8% win) | -8.5% (343, 7% win) | -8.7% (279, 6% win) | -8.1% (215, 6% win) | -7.8% (163, 7% win) | -7.8% (107, 3% win) | -7.7% (234, 12% win) |

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
| alle | -6.3% (10404, 30% win) | -6.9% (10180, 28% win) | -7.0% (9957, 27% win) | -6.7% (9746, 27% win) | -7.2% (9542, 26% win) | -7.2% (9164, 26% win) | -7.1% (8475, 26% win) | -6.8% (7541, 28% win) | -6.5% (6640, 30% win) | -7.2% (5838, 31% win) | -7.4% (5065, 33% win) |
| schoon | -6.5% (8379, 30% win) | -6.9% (8214, 29% win) | -6.9% (8038, 28% win) | -6.6% (7862, 28% win) | -7.2% (7693, 27% win) | -7.1% (7367, 27% win) | -7.1% (6759, 28% win) | -6.5% (6001, 30% win) | -6.1% (5321, 32% win) | -6.8% (4693, 33% win) | -7.0% (4138, 35% win) |
| bundelgrafiek | -5.7% (2025, 29% win) | -7.0% (1966, 26% win) | -7.4% (1919, 23% win) | -6.9% (1884, 22% win) | -7.4% (1849, 21% win) | -7.2% (1797, 20% win) | -6.9% (1716, 19% win) | -7.5% (1540, 19% win) | -8.2% (1319, 21% win) | -9.1% (1145, 22% win) | -9.1% (927, 26% win) |
| schoon+houders_ok | -6.6% (1234, 27% win) | -6.8% (1372, 27% win) | -6.9% (1524, 26% win) | -7.2% (1630, 27% win) | -7.6% (1755, 25% win) | -6.3% (1882, 26% win) | -5.8% (1951, 25% win) | -5.7% (1772, 28% win) | -4.9% (1600, 31% win) | -5.3% (1393, 32% win) | -6.9% (1205, 32% win) |
| schoon+houders_ok+final_stretch | -7.0% (534, 25% win) | -7.7% (597, 23% win) | -7.7% (665, 23% win) | -9.4% (712, 21% win) | -10.5% (765, 17% win) | -9.1% (816, 18% win) | -7.6% (817, 19% win) | -8.4% (640, 20% win) | -8.0% (505, 23% win) | -7.5% (355, 24% win) | -7.0% (231, 24% win) |
| volledige_screening+schoon | -7.1% (382, 25% win) | -7.7% (412, 23% win) | -8.6% (439, 23% win) | -10.8% (467, 20% win) | -11.8% (494, 16% win) | -10.4% (507, 17% win) | -8.3% (497, 17% win) | -9.1% (386, 18% win) | -10.3% (295, 18% win) | -9.4% (220, 19% win) | -9.3% (142, 18% win) |
| volledige_screening+schoon+x_link | -7.2% (295, 25% win) | -7.0% (314, 24% win) | -8.8% (323, 23% win) | -11.2% (332, 19% win) | -12.0% (340, 15% win) | -10.0% (346, 17% win) | -8.1% (343, 18% win) | -9.0% (279, 17% win) | -9.4% (215, 18% win) | -8.9% (163, 19% win) | -9.3% (107, 16% win) |


## Regel H4: dip 65%, trailing stop vanaf +15% op 10% onder de piek

Tot +15% ligt de stop op hetzelfde niveau als bij de vorige regel — 10%-punt dieper dan de instap — zodat de positie eerst nog kan zakken. Vanaf +15% loopt de stop mee op 10% onder de hoogste koers, en ligt daarmee altijd boven de instapprijs. Geen vaste winstgrens: een uitschieter wordt niet afgekapt.

**Vooraf vastgelegd als H4 op d65 met filter schoon+houders_ok; de rest van deze regel is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.4% (10404, 28% win) | -7.0% (10180, 27% win) | -7.1% (9957, 26% win) | -7.1% (9746, 26% win) | -7.7% (9542, 24% win) | -7.4% (9164, 24% win) | -7.1% (8475, 24% win) | -6.5% (7541, 26% win) | -5.9% (6640, 28% win) | -7.1% (5838, 28% win) | -8.0% (5065, 29% win) |
| schoon | -6.7% (8379, 29% win) | -6.9% (8214, 28% win) | -7.0% (8038, 27% win) | -6.9% (7862, 27% win) | -7.5% (7693, 26% win) | -7.4% (7367, 25% win) | -6.8% (6759, 26% win) | -6.0% (6001, 28% win) | -4.9% (5321, 30% win) | -6.4% (4693, 30% win) | -7.8% (4138, 31% win) |
| bundelgrafiek | -5.3% (2025, 28% win) | -7.3% (1966, 25% win) | -7.7% (1919, 22% win) | -8.0% (1884, 20% win) | -8.3% (1849, 20% win) | -7.5% (1797, 19% win) | -8.4% (1716, 17% win) | -8.3% (1540, 18% win) | -9.6% (1319, 19% win) | -10.1% (1145, 20% win) | -8.9% (927, 22% win) |
| schoon+houders_ok | -5.6% (1234, 27% win) | -6.0% (1372, 27% win) | -7.1% (1524, 26% win) | -7.6% (1630, 26% win) | -7.1% (1755, 24% win) | -6.3% (1882, 25% win) | -5.8% (1951, 25% win) | -5.1% (1772, 26% win) | -3.7% (1600, 28% win) | -4.6% (1393, 29% win) | -6.3% (1205, 29% win) |
| schoon+houders_ok+final_stretch | -5.9% (534, 27% win) | -7.0% (597, 26% win) | -7.2% (665, 25% win) | -8.6% (712, 23% win) | -9.8% (765, 18% win) | -9.0% (816, 20% win) | -7.7% (817, 20% win) | -7.2% (640, 22% win) | -8.5% (505, 22% win) | -8.5% (355, 23% win) | -8.0% (231, 23% win) |
| volledige_screening+schoon | -5.9% (382, 26% win) | -6.6% (412, 25% win) | -8.4% (439, 24% win) | -10.8% (467, 21% win) | -11.5% (494, 17% win) | -10.0% (507, 19% win) | -7.8% (497, 19% win) | -8.3% (386, 19% win) | -10.6% (295, 18% win) | -10.4% (220, 18% win) | -10.1% (142, 17% win) |
| volledige_screening+schoon+x_link | -7.0% (295, 25% win) | -5.6% (314, 26% win) | -8.3% (323, 22% win) | -10.6% (332, 20% win) | -11.6% (340, 16% win) | -10.1% (346, 17% win) | -8.6% (343, 19% win) | -8.8% (279, 18% win) | -10.4% (215, 17% win) | -11.3% (163, 17% win) | -9.9% (107, 13% win) |


## Verkennend: winstgrens tegen dipdiepte

Elke winstgrens bij elke instapdiepte, filter `schoon+houders_ok`, stop als in de video. Dit is het raster waar 8 grenzen x 11 dieptes = 88 cellen uit komen. Bij zoveel cellen zit er door toeval altijd een goede tussen, dus **hier telt geen enkele cel als bewijs** — het is bedoeld om te zien of er ergens een gebied is dat consequent beter is, niet om de beste cel te kiezen.

| winstgrens | d30 | d35 | d40 | d45 | d50 | d55 | d60 | d65 | d70 | d75 | d80 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +10% | -7.1% (1234) | -6.3% (1372) | -6.3% (1524) | -5.9% (1630) | -6.0% (1755) | -5.9% (1882) | -5.2% (1951) | -5.0% (1772) | -5.6% (1600) | -5.2% (1393) | -6.0% (1205) |
| +15% | -7.1% (1234) | -6.5% (1372) | -6.3% (1524) | -6.0% (1630) | -6.1% (1755) | -5.9% (1882) | -5.3% (1951) | -5.2% (1772) | -5.6% (1600) | -5.4% (1393) | -5.8% (1205) |
| +20% | -7.1% (1234) | -6.6% (1372) | -6.3% (1524) | -6.1% (1630) | -6.5% (1755) | -6.0% (1882) | -5.3% (1951) | -5.5% (1772) | -5.5% (1600) | -5.3% (1393) | -5.8% (1205) |
| +25% | -6.8% (1234) | -6.4% (1372) | -6.5% (1524) | -6.3% (1630) | -6.6% (1755) | -6.1% (1882) | -5.5% (1951) | -5.7% (1772) | -5.5% (1600) | -5.3% (1393) | -5.7% (1205) |
| +30% | -6.7% (1234) | -6.6% (1372) | -6.5% (1524) | -6.4% (1630) | -7.0% (1755) | -6.0% (1882) | -5.5% (1951) | -5.5% (1772) | -5.4% (1600) | -5.5% (1393) | -6.2% (1205) |
| +35% | -6.9% (1234) | -7.1% (1372) | -6.6% (1524) | -6.5% (1630) | -7.0% (1755) | -5.9% (1882) | -5.5% (1951) | -5.4% (1772) | -5.1% (1600) | -5.4% (1393) | -5.9% (1205) |
| +45% | -6.7% (1234) | -7.2% (1372) | -7.4% (1524) | -7.2% (1630) | -7.2% (1755) | -6.2% (1882) | -5.5% (1951) | -5.1% (1772) | -4.5% (1600) | -5.1% (1393) | -5.5% (1205) |
| +60% | -6.3% (1234) | -6.8% (1372) | -7.1% (1524) | -7.0% (1630) | -7.0% (1755) | -6.2% (1882) | -5.5% (1951) | -4.8% (1772) | -4.4% (1600) | -4.6% (1393) | -5.1% (1205) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 467 instappen, mediane hoogste stijging +8.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 48% | 24% | -8.0% | 25% |
| +15% | 43% | 20% | -8.1% | 21% |
| +20% | 39% | 17% | -8.1% | 19% |
| +25% | 34% | 15% | -8.4% | 16% |
| +30% | 31% | 13% | -8.5% | 15% |
| +35% | 29% | 12% | -8.4% | 14% |
| +45% | 23% | 8% | -9.4% | 11% |
| +60% | 19% | 7% | -9.3% | 9% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1630 instappen, mediane hoogste stijging +18.8%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 57% | 32% | -5.9% | 30% |
| +15% | 52% | 26% | -6.0% | 27% |
| +20% | 49% | 23% | -6.1% | 24% |
| +25% | 46% | 20% | -6.3% | 23% |
| +30% | 43% | 18% | -6.4% | 22% |
| +35% | 40% | 16% | -6.5% | 21% |
| +45% | 35% | 13% | -7.2% | 19% |
| +60% | 31% | 10% | -7.0% | 17% |

**filter `alle`** — variant `d45_direct`, 9746 instappen, mediane hoogste stijging +21.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 58% | 33% | -6.0% | 29% |
| +15% | 54% | 29% | -6.1% | 28% |
| +20% | 51% | 26% | -6.2% | 27% |
| +25% | 48% | 23% | -6.3% | 26% |
| +30% | 45% | 20% | -6.4% | 25% |
| +35% | 43% | 18% | -6.5% | 24% |
| +45% | 38% | 15% | -6.6% | 22% |
| +60% | 34% | 12% | -6.6% | 21% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.9% (382, 15% win) | -9.2% (382, 15% win) | -7.5% (382, 16% win) | -6.9% (382, 16% win) | -9.9% (382, 15% win) | -9.3% (382, 15% win) |
| d35_direct | -10.5% (412, 14% win) | -9.8% (412, 14% win) | -8.1% (412, 15% win) | -7.4% (412, 15% win) | -10.5% (412, 14% win) | -9.8% (412, 14% win) |
| d40_direct | -11.9% (439, 12% win) | -11.2% (439, 12% win) | -9.5% (439, 12% win) | -8.9% (439, 12% win) | -11.9% (439, 11% win) | -11.3% (439, 12% win) |
| d45_direct | -12.4% (467, 10% win) | -11.7% (467, 10% win) | -10.0% (467, 11% win) | -9.4% (467, 11% win) | -12.5% (467, 10% win) | -11.9% (467, 10% win) |
| d50_direct | -12.7% (494, 8% win) | -12.1% (494, 8% win) | -10.4% (494, 8% win) | -9.8% (494, 9% win) | -13.1% (494, 8% win) | -12.5% (494, 8% win) |
| d55_direct | -11.8% (507, 8% win) | -11.2% (507, 8% win) | -9.5% (507, 8% win) | -8.9% (507, 8% win) | -12.4% (507, 7% win) | -11.8% (507, 8% win) |
| d60_direct | -10.3% (497, 8% win) | -9.7% (497, 8% win) | -8.1% (497, 8% win) | -7.5% (497, 8% win) | -11.2% (497, 7% win) | -10.6% (497, 7% win) |
| d65_direct | -10.6% (386, 8% win) | -9.9% (386, 8% win) | -8.4% (386, 8% win) | -7.7% (386, 8% win) | -11.5% (386, 7% win) | -10.9% (386, 8% win) |
| d70_direct | -10.8% (295, 6% win) | -10.2% (295, 6% win) | -8.6% (295, 6% win) | -8.0% (295, 6% win) | -11.8% (295, 5% win) | -11.2% (295, 6% win) |
| d75_direct | -10.5% (220, 6% win) | -9.8% (220, 6% win) | -8.3% (220, 7% win) | -7.7% (220, 7% win) | -11.6% (220, 6% win) | -11.0% (220, 6% win) |
| d80_direct | -10.2% (142, 5% win) | -9.5% (142, 5% win) | -8.1% (142, 5% win) | -7.4% (142, 6% win) | -11.7% (142, 4% win) | -11.1% (142, 4% win) |
| d45_herstel5 | -10.3% (339, 13% win) | -9.6% (339, 13% win) | -7.9% (339, 13% win) | -7.2% (339, 13% win) | -10.3% (339, 13% win) | -9.7% (339, 13% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.8% (1234, 19% win) | -9.2% (1234, 19% win) | -7.4% (1234, 20% win) | -6.7% (1234, 20% win) | -9.5% (1234, 19% win) | -8.8% (1234, 19% win) |
| d35_direct | -10.3% (1372, 18% win) | -9.6% (1372, 18% win) | -7.8% (1372, 19% win) | -7.2% (1372, 19% win) | -10.1% (1372, 18% win) | -9.4% (1372, 19% win) |
| d40_direct | -10.5% (1524, 17% win) | -9.8% (1524, 18% win) | -8.1% (1524, 18% win) | -7.4% (1524, 19% win) | -10.4% (1524, 17% win) | -9.8% (1524, 18% win) |
| d45_direct | -10.2% (1630, 17% win) | -9.6% (1630, 17% win) | -7.9% (1630, 18% win) | -7.2% (1630, 19% win) | -10.3% (1630, 17% win) | -9.7% (1630, 17% win) |
| d50_direct | -10.2% (1755, 17% win) | -9.5% (1755, 17% win) | -7.8% (1755, 18% win) | -7.2% (1755, 18% win) | -10.4% (1755, 16% win) | -9.8% (1755, 17% win) |
| d55_direct | -9.1% (1882, 17% win) | -8.4% (1882, 17% win) | -6.8% (1882, 18% win) | -6.2% (1882, 18% win) | -9.7% (1882, 16% win) | -9.0% (1882, 17% win) |
| d60_direct | -8.4% (1951, 17% win) | -7.7% (1951, 17% win) | -6.2% (1951, 18% win) | -5.5% (1951, 18% win) | -9.2% (1951, 16% win) | -8.6% (1951, 17% win) |
| d65_direct | -8.0% (1772, 18% win) | -7.3% (1772, 18% win) | -5.8% (1772, 19% win) | -5.1% (1772, 20% win) | -9.1% (1772, 18% win) | -8.5% (1772, 18% win) |
| d70_direct | -7.3% (1600, 21% win) | -6.6% (1600, 21% win) | -5.2% (1600, 22% win) | -4.5% (1600, 22% win) | -8.9% (1600, 20% win) | -8.2% (1600, 20% win) |
| d75_direct | -7.8% (1393, 22% win) | -7.1% (1393, 22% win) | -5.8% (1393, 22% win) | -5.1% (1393, 23% win) | -10.0% (1393, 20% win) | -9.3% (1393, 20% win) |
| d80_direct | -7.9% (1205, 24% win) | -7.2% (1205, 24% win) | -6.2% (1205, 25% win) | -5.5% (1205, 25% win) | -11.4% (1205, 22% win) | -10.8% (1205, 22% win) |
| d45_herstel5 | -7.2% (1313, 22% win) | -6.5% (1313, 22% win) | -4.8% (1313, 23% win) | -4.1% (1313, 23% win) | -7.2% (1313, 22% win) | -6.6% (1313, 22% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.1% (10404, 24% win) | -8.4% (10404, 24% win) | -6.8% (10404, 25% win) | -6.1% (10404, 25% win) | -9.4% (10404, 23% win) | -8.7% (10404, 24% win) |
| d35_direct | -9.6% (10180, 22% win) | -8.9% (10180, 23% win) | -7.3% (10180, 24% win) | -6.6% (10180, 24% win) | -10.0% (10180, 22% win) | -9.3% (10180, 22% win) |
| d40_direct | -9.9% (9957, 21% win) | -9.2% (9957, 22% win) | -7.6% (9957, 22% win) | -7.0% (9957, 23% win) | -10.5% (9957, 21% win) | -9.9% (9957, 21% win) |
| d45_direct | -9.5% (9746, 21% win) | -8.8% (9746, 21% win) | -7.2% (9746, 22% win) | -6.6% (9746, 22% win) | -10.3% (9746, 20% win) | -9.7% (9746, 21% win) |
| d50_direct | -9.7% (9542, 20% win) | -9.0% (9542, 21% win) | -7.5% (9542, 21% win) | -6.9% (9542, 22% win) | -10.8% (9542, 20% win) | -10.2% (9542, 20% win) |
| d55_direct | -9.8% (9164, 19% win) | -9.1% (9164, 20% win) | -7.7% (9164, 21% win) | -7.0% (9164, 21% win) | -11.2% (9164, 18% win) | -10.5% (9164, 19% win) |
| d60_direct | -9.4% (8475, 20% win) | -8.7% (8475, 20% win) | -7.3% (8475, 21% win) | -6.6% (8475, 21% win) | -11.1% (8475, 19% win) | -10.5% (8475, 19% win) |
| d65_direct | -9.0% (7541, 21% win) | -8.3% (7541, 22% win) | -7.0% (7541, 22% win) | -6.3% (7541, 23% win) | -11.2% (7541, 20% win) | -10.6% (7541, 20% win) |
| d70_direct | -8.3% (6640, 23% win) | -7.6% (6640, 24% win) | -6.5% (6640, 24% win) | -5.8% (6640, 24% win) | -11.4% (6640, 21% win) | -10.7% (6640, 22% win) |
| d75_direct | -8.9% (5838, 24% win) | -8.2% (5838, 24% win) | -7.3% (5838, 24% win) | -6.6% (5838, 25% win) | -12.9% (5838, 21% win) | -12.3% (5838, 21% win) |
| d80_direct | -8.6% (5065, 26% win) | -7.9% (5065, 27% win) | -7.3% (5065, 27% win) | -6.7% (5065, 28% win) | -14.4% (5065, 23% win) | -13.8% (5065, 23% win) |
| d45_herstel5 | -9.2% (7932, 25% win) | -8.5% (7932, 25% win) | -7.0% (7932, 26% win) | -6.4% (7932, 26% win) | -10.3% (7932, 24% win) | -9.6% (7932, 24% win) |


## Wat kost de uitvoering echt?

Wij rekenen met 0.001 SOL vaste kosten per transactie. De video van 14 sept gebruikt een tip van 0,02 SOL plus 0,001 prioriteitsfee — twintig keer zoveel. Een vaste fee werkt lineair door: elke extra T SOL per kant verlaagt het rendement met 2T gedeeld door de inzet. Onderstaande EV's zijn daarmee exact doorgerekend, niet opnieuw gesimuleerd. Filter `schoon+houders_ok`, videoregel, PumpPortal.

| extra vaste fee per transactie | inzet 0.05 SOL | inzet 0.2 SOL | inzet 1.0 SOL |
|---|---|---|---|
| +0.0 SOL | -9.6% | -7.2% | -9.7% |
| +0.005 SOL | -29.6% | -12.2% | -10.7% |
| +0.01 SOL | -49.6% | -17.2% | -11.7% |
| +0.02 SOL | -89.6% | -27.2% | -13.7% |

Bij 0,05 SOL inzet eet een tip van 0,02 SOL per kant 84% van de positie op. Een strategie met een randje van een paar procent bestaat bij die instellingen simpelweg niet; bij 1 SOL kost hij 4,2%. Dit verandert onze conclusie niet — de EV was al negatief — maar het laat zien dat kleine inzetten bij deze uitvoering sowieso kansloos zijn, en dat onze eigen cijfers aan de gunstige kant staan.



## Uitstapregels vergeleken (dip 45%, direct)

'Gespreid' is vier gelijke plakjes op +10%, +20%, +30% en +45%, allemaal met dezelfde stop — het advies uit de KOL-video om niet in één keer te verkopen. Dat is rekenkundig het gewogen gemiddelde van de vier losse grenzen, dus het kan de verwachting niet redden; het verandert alleen de spreiding.

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) | gespreid |
|---|---|---|---|---|
| alle | -6.6% (9746, 22% win) | -6.3% (9746, 22% win) | -7.1% (9746, 21% win) | -6.3% (9746, 25% win) |
| schoon | -6.5% (7862, 23% win) | -6.3% (7862, 23% win) | -6.8% (7862, 22% win) | -6.2% (7862, 26% win) |
| bundelgrafiek | -7.0% (1884, 18% win) | -6.6% (1884, 18% win) | -8.4% (1884, 17% win) | -6.6% (1884, 21% win) |
| schoon+houders_ok | -7.2% (1630, 19% win) | -6.8% (1630, 18% win) | -7.2% (1630, 19% win) | -6.4% (1630, 24% win) |
| schoon+houders_ok+final_stretch | -8.2% (712, 12% win) | -7.3% (712, 10% win) | -10.2% (712, 14% win) | -7.3% (712, 18% win) |
| volledige_screening+schoon | -9.4% (467, 11% win) | -8.7% (467, 8% win) | -12.2% (467, 13% win) | -8.5% (467, 17% win) |
| volledige_screening+schoon+x_link | -9.6% (332, 11% win) | -8.9% (332, 8% win) | -12.2% (332, 12% win) | -9.0% (332, 17% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.5% (4076, 28% win); 1,3–2x: -7.5% (3785, 19% win); ≥ 2x (bundelgrafiek): -7.0% (1885, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.6% (5979, 29% win); 5–20%: -8.2% (1695, 13% win); ≥ 20%: -8.2% (2072, 12% win)

**top t.o.v. start:** 2–3x: -6.1% (5549, 21% win); 3–6x: -6.9% (3274, 24% win); ≥ 6x: -7.9% (923, 23% win)

**unieke kopers tot de top:** < 30: -5.8% (6016, 28% win); 30–100: -6.9% (2087, 12% win); ≥ 100: -9.1% (1643, 13% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -6.8% (2421, 16% win); 1–2: -6.5% (4718, 24% win); ≥ 3 (trap): -6.5% (2607, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.4% (2511, 13% win); 10–25%: -7.9% (1655, 12% win); ≥ 25%: -5.4% (5580, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (7599, 25% win); 30 s–3 min: -8.4% (1708, 14% win); ≥ 3 min (langzaam): -9.0% (439, 9% win)

**tijd van start tot top:** < 2 min: -6.2% (7954, 24% win); 2–10 min: -8.0% (1440, 15% win); ≥ 10 min: -10.2% (352, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
