# Videostrategie op alle trades — 2026-09-12 12:08 UTC

Tokens sinds 2026-09-11 08:47 UTC: 19594 geschikt (≥ 2 uur oud, geen herstart), 16626 met trades, 3438 haalden 2x de startkoers, 2643 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 782 tokens. Houdercheck echt uitgevoerd bij 82% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 925, winkans 20%, EV per trade -7.2% (95%-marge -9.3% tot -5.1%), mediaan -10.1%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 1616, winkans 23%, EV -6.9% (95%-marge -9.5% tot -4.3%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 2643 | 38% | 76% | 0% |
| schoon | 2105 | 40% | 76% | 0% |
| bundelgrafiek | 538 | 28% | 76% | 0% |
| schoon+houders_ok | 925 | 37% | 79% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.7% (2700, 22% win) | -7.3% (2643, 22% win) | -7.9% (2589, 21% win) | -5.7% (2103, 27% win) |
| schoon | -7.2% (2156, 23% win) | -6.9% (2105, 24% win) | -7.1% (2069, 23% win) | -5.0% (1753, 28% win) |
| bundelgrafiek | -9.4% (544, 18% win) | -9.0% (538, 17% win) | -10.9% (520, 14% win) | -8.9% (350, 22% win) |
| schoon+houders_ok | -7.5% (884, 20% win) | -7.2% (925, 20% win) | -7.0% (982, 20% win) | -3.2% (754, 25% win) |
| schoon+houders_ok+final_stretch | -9.4% (355, 12% win) | -9.3% (365, 12% win) | -9.1% (376, 10% win) | -6.2% (273, 16% win) |
| volledige_screening+schoon | -10.7% (209, 12% win) | -11.2% (215, 10% win) | -10.7% (219, 9% win) | -8.4% (148, 15% win) |
| volledige_screening+schoon+x_link | -10.7% (165, 13% win) | -11.3% (167, 10% win) | -10.8% (168, 8% win) | -9.3% (107, 13% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.3% (2643, 22% win) | -6.9% (2643, 22% win) | -6.7% (2643, 21% win) |
| schoon | -6.9% (2105, 24% win) | -6.5% (2105, 24% win) | -6.0% (2105, 23% win) |
| bundelgrafiek | -9.0% (538, 17% win) | -8.2% (538, 16% win) | -9.5% (538, 14% win) |
| schoon+houders_ok | -7.2% (925, 20% win) | -6.6% (925, 20% win) | -5.4% (925, 21% win) |
| schoon+houders_ok+final_stretch | -9.3% (365, 12% win) | -7.8% (365, 11% win) | -9.7% (365, 13% win) |
| volledige_screening+schoon | -11.2% (215, 10% win) | -9.6% (215, 9% win) | -11.3% (215, 14% win) |
| volledige_screening+schoon+x_link | -11.3% (167, 10% win) | -9.8% (167, 8% win) | -12.2% (167, 11% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (1040, 30% win); 1,3–2x: -8.0% (1065, 18% win); ≥ 2x (bundelgrafiek): -9.0% (538, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.2% (1620, 29% win); 5–20%: -9.1% (533, 12% win); ≥ 20%: -8.8% (490, 10% win)

**top t.o.v. start:** 2–3x: -7.0% (1486, 21% win); 3–6x: -7.1% (908, 24% win); ≥ 6x: -9.9% (249, 23% win)

**unieke kopers tot de top:** < 30: -6.0% (1634, 30% win); 30–100: -8.2% (547, 10% win); ≥ 100: -10.9% (462, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -9.1% (677, 15% win); 1–2: -6.1% (1263, 25% win); ≥ 3 (trap): -7.7% (703, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -10.2% (709, 11% win); 10–25%: -7.4% (430, 12% win); ≥ 25%: -5.9% (1504, 31% win)

**duur van top naar dip:** < 30 s (crash): -6.8% (2116, 24% win); 30 s–3 min: -8.6% (428, 16% win); ≥ 3 min (langzaam): -12.0% (99, 4% win)

**tijd van start tot top:** < 2 min: -6.5% (2215, 24% win); 2–10 min: -11.8% (340, 14% win); ≥ 10 min: -10.7% (88, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
