# Videostrategie op alle trades — 2026-09-13 13:40 UTC

Tokens sinds 2026-09-11 08:47 UTC: 37883 geschikt (≥ 2 uur oud, geen herstart), 30181 met trades, 5711 haalden 2x de startkoers, 4335 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1336 tokens. Houdercheck echt uitgevoerd bij 89% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1280, winkans 20%, EV per trade -7.0% (95%-marge -8.8% tot -5.2%), mediaan -10.6%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2993, winkans 24%, EV -6.9% (95%-marge -8.8% tot -5.0%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: n = 18, winkans 11%, EV -11.0% (95%-marge -18.1% tot -4.0%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4335 | 40% | 76% | 37% |
| schoon | 3482 | 42% | 76% | 40% |
| bundelgrafiek | 853 | 29% | 78% | 25% |
| schoon+houders_ok | 1280 | 38% | 79% | 26% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d65_direct | d70_direct | d75_direct | d80_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alle | -6.3% (4641, 25% win) | -6.4% (4542, 24% win) | -6.7% (4442, 23% win) | -6.6% (4335, 23% win) | -7.1% (4238, 22% win) | -6.9% (4079, 21% win) | -6.4% (3786, 22% win) | -6.3% (3381, 24% win) | -5.6% (2994, 26% win) | -6.7% (2640, 25% win) | -7.0% (2299, 27% win) | -6.5% (3560, 26% win) |
| schoon | -6.1% (3731, 26% win) | -5.9% (3659, 26% win) | -6.3% (3576, 25% win) | -6.3% (3482, 24% win) | -6.6% (3408, 24% win) | -6.8% (3274, 23% win) | -6.0% (3010, 24% win) | -5.4% (2678, 26% win) | -5.0% (2398, 28% win) | -6.2% (2124, 27% win) | -6.6% (1877, 29% win) | -6.0% (2986, 27% win) |
| bundelgrafiek | -7.0% (910, 22% win) | -8.4% (883, 19% win) | -8.4% (866, 18% win) | -8.0% (853, 16% win) | -9.2% (830, 15% win) | -7.5% (805, 15% win) | -7.7% (776, 15% win) | -9.5% (703, 15% win) | -8.0% (596, 18% win) | -8.7% (516, 18% win) | -8.9% (422, 19% win) | -9.0% (574, 22% win) |
| schoon+houders_ok | -6.5% (1024, 21% win) | -6.7% (1119, 21% win) | -7.1% (1212, 20% win) | -7.0% (1280, 20% win) | -6.8% (1363, 20% win) | -5.5% (1440, 20% win) | -5.1% (1471, 21% win) | -4.5% (1333, 23% win) | -3.9% (1213, 25% win) | -5.1% (1065, 26% win) | -5.2% (947, 28% win) | -4.2% (1063, 24% win) |
| schoon+houders_ok+final_stretch | -7.6% (430, 16% win) | -7.1% (467, 15% win) | -8.0% (498, 13% win) | -9.0% (519, 12% win) | -8.8% (539, 10% win) | -7.7% (560, 10% win) | -6.9% (546, 10% win) | -6.1% (419, 11% win) | -7.5% (314, 9% win) | -7.6% (205, 9% win) | -5.4% (125, 12% win) | -6.1% (401, 15% win) |
| volledige_screening+schoon | -7.8% (296, 15% win) | -6.5% (307, 16% win) | -8.5% (312, 14% win) | -10.1% (321, 11% win) | -10.0% (326, 9% win) | -8.7% (327, 8% win) | -7.1% (314, 8% win) | -7.1% (245, 9% win) | -8.6% (184, 5% win) | -8.9% (123, 7% win) | -9.1% (76, 4% win) | -7.6% (235, 14% win) |
| volledige_screening+schoon+x_link | -8.4% (231, 16% win) | -5.4% (240, 19% win) | -8.8% (240, 15% win) | -10.3% (243, 11% win) | -10.2% (241, 9% win) | -9.5% (241, 8% win) | -8.6% (234, 7% win) | -8.6% (182, 6% win) | -8.7% (138, 4% win) | -8.7% (96, 6% win) | -8.7% (60, 2% win) | -8.1% (171, 13% win) |

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
| alle | -5.8% (4641, 30% win) | -5.8% (4542, 29% win) | -6.1% (4442, 28% win) | -6.4% (4335, 28% win) | -7.4% (4238, 26% win) | -6.8% (4079, 26% win) | -6.4% (3786, 27% win) | -6.6% (3381, 28% win) | -6.2% (2994, 31% win) | -6.6% (2640, 32% win) | -7.7% (2299, 33% win) |
| schoon | -5.7% (3731, 31% win) | -5.4% (3659, 30% win) | -5.8% (3576, 30% win) | -6.2% (3482, 29% win) | -7.3% (3408, 27% win) | -6.9% (3274, 27% win) | -6.2% (3010, 29% win) | -6.1% (2678, 31% win) | -5.7% (2398, 34% win) | -5.9% (2124, 34% win) | -7.0% (1877, 35% win) |
| bundelgrafiek | -6.5% (910, 26% win) | -7.6% (883, 24% win) | -7.0% (866, 22% win) | -7.2% (853, 21% win) | -7.7% (830, 20% win) | -6.5% (805, 20% win) | -7.0% (776, 18% win) | -8.7% (703, 17% win) | -8.6% (596, 20% win) | -9.3% (516, 22% win) | -10.8% (422, 23% win) |
| schoon+houders_ok | -6.4% (1024, 28% win) | -6.3% (1119, 28% win) | -6.4% (1212, 28% win) | -6.7% (1280, 28% win) | -7.0% (1363, 27% win) | -5.6% (1440, 27% win) | -4.9% (1471, 28% win) | -4.8% (1333, 30% win) | -3.9% (1213, 34% win) | -4.6% (1065, 34% win) | -6.8% (947, 34% win) |
| schoon+houders_ok+final_stretch | -7.0% (430, 24% win) | -6.8% (467, 24% win) | -6.9% (498, 24% win) | -9.0% (519, 21% win) | -10.3% (539, 17% win) | -9.3% (560, 18% win) | -6.4% (546, 20% win) | -6.9% (419, 22% win) | -8.5% (314, 23% win) | -7.8% (205, 25% win) | -6.8% (125, 25% win) |
| volledige_screening+schoon | -7.1% (296, 25% win) | -6.6% (307, 24% win) | -7.4% (312, 25% win) | -10.2% (321, 20% win) | -11.6% (326, 16% win) | -10.8% (327, 16% win) | -7.4% (314, 18% win) | -8.4% (245, 18% win) | -11.4% (184, 16% win) | -11.1% (123, 16% win) | -12.6% (76, 12% win) |
| volledige_screening+schoon+x_link | -7.3% (231, 25% win) | -6.0% (240, 26% win) | -7.5% (240, 24% win) | -10.7% (243, 19% win) | -12.4% (241, 13% win) | -11.0% (241, 14% win) | -8.0% (234, 16% win) | -8.8% (182, 16% win) | -10.1% (138, 17% win) | -11.4% (96, 16% win) | -12.6% (60, 8% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 321 instappen, mediane hoogste stijging +8.4%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 47% | 23% | -8.5% | 25% |
| +15% | 41% | 18% | -8.6% | 21% |
| +20% | 38% | 16% | -8.7% | 18% |
| +25% | 33% | 13% | -9.1% | 16% |
| +30% | 30% | 12% | -9.2% | 15% |
| +35% | 28% | 11% | -9.3% | 13% |
| +45% | 24% | 8% | -10.1% | 11% |
| +60% | 20% | 6% | -9.9% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1280 instappen, mediane hoogste stijging +21.2%

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

**filter `alle`** — variant `d45_direct`, 4335 instappen, mediane hoogste stijging +22.6%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.9% | 30% |
| +15% | 55% | 30% | -6.1% | 28% |
| +20% | 52% | 27% | -6.3% | 27% |
| +25% | 49% | 24% | -6.3% | 26% |
| +30% | 46% | 21% | -6.4% | 25% |
| +35% | 43% | 19% | -6.5% | 24% |
| +45% | 39% | 16% | -6.6% | 23% |
| +60% | 35% | 13% | -6.6% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.9% (296, 14% win) | -10.2% (296, 14% win) | -8.5% (296, 14% win) | -7.8% (296, 15% win) | -10.9% (296, 14% win) | -10.2% (296, 14% win) |
| d35_direct | -9.5% (307, 16% win) | -8.8% (307, 16% win) | -7.1% (307, 16% win) | -6.5% (307, 16% win) | -9.6% (307, 16% win) | -9.0% (307, 16% win) |
| d40_direct | -11.5% (312, 13% win) | -10.8% (312, 13% win) | -9.1% (312, 14% win) | -8.5% (312, 14% win) | -11.6% (312, 12% win) | -10.9% (312, 13% win) |
| d45_direct | -13.1% (321, 10% win) | -12.5% (321, 10% win) | -10.8% (321, 11% win) | -10.1% (321, 11% win) | -13.3% (321, 9% win) | -12.7% (321, 10% win) |
| d50_direct | -12.9% (326, 9% win) | -12.3% (326, 9% win) | -10.6% (326, 9% win) | -10.0% (326, 9% win) | -13.3% (326, 8% win) | -12.7% (326, 8% win) |
| d55_direct | -11.6% (327, 8% win) | -11.0% (327, 8% win) | -9.4% (327, 8% win) | -8.7% (327, 8% win) | -12.2% (327, 7% win) | -11.6% (327, 8% win) |
| d60_direct | -10.0% (314, 8% win) | -9.3% (314, 8% win) | -7.8% (314, 8% win) | -7.1% (314, 8% win) | -10.9% (314, 7% win) | -10.3% (314, 8% win) |
| d65_direct | -10.0% (245, 9% win) | -9.3% (245, 9% win) | -7.8% (245, 9% win) | -7.1% (245, 9% win) | -11.0% (245, 8% win) | -10.4% (245, 9% win) |
| d70_direct | -11.4% (184, 5% win) | -10.8% (184, 5% win) | -9.2% (184, 5% win) | -8.6% (184, 5% win) | -12.4% (184, 4% win) | -11.8% (184, 5% win) |
| d75_direct | -11.7% (123, 6% win) | -11.0% (123, 6% win) | -9.5% (123, 7% win) | -8.9% (123, 7% win) | -12.9% (123, 5% win) | -12.3% (123, 5% win) |
| d80_direct | -11.8% (76, 4% win) | -11.1% (76, 4% win) | -9.8% (76, 4% win) | -9.1% (76, 4% win) | -13.7% (76, 3% win) | -13.0% (76, 3% win) |
| d45_herstel5 | -10.6% (235, 14% win) | -10.0% (235, 14% win) | -8.3% (235, 14% win) | -7.6% (235, 14% win) | -10.7% (235, 14% win) | -10.1% (235, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.6% (1024, 19% win) | -8.9% (1024, 20% win) | -7.1% (1024, 20% win) | -6.5% (1024, 21% win) | -9.2% (1024, 20% win) | -8.6% (1024, 20% win) |
| d35_direct | -9.8% (1119, 19% win) | -9.1% (1119, 19% win) | -7.3% (1119, 21% win) | -6.7% (1119, 21% win) | -9.5% (1119, 19% win) | -8.9% (1119, 20% win) |
| d40_direct | -10.2% (1212, 18% win) | -9.5% (1212, 19% win) | -7.8% (1212, 20% win) | -7.1% (1212, 20% win) | -10.1% (1212, 18% win) | -9.4% (1212, 19% win) |
| d45_direct | -10.1% (1280, 18% win) | -9.4% (1280, 18% win) | -7.7% (1280, 20% win) | -7.0% (1280, 20% win) | -10.2% (1280, 18% win) | -9.5% (1280, 18% win) |
| d50_direct | -9.8% (1363, 19% win) | -9.1% (1363, 19% win) | -7.5% (1363, 20% win) | -6.8% (1363, 20% win) | -10.1% (1363, 18% win) | -9.4% (1363, 19% win) |
| d55_direct | -8.5% (1440, 19% win) | -7.8% (1440, 19% win) | -6.2% (1440, 20% win) | -5.5% (1440, 20% win) | -9.0% (1440, 18% win) | -8.4% (1440, 19% win) |
| d60_direct | -8.0% (1471, 19% win) | -7.3% (1471, 20% win) | -5.8% (1471, 20% win) | -5.1% (1471, 21% win) | -8.9% (1471, 19% win) | -8.2% (1471, 19% win) |
| d65_direct | -7.3% (1333, 21% win) | -6.6% (1333, 21% win) | -5.2% (1333, 22% win) | -4.5% (1333, 23% win) | -8.5% (1333, 20% win) | -7.9% (1333, 21% win) |
| d70_direct | -6.7% (1213, 24% win) | -6.0% (1213, 24% win) | -4.6% (1213, 25% win) | -3.9% (1213, 25% win) | -8.5% (1213, 23% win) | -7.8% (1213, 23% win) |
| d75_direct | -7.7% (1065, 25% win) | -7.0% (1065, 25% win) | -5.8% (1065, 26% win) | -5.1% (1065, 26% win) | -10.2% (1065, 23% win) | -9.6% (1065, 23% win) |
| d80_direct | -7.6% (947, 27% win) | -6.9% (947, 28% win) | -5.9% (947, 28% win) | -5.2% (947, 28% win) | -11.6% (947, 24% win) | -11.0% (947, 24% win) |
| d45_herstel5 | -7.2% (1063, 23% win) | -6.5% (1063, 23% win) | -4.9% (1063, 24% win) | -4.2% (1063, 24% win) | -7.3% (1063, 23% win) | -6.7% (1063, 23% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.3% (4641, 23% win) | -8.6% (4641, 24% win) | -7.0% (4641, 25% win) | -6.3% (4641, 25% win) | -9.5% (4641, 23% win) | -8.9% (4641, 24% win) |
| d35_direct | -9.3% (4542, 23% win) | -8.6% (4542, 23% win) | -7.0% (4542, 24% win) | -6.4% (4542, 24% win) | -9.8% (4542, 22% win) | -9.1% (4542, 23% win) |
| d40_direct | -9.7% (4442, 22% win) | -9.0% (4442, 22% win) | -7.4% (4442, 23% win) | -6.7% (4442, 23% win) | -10.2% (4442, 21% win) | -9.6% (4442, 22% win) |
| d45_direct | -9.5% (4335, 21% win) | -8.8% (4335, 22% win) | -7.3% (4335, 22% win) | -6.6% (4335, 23% win) | -10.3% (4335, 20% win) | -9.7% (4335, 21% win) |
| d50_direct | -10.0% (4238, 20% win) | -9.3% (4238, 21% win) | -7.8% (4238, 22% win) | -7.1% (4238, 22% win) | -11.0% (4238, 20% win) | -10.4% (4238, 20% win) |
| d55_direct | -9.8% (4079, 20% win) | -9.1% (4079, 20% win) | -7.6% (4079, 21% win) | -6.9% (4079, 21% win) | -11.1% (4079, 18% win) | -10.4% (4079, 19% win) |
| d60_direct | -9.1% (3786, 21% win) | -8.4% (3786, 21% win) | -7.1% (3786, 22% win) | -6.4% (3786, 22% win) | -10.8% (3786, 20% win) | -10.2% (3786, 20% win) |
| d65_direct | -8.9% (3381, 22% win) | -8.2% (3381, 22% win) | -7.0% (3381, 23% win) | -6.3% (3381, 24% win) | -11.1% (3381, 20% win) | -10.5% (3381, 21% win) |
| d70_direct | -8.1% (2994, 24% win) | -7.4% (2994, 25% win) | -6.3% (2994, 25% win) | -5.6% (2994, 26% win) | -11.1% (2994, 22% win) | -10.5% (2994, 23% win) |
| d75_direct | -9.0% (2640, 24% win) | -8.3% (2640, 24% win) | -7.3% (2640, 25% win) | -6.7% (2640, 25% win) | -13.0% (2640, 21% win) | -12.4% (2640, 22% win) |
| d80_direct | -8.9% (2299, 27% win) | -8.2% (2299, 27% win) | -7.7% (2299, 27% win) | -7.0% (2299, 27% win) | -14.8% (2299, 22% win) | -14.3% (2299, 22% win) |
| d45_herstel5 | -9.3% (3560, 25% win) | -8.6% (3560, 25% win) | -7.2% (3560, 26% win) | -6.5% (3560, 26% win) | -10.4% (3560, 24% win) | -9.8% (3560, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.6% (4335, 23% win) | -6.3% (4335, 22% win) | -6.8% (4335, 22% win) |
| schoon | -6.3% (3482, 24% win) | -6.1% (3482, 24% win) | -6.3% (3482, 24% win) |
| bundelgrafiek | -8.0% (853, 16% win) | -6.9% (853, 16% win) | -8.7% (853, 15% win) |
| schoon+houders_ok | -7.0% (1280, 20% win) | -6.6% (1280, 20% win) | -6.2% (1280, 21% win) |
| schoon+houders_ok+final_stretch | -9.0% (519, 12% win) | -7.6% (519, 11% win) | -9.7% (519, 14% win) |
| volledige_screening+schoon | -10.1% (321, 11% win) | -8.9% (321, 9% win) | -10.9% (321, 14% win) |
| volledige_screening+schoon+x_link | -10.3% (243, 11% win) | -9.0% (243, 9% win) | -11.3% (243, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.9% (1862, 29% win); 1,3–2x: -8.0% (1620, 18% win); ≥ 2x (bundelgrafiek): -8.0% (853, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.6% (2795, 29% win); 5–20%: -8.8% (782, 13% win); ≥ 20%: -8.3% (758, 10% win)

**top t.o.v. start:** 2–3x: -6.2% (2431, 22% win); 3–6x: -6.7% (1490, 24% win); ≥ 6x: -8.8% (414, 22% win)

**unieke kopers tot de top:** < 30: -5.5% (2797, 29% win); 30–100: -7.5% (849, 11% win); ≥ 100: -10.0% (689, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -7.8% (1071, 16% win); 1–2: -6.0% (2070, 25% win); ≥ 3 (trap): -6.8% (1194, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.4% (1053, 11% win); 10–25%: -7.3% (667, 12% win); ≥ 25%: -5.3% (2615, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.0% (3456, 25% win); 30 s–3 min: -8.7% (692, 15% win); ≥ 3 min (langzaam): -9.9% (187, 7% win)

**tijd van start tot top:** < 2 min: -6.4% (3598, 24% win); 2–10 min: -7.4% (590, 16% win); ≥ 10 min: -9.2% (147, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
