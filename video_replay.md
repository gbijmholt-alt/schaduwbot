# Videostrategie op alle trades — 2026-09-11 23:49 UTC

Tokens sinds 2026-09-11 08:47 UTC: 10282 geschikt (≥ 2 uur oud, geen herstart), 8512 met trades, 1776 haalden 2x de startkoers, 1362 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 408 tokens. Houdercheck echt uitgevoerd bij 65% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 448, winkans 20%, EV per trade -7.6% (95%-marge -10.3% tot -4.8%), mediaan -9.7%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 591, winkans 21%, EV -8.8% (95%-marge -12.4% tot -5.3%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 1362 | 37% | 78% | 0% |
| schoon | 1080 | 39% | 78% | 0% |
| bundelgrafiek | 282 | 28% | 77% | 0% |
| schoon+houders_ok | 448 | 38% | 80% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.3% (1391, 23% win) | -7.2% (1362, 22% win) | -8.7% (1336, 20% win) | -7.0% (1085, 26% win) |
| schoon | -7.0% (1107, 24% win) | -6.9% (1080, 23% win) | -7.8% (1062, 22% win) | -7.1% (898, 26% win) |
| bundelgrafiek | -8.2% (284, 19% win) | -8.3% (282, 18% win) | -12.0% (274, 14% win) | -6.3% (187, 24% win) |
| schoon+houders_ok | -6.7% (430, 21% win) | -7.6% (448, 20% win) | -7.8% (478, 18% win) | -4.8% (361, 24% win) |
| schoon+houders_ok+final_stretch | -8.6% (171, 13% win) | -9.9% (176, 10% win) | -8.6% (179, 9% win) | -7.6% (126, 15% win) |
| volledige_screening+schoon | -9.5% (121, 12% win) | -10.8% (124, 8% win) | -9.7% (124, 9% win) | -7.5% (82, 17% win) |
| volledige_screening+schoon+x_link | -8.8% (95, 15% win) | -10.5% (96, 8% win) | -9.3% (95, 8% win) | -8.2% (55, 16% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.2% (1362, 22% win) | -6.5% (1362, 22% win) | -7.1% (1362, 21% win) |
| schoon | -6.9% (1080, 23% win) | -6.3% (1080, 23% win) | -6.1% (1080, 23% win) |
| bundelgrafiek | -8.3% (282, 18% win) | -7.1% (282, 18% win) | -10.8% (282, 14% win) |
| schoon+houders_ok | -7.6% (448, 20% win) | -6.9% (448, 21% win) | -7.5% (448, 21% win) |
| schoon+houders_ok+final_stretch | -9.9% (176, 10% win) | -8.2% (176, 11% win) | -10.5% (176, 12% win) |
| volledige_screening+schoon | -10.8% (124, 8% win) | -9.2% (124, 9% win) | -12.6% (124, 12% win) |
| volledige_screening+schoon+x_link | -10.5% (96, 8% win) | -9.2% (96, 8% win) | -13.1% (96, 9% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (525, 29% win); 1,3–2x: -8.0% (555, 18% win); ≥ 2x (bundelgrafiek): -8.3% (282, 18% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.9% (839, 29% win); 5–20%: -10.1% (274, 12% win); ≥ 20%: -8.2% (249, 12% win)

**top t.o.v. start:** 2–3x: -7.3% (748, 20% win); 3–6x: -6.0% (476, 25% win); ≥ 6x: -10.4% (138, 23% win)

**unieke kopers tot de top:** < 30: -5.8% (841, 29% win); 30–100: -8.1% (241, 11% win); ≥ 100: -10.4% (280, 11% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -10.3% (382, 13% win); 1–2: -4.9% (635, 26% win); ≥ 3 (trap): -8.0% (345, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.6% (380, 11% win); 10–25%: -8.4% (213, 13% win); ≥ 25%: -5.6% (769, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.8% (1099, 24% win); 30 s–3 min: -8.0% (211, 16% win); ≥ 3 min (langzaam): -12.4% (52, 6% win)

**tijd van start tot top:** < 2 min: -6.5% (1118, 24% win); 2–10 min: -10.9% (187, 13% win); ≥ 10 min: -9.1% (57, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
