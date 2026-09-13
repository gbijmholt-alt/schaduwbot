# Videostrategie op alle trades — 2026-09-13 05:47 UTC

Tokens sinds 2026-09-11 08:47 UTC: 33476 geschikt (≥ 2 uur oud, geen herstart), 27032 met trades, 5246 haalden 2x de startkoers, 3998 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1224 tokens. Houdercheck echt uitgevoerd bij 88% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1225, winkans 21%, EV per trade -6.9% (95%-marge -8.8% tot -5.0%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2694, winkans 23%, EV -6.7% (95%-marge -8.8% tot -4.7%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 3998 | 40% | 76% | 0% |
| schoon | 3183 | 43% | 76% | 0% |
| bundelgrafiek | 815 | 29% | 78% | 0% |
| schoon+houders_ok | 1225 | 38% | 79% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.0% (4095, 23% win) | -6.8% (3998, 23% win) | -7.3% (3907, 22% win) | -6.6% (3282, 27% win) |
| schoon | -6.5% (3269, 25% win) | -6.5% (3183, 24% win) | -6.8% (3114, 23% win) | -5.9% (2734, 28% win) |
| bundelgrafiek | -8.7% (826, 17% win) | -8.1% (815, 17% win) | -9.3% (793, 15% win) | -9.6% (548, 22% win) |
| schoon+houders_ok | -7.1% (1159, 20% win) | -6.9% (1225, 21% win) | -6.7% (1301, 21% win) | -4.0% (1019, 24% win) |
| schoon+houders_ok+final_stretch | -8.0% (463, 13% win) | -8.8% (484, 12% win) | -8.8% (501, 10% win) | -5.9% (374, 16% win) |
| volledige_screening+schoon | -8.5% (282, 14% win) | -9.9% (293, 11% win) | -10.1% (298, 9% win) | -7.5% (214, 14% win) |
| volledige_screening+schoon+x_link | -8.8% (221, 15% win) | -10.1% (225, 11% win) | -10.4% (223, 8% win) | -8.1% (158, 13% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -6.8% (3998, 23% win) | -6.5% (3998, 22% win) | -6.7% (3998, 22% win) |
| schoon | -6.5% (3183, 24% win) | -6.3% (3183, 24% win) | -6.2% (3183, 24% win) |
| bundelgrafiek | -8.1% (815, 17% win) | -7.1% (815, 16% win) | -8.7% (815, 15% win) |
| schoon+houders_ok | -6.9% (1225, 21% win) | -6.5% (1225, 20% win) | -6.0% (1225, 21% win) |
| schoon+houders_ok+final_stretch | -8.8% (484, 12% win) | -7.4% (484, 11% win) | -9.5% (484, 14% win) |
| volledige_screening+schoon | -9.9% (293, 11% win) | -8.6% (293, 10% win) | -10.7% (293, 14% win) |
| volledige_screening+schoon+x_link | -10.1% (225, 11% win) | -8.7% (225, 9% win) | -11.0% (225, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.9% (1698, 29% win); 1,3–2x: -8.2% (1485, 18% win); ≥ 2x (bundelgrafiek): -8.1% (815, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.9% (2582, 29% win); 5–20%: -8.6% (711, 13% win); ≥ 20%: -8.4% (705, 10% win)

**top t.o.v. start:** 2–3x: -6.4% (2238, 22% win); 3–6x: -6.9% (1372, 24% win); ≥ 6x: -8.6% (388, 22% win)

**unieke kopers tot de top:** < 30: -5.8% (2589, 29% win); 30–100: -7.4% (773, 11% win); ≥ 100: -10.1% (636, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.1% (1014, 16% win); 1–2: -5.8% (1902, 25% win); ≥ 3 (trap): -7.2% (1082, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.4% (957, 12% win); 10–25%: -7.2% (619, 12% win); ≥ 25%: -5.7% (2422, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.3% (3208, 25% win); 30 s–3 min: -8.4% (631, 15% win); ≥ 3 min (langzaam): -9.6% (159, 7% win)

**tijd van start tot top:** < 2 min: -6.5% (3338, 24% win); 2–10 min: -7.9% (527, 16% win); ≥ 10 min: -9.2% (133, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
