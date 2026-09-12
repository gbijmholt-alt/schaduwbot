# Videostrategie op alle trades — 2026-09-12 23:35 UTC

Tokens sinds 2026-09-11 08:47 UTC: 26354 geschikt (≥ 2 uur oud, geen herstart), 22034 met trades, 4417 haalden 2x de startkoers, 3365 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1028 tokens. Houdercheck echt uitgevoerd bij 86% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1162, winkans 21%, EV per trade -6.7% (95%-marge -8.6% tot -4.7%), mediaan -10.1%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2185, winkans 23%, EV -7.3% (95%-marge -9.6% tot -5.1%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 3365 | 39% | 76% | 0% |
| schoon | 2674 | 42% | 76% | 0% |
| bundelgrafiek | 691 | 29% | 77% | 0% |
| schoon+houders_ok | 1162 | 38% | 78% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.5% (3441, 23% win) | -7.3% (3365, 22% win) | -7.7% (3287, 22% win) | -6.6% (2728, 27% win) |
| schoon | -7.0% (2743, 24% win) | -6.9% (2674, 24% win) | -7.1% (2616, 23% win) | -5.9% (2272, 28% win) |
| bundelgrafiek | -9.3% (698, 17% win) | -9.0% (691, 16% win) | -10.3% (671, 14% win) | -10.0% (456, 22% win) |
| schoon+houders_ok | -7.1% (1109, 20% win) | -6.7% (1162, 21% win) | -6.5% (1224, 22% win) | -3.8% (971, 25% win) |
| schoon+houders_ok+final_stretch | -8.1% (434, 13% win) | -8.8% (449, 12% win) | -8.7% (456, 10% win) | -6.1% (349, 15% win) |
| volledige_screening+schoon | -9.1% (265, 13% win) | -10.3% (272, 11% win) | -10.2% (270, 9% win) | -8.1% (200, 14% win) |
| volledige_screening+schoon+x_link | -9.4% (207, 14% win) | -10.4% (211, 10% win) | -10.3% (206, 8% win) | -9.0% (148, 12% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.3% (3365, 22% win) | -6.9% (3365, 22% win) | -7.2% (3365, 22% win) |
| schoon | -6.9% (2674, 24% win) | -6.7% (2674, 24% win) | -6.5% (2674, 24% win) |
| bundelgrafiek | -9.0% (691, 16% win) | -8.0% (691, 16% win) | -10.1% (691, 14% win) |
| schoon+houders_ok | -6.7% (1162, 21% win) | -6.3% (1162, 21% win) | -5.6% (1162, 22% win) |
| schoon+houders_ok+final_stretch | -8.8% (449, 12% win) | -7.3% (449, 12% win) | -9.3% (449, 14% win) |
| volledige_screening+schoon | -10.3% (272, 11% win) | -8.7% (272, 10% win) | -10.9% (272, 14% win) |
| volledige_screening+schoon+x_link | -10.4% (211, 10% win) | -8.9% (211, 9% win) | -11.3% (211, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (1388, 29% win); 1,3–2x: -8.2% (1286, 18% win); ≥ 2x (bundelgrafiek): -9.0% (691, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.5% (2151, 28% win); 5–20%: -9.0% (609, 12% win); ≥ 20%: -8.5% (605, 11% win)

**top t.o.v. start:** 2–3x: -7.1% (1884, 21% win); 3–6x: -6.8% (1155, 24% win); ≥ 6x: -10.5% (326, 22% win)

**unieke kopers tot de top:** < 30: -6.3% (2147, 29% win); 30–100: -7.8% (655, 10% win); ≥ 100: -10.4% (563, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.3% (852, 15% win); 1–2: -6.5% (1595, 24% win); ≥ 3 (trap): -7.9% (918, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -10.0% (834, 11% win); 10–25%: -7.0% (514, 12% win); ≥ 25%: -6.3% (2017, 30% win)

**duur van top naar dip:** < 30 s (crash): -7.0% (2705, 24% win); 30 s–3 min: -8.5% (525, 16% win); ≥ 3 min (langzaam): -9.5% (135, 7% win)

**tijd van start tot top:** < 2 min: -7.0% (2814, 24% win); 2–10 min: -9.3% (436, 15% win); ≥ 10 min: -8.8% (115, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
