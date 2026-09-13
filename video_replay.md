# Videostrategie op alle trades — 2026-09-13 06:44 UTC

Tokens sinds 2026-09-11 08:47 UTC: 34443 geschikt (≥ 2 uur oud, geen herstart), 27644 met trades, 5349 haalden 2x de startkoers, 4078 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1248 tokens. Houdercheck echt uitgevoerd bij 88% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1240, winkans 21%, EV per trade -6.9% (95%-marge -8.8% tot -5.1%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2760, winkans 24%, EV -6.6% (95%-marge -8.6% tot -4.5%).
- **H3** (2026-09-13 06:00 UTC): instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening. Aanleiding: voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — 76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst.. Resultaat: nog geen trades.

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 4078 | 40% | 76% | 37% |
| schoon | 3249 | 43% | 76% | 40% |
| bundelgrafiek | 829 | 29% | 78% | 25% |
| schoon+houders_ok | 1240 | 38% | 79% | 27% |

## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct | d45_herstel5 |
|---|---|---|---|---|---|---|---|---|
| alle | -6.3% (4356, 25% win) | -6.4% (4268, 24% win) | -6.9% (4175, 23% win) | -6.7% (4078, 23% win) | -7.3% (3985, 22% win) | -7.1% (3836, 21% win) | -6.5% (3563, 22% win) | -6.5% (3348, 27% win) |
| schoon | -6.1% (3478, 26% win) | -6.0% (3414, 26% win) | -6.5% (3335, 25% win) | -6.4% (3249, 24% win) | -6.8% (3179, 23% win) | -6.9% (3055, 23% win) | -6.1% (2810, 24% win) | -5.9% (2792, 27% win) |
| bundelgrafiek | -7.1% (878, 22% win) | -8.3% (854, 19% win) | -8.5% (840, 17% win) | -8.1% (829, 16% win) | -9.5% (806, 15% win) | -7.7% (781, 15% win) | -8.1% (753, 15% win) | -9.5% (556, 22% win) |
| schoon+houders_ok | -6.6% (989, 21% win) | -6.8% (1084, 21% win) | -7.1% (1173, 20% win) | -6.9% (1240, 21% win) | -6.6% (1320, 21% win) | -5.4% (1389, 21% win) | -4.9% (1413, 21% win) | -4.0% (1032, 24% win) |
| schoon+houders_ok+final_stretch | -7.8% (409, 16% win) | -7.0% (446, 16% win) | -8.0% (473, 13% win) | -8.8% (495, 12% win) | -8.5% (513, 10% win) | -7.5% (532, 10% win) | -6.7% (516, 10% win) | -5.9% (384, 15% win) |
| volledige_screening+schoon | -7.9% (278, 16% win) | -6.3% (289, 17% win) | -8.6% (291, 13% win) | -10.0% (303, 11% win) | -9.7% (308, 10% win) | -8.4% (309, 8% win) | -6.9% (298, 9% win) | -7.5% (223, 14% win) |
| volledige_screening+schoon+x_link | -8.5% (218, 16% win) | -5.2% (227, 20% win) | -8.8% (226, 15% win) | -10.2% (230, 11% win) | -10.0% (228, 9% win) | -9.2% (228, 8% win) | -8.4% (221, 7% win) | -8.0% (162, 13% win) |

## Regel van Gerben: dip 55%, stop op 65% vanaf de top, winst op +30%, breakeven bij +20%

De stop is een koersniveau t.o.v. de top (ATH × 0.35), niet een percentage onder de instap. Bij instap op een dip van 55% ligt hij dus ruim 22% onder de instapprijs — waar de videoregel maar 3% ruimte geeft. Zodra +20% is aangetikt schuift de stop naar de instapprijs. Hieronder de regel op élke dipdiepte, zodat te zien is of 55% inderdaad het beste instapmoment is. **Vooraf vastgelegd als H3 op de 55%-variant met volledige screening; de rest is verkennend.**

| filter | d30_direct | d35_direct | d40_direct | d45_direct | d50_direct | d55_direct | d60_direct |
|---|---|---|---|---|---|---|---|
| alle | -7.1% (4356, 35% win) | -6.8% (4268, 34% win) | -7.0% (4175, 32% win) | -7.1% (4078, 30% win) | -7.6% (3985, 27% win) | -6.9% (3836, 26% win) | -5.9% (3563, 26% win) |
| schoon | -7.2% (3478, 36% win) | -6.6% (3414, 35% win) | -7.0% (3335, 33% win) | -7.1% (3249, 31% win) | -7.6% (3179, 29% win) | -7.0% (3055, 27% win) | -5.6% (2810, 28% win) |
| bundelgrafiek | -7.0% (878, 32% win) | -7.8% (854, 29% win) | -6.8% (840, 26% win) | -7.0% (829, 24% win) | -7.8% (806, 22% win) | -6.7% (781, 20% win) | -7.1% (753, 17% win) |
| schoon+houders_ok | -8.4% (989, 37% win) | -7.6% (1084, 36% win) | -7.3% (1173, 34% win) | -7.5% (1240, 32% win) | -7.4% (1320, 30% win) | -5.5% (1389, 28% win) | -4.3% (1413, 26% win) |
| schoon+houders_ok+final_stretch | -10.1% (409, 35% win) | -9.2% (446, 34% win) | -9.6% (473, 30% win) | -10.4% (495, 26% win) | -10.9% (513, 21% win) | -9.3% (532, 18% win) | -6.9% (516, 15% win) |
| volledige_screening+schoon | -10.3% (278, 37% win) | -10.0% (289, 35% win) | -11.6% (291, 31% win) | -11.9% (303, 27% win) | -12.3% (308, 20% win) | -10.8% (309, 17% win) | -7.4% (298, 13% win) |
| volledige_screening+schoon+x_link | -10.0% (218, 36% win) | -10.6% (227, 34% win) | -12.1% (226, 29% win) | -13.3% (230, 24% win) | -13.5% (228, 17% win) | -10.8% (228, 15% win) | -7.8% (221, 12% win) |


## Wordt die +45% na de dip wel gehaald?

De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: **ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.

**filter `volledige_screening+schoon`** — variant `d45_direct`, 303 instappen, mediane hoogste stijging +8.3%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 47% | 23% | -8.6% | 24% |
| +15% | 41% | 18% | -8.7% | 20% |
| +20% | 38% | 16% | -8.7% | 18% |
| +25% | 33% | 13% | -8.9% | 16% |
| +30% | 30% | 12% | -9.0% | 15% |
| +35% | 28% | 11% | -9.1% | 14% |
| +45% | 24% | 8% | -10.0% | 11% |
| +60% | 20% | 7% | -9.8% | 10% |

**filter `schoon+houders_ok`** — variant `d45_direct`, 1240 instappen, mediane hoogste stijging +21.5%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -5.4% | 31% |
| +15% | 54% | 28% | -5.6% | 28% |
| +20% | 51% | 24% | -5.7% | 26% |
| +25% | 48% | 22% | -5.9% | 24% |
| +30% | 46% | 20% | -6.0% | 24% |
| +35% | 42% | 17% | -6.2% | 22% |
| +45% | 38% | 14% | -6.9% | 21% |
| +60% | 33% | 11% | -6.7% | 19% |

**filter `alle`** — variant `d45_direct`, 4078 instappen, mediane hoogste stijging +22.7%

| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |
|---|---|---|---|---|
| +10% | 59% | 34% | -6.0% | 30% |
| +15% | 55% | 30% | -6.3% | 28% |
| +20% | 52% | 27% | -6.4% | 26% |
| +25% | 49% | 24% | -6.4% | 26% |
| +30% | 46% | 21% | -6.5% | 25% |
| +35% | 43% | 19% | -6.7% | 24% |
| +45% | 39% | 16% | -6.7% | 23% |
| +60% | 35% | 13% | -6.6% | 22% |


## Alle inzetgroottes en beide terminals (videoregel)

Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.

**filter `volledige_screening+schoon`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -10.9% (278, 14% win) | -10.2% (278, 14% win) | -8.5% (278, 15% win) | -7.9% (278, 16% win) | -10.9% (278, 14% win) | -10.3% (278, 14% win) |
| d35_direct | -9.3% (289, 16% win) | -8.6% (289, 16% win) | -7.0% (289, 17% win) | -6.3% (289, 17% win) | -9.4% (289, 16% win) | -8.8% (289, 16% win) |
| d40_direct | -11.6% (291, 13% win) | -10.9% (291, 13% win) | -9.2% (291, 13% win) | -8.6% (291, 13% win) | -11.7% (291, 12% win) | -11.1% (291, 13% win) |
| d45_direct | -13.0% (303, 10% win) | -12.3% (303, 10% win) | -10.6% (303, 11% win) | -10.0% (303, 11% win) | -13.1% (303, 10% win) | -12.5% (303, 10% win) |
| d50_direct | -12.6% (308, 9% win) | -11.9% (308, 9% win) | -10.3% (308, 9% win) | -9.7% (308, 10% win) | -13.0% (308, 8% win) | -12.4% (308, 9% win) |
| d55_direct | -11.3% (309, 8% win) | -10.7% (309, 8% win) | -9.1% (309, 8% win) | -8.4% (309, 8% win) | -12.0% (309, 7% win) | -11.3% (309, 8% win) |
| d60_direct | -9.8% (298, 9% win) | -9.1% (298, 9% win) | -7.6% (298, 9% win) | -6.9% (298, 9% win) | -10.7% (298, 7% win) | -10.1% (298, 8% win) |
| d45_herstel5 | -10.5% (223, 14% win) | -9.8% (223, 14% win) | -8.1% (223, 14% win) | -7.5% (223, 14% win) | -10.6% (223, 14% win) | -9.9% (223, 14% win) |

**filter `schoon+houders_ok`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.8% (989, 19% win) | -9.1% (989, 20% win) | -7.3% (989, 21% win) | -6.6% (989, 21% win) | -9.4% (989, 20% win) | -8.7% (989, 20% win) |
| d35_direct | -9.8% (1084, 19% win) | -9.2% (1084, 19% win) | -7.4% (1084, 21% win) | -6.8% (1084, 21% win) | -9.6% (1084, 19% win) | -9.0% (1084, 20% win) |
| d40_direct | -10.2% (1173, 19% win) | -9.5% (1173, 19% win) | -7.8% (1173, 20% win) | -7.1% (1173, 20% win) | -10.1% (1173, 19% win) | -9.4% (1173, 19% win) |
| d45_direct | -10.0% (1240, 18% win) | -9.3% (1240, 19% win) | -7.6% (1240, 20% win) | -6.9% (1240, 21% win) | -10.0% (1240, 18% win) | -9.4% (1240, 19% win) |
| d50_direct | -9.6% (1320, 19% win) | -8.9% (1320, 19% win) | -7.3% (1320, 20% win) | -6.6% (1320, 21% win) | -9.9% (1320, 19% win) | -9.2% (1320, 19% win) |
| d55_direct | -8.4% (1389, 19% win) | -7.7% (1389, 19% win) | -6.1% (1389, 20% win) | -5.4% (1389, 21% win) | -8.9% (1389, 18% win) | -8.3% (1389, 19% win) |
| d60_direct | -7.8% (1413, 20% win) | -7.1% (1413, 20% win) | -5.6% (1413, 21% win) | -4.9% (1413, 21% win) | -8.7% (1413, 19% win) | -8.1% (1413, 20% win) |
| d45_herstel5 | -7.0% (1032, 23% win) | -6.3% (1032, 23% win) | -4.6% (1032, 24% win) | -4.0% (1032, 24% win) | -7.1% (1032, 23% win) | -6.5% (1032, 23% win) |

**filter `alle`**

| variant | 0.05_axiom | 0.05_pp | 0.2_axiom | 0.2_pp | 1.0_axiom | 1.0_pp |
|---|---|---|---|---|---|---|
| d30_direct | -9.3% (4356, 24% win) | -8.7% (4356, 24% win) | -7.0% (4356, 25% win) | -6.3% (4356, 25% win) | -9.6% (4356, 23% win) | -8.9% (4356, 24% win) |
| d35_direct | -9.4% (4268, 23% win) | -8.7% (4268, 23% win) | -7.1% (4268, 24% win) | -6.4% (4268, 24% win) | -9.8% (4268, 22% win) | -9.2% (4268, 23% win) |
| d40_direct | -9.8% (4175, 22% win) | -9.2% (4175, 22% win) | -7.6% (4175, 23% win) | -6.9% (4175, 23% win) | -10.4% (4175, 21% win) | -9.8% (4175, 22% win) |
| d45_direct | -9.6% (4078, 21% win) | -8.9% (4078, 22% win) | -7.4% (4078, 22% win) | -6.7% (4078, 23% win) | -10.4% (4078, 20% win) | -9.8% (4078, 21% win) |
| d50_direct | -10.2% (3985, 20% win) | -9.5% (3985, 21% win) | -8.0% (3985, 21% win) | -7.3% (3985, 22% win) | -11.2% (3985, 19% win) | -10.6% (3985, 20% win) |
| d55_direct | -9.9% (3836, 20% win) | -9.2% (3836, 20% win) | -7.8% (3836, 21% win) | -7.1% (3836, 21% win) | -11.2% (3836, 18% win) | -10.6% (3836, 19% win) |
| d60_direct | -9.2% (3563, 21% win) | -8.6% (3563, 21% win) | -7.2% (3563, 22% win) | -6.5% (3563, 22% win) | -10.9% (3563, 20% win) | -10.3% (3563, 20% win) |
| d45_herstel5 | -9.4% (3348, 25% win) | -8.7% (3348, 25% win) | -7.2% (3348, 26% win) | -6.5% (3348, 27% win) | -10.5% (3348, 24% win) | -9.8% (3348, 24% win) |


## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.7% (4078, 23% win) | -6.4% (4078, 22% win) | -6.5% (4078, 22% win) |
| schoon | -6.4% (3249, 24% win) | -6.2% (3249, 24% win) | -6.0% (3249, 24% win) |
| bundelgrafiek | -8.1% (829, 16% win) | -7.1% (829, 16% win) | -8.6% (829, 15% win) |
| schoon+houders_ok | -6.9% (1240, 21% win) | -6.5% (1240, 20% win) | -6.0% (1240, 21% win) |
| schoon+houders_ok+final_stretch | -8.8% (495, 12% win) | -7.4% (495, 11% win) | -9.4% (495, 14% win) |
| volledige_screening+schoon | -10.0% (303, 11% win) | -8.6% (303, 10% win) | -10.5% (303, 14% win) |
| volledige_screening+schoon+x_link | -10.2% (230, 11% win) | -8.7% (230, 9% win) | -11.0% (230, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.9% (1733, 29% win); 1,3–2x: -8.1% (1516, 18% win); ≥ 2x (bundelgrafiek): -8.1% (829, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.7% (2631, 29% win); 5–20%: -8.8% (730, 13% win); ≥ 20%: -8.4% (717, 10% win)

**top t.o.v. start:** 2–3x: -6.4% (2280, 22% win); 3–6x: -6.9% (1402, 24% win); ≥ 6x: -8.4% (396, 22% win)

**unieke kopers tot de top:** < 30: -5.7% (2635, 29% win); 30–100: -7.5% (791, 11% win); ≥ 100: -10.2% (652, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.0% (1023, 16% win); 1–2: -5.9% (1948, 25% win); ≥ 3 (trap): -7.0% (1107, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.6% (983, 11% win); 10–25%: -7.2% (631, 12% win); ≥ 25%: -5.5% (2464, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.2% (3261, 25% win); 30 s–3 min: -8.5% (652, 15% win); ≥ 3 min (langzaam): -9.9% (165, 7% win)

**tijd van start tot top:** < 2 min: -6.4% (3395, 24% win); 2–10 min: -7.9% (546, 16% win); ≥ 10 min: -9.2% (137, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
