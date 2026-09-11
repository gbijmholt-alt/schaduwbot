# Videostrategie op alle trades — 2026-09-11 18:39 UTC

Tokens sinds 2026-09-11 08:47 UTC: 2521 geschikt (≥ 2 uur oud, geen herstart), 2161 met trades, 386 haalden 2x de startkoers, 288 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 118 tokens. Houdercheck echt uitgevoerd bij 46% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 62, winkans 21%, EV per trade -5.2% (95%-marge -12.2% tot +1.8%), mediaan -9.7%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: nog geen trades.

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 288 | 33% | 79% | 0% |
| schoon | 202 | 38% | 77% | 0% |
| bundelgrafiek | 86 | 23% | 84% | 0% |
| schoon+houders_ok | 62 | 32% | 79% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -5.1% (300, 22% win) | -4.4% (288, 24% win) | -6.7% (280, 20% win) | -4.0% (233, 30% win) |
| schoon | -1.6% (212, 26% win) | -1.5% (202, 28% win) | -3.4% (196, 24% win) | -2.5% (173, 32% win) |
| bundelgrafiek | -13.6% (88, 12% win) | -11.1% (86, 15% win) | -14.4% (84, 11% win) | -8.3% (60, 22% win) |
| schoon+houders_ok | -1.2% (59, 20% win) | -5.2% (62, 21% win) | -9.1% (66, 15% win) | -4.5% (51, 20% win) |
| schoon+houders_ok+final_stretch | -5.9% (23, 9% win) | -9.1% (24, 4% win) | -10.0% (24, 4% win) | -8.7% (19, 5% win) |
| volledige_screening+schoon | -5.4% (13, 15% win) | -10.0% (14, 7% win) | -15.6% (14, 0% win) | -8.0% (11, 9% win) |
| volledige_screening+schoon+x_link | -5.1% (12, 17% win) | -9.8% (13, 8% win) | -16.1% (13, 0% win) | -7.6% (10, 10% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -4.4% (288, 24% win) | -3.5% (288, 24% win) | -1.3% (288, 22% win) |
| schoon | -1.5% (202, 28% win) | -0.7% (202, 28% win) | +3.9% (202, 28% win) |
| bundelgrafiek | -11.1% (86, 15% win) | -10.3% (86, 15% win) | -13.5% (86, 9% win) |
| schoon+houders_ok | -5.2% (62, 21% win) | -4.2% (62, 21% win) | -5.7% (62, 21% win) |
| schoon+houders_ok+final_stretch | -9.1% (24, 4% win) | -7.4% (24, 4% win) | -7.0% (24, 8% win) |
| volledige_screening+schoon | -10.0% (14, 7% win) | -9.0% (14, 7% win) | -14.8% (14, 7% win) |
| volledige_screening+schoon+x_link | -9.8% (13, 8% win) | -9.1% (13, 8% win) | -14.7% (13, 8% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: +1.1% (97, 34% win); 1,3–2x: -4.0% (105, 22% win); ≥ 2x (bundelgrafiek): -11.1% (86, 15% win)

**aandeel supply gekocht in creatieblok:** < 5%: -4.0% (167, 30% win); 5–20%: -5.4% (59, 14% win); ≥ 20%: -4.3% (62, 18% win)

**top t.o.v. start:** 2–3x: -6.5% (177, 20% win); 3–6x: +2.6% (86, 35% win); ≥ 6x: -13.6% (25, 12% win)

**unieke kopers tot de top:** < 30: -4.0% (181, 29% win); 30–100: -4.4% (55, 14% win); ≥ 100: -5.7% (52, 15% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -10.1% (89, 15% win); 1–2: +0.4% (132, 30% win); ≥ 3 (trap): -6.1% (67, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -4.5% (76, 17% win); 10–25%: -5.4% (49, 14% win); ≥ 25%: -4.0% (163, 30% win)

**duur van top naar dip:** < 30 s (crash): -3.6% (229, 26% win); 30 s–3 min: -5.1% (45, 22% win); ≥ 3 min (langzaam): -14.3% (14, 0% win)

**tijd van start tot top:** < 2 min: -4.6% (249, 25% win); 2–10 min: -0.9% (28, 18% win); ≥ 10 min: -9.0% (11, 9% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
