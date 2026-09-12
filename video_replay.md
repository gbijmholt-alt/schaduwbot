# Videostrategie op alle trades — 2026-09-12 17:30 UTC

Tokens sinds 2026-09-11 08:47 UTC: 24457 geschikt (≥ 2 uur oud, geen herstart), 20868 met trades, 4215 haalden 2x de startkoers, 3215 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 987 tokens. Houdercheck echt uitgevoerd bij 86% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1137, winkans 22%, EV per trade -6.6% (95%-marge -8.6% tot -4.6%), mediaan -10.1%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2066, winkans 23%, EV -7.6% (95%-marge -9.8% tot -5.3%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 3215 | 39% | 76% | 0% |
| schoon | 2555 | 41% | 76% | 0% |
| bundelgrafiek | 660 | 29% | 77% | 0% |
| schoon+houders_ok | 1137 | 39% | 78% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.5% (3286, 23% win) | -7.3% (3215, 22% win) | -7.6% (3146, 22% win) | -6.4% (2597, 27% win) |
| schoon | -7.0% (2619, 24% win) | -6.9% (2555, 24% win) | -6.9% (2504, 23% win) | -5.8% (2166, 28% win) |
| bundelgrafiek | -9.2% (667, 17% win) | -8.7% (660, 16% win) | -10.2% (642, 14% win) | -9.6% (431, 22% win) |
| schoon+houders_ok | -7.1% (1085, 21% win) | -6.6% (1137, 22% win) | -6.4% (1200, 22% win) | -3.8% (953, 25% win) |
| schoon+houders_ok+final_stretch | -8.0% (424, 13% win) | -8.7% (437, 12% win) | -8.6% (445, 11% win) | -5.9% (342, 16% win) |
| volledige_screening+schoon | -9.1% (258, 13% win) | -10.3% (264, 11% win) | -10.1% (263, 9% win) | -8.0% (195, 14% win) |
| volledige_screening+schoon+x_link | -9.5% (202, 14% win) | -10.6% (205, 10% win) | -10.2% (201, 8% win) | -8.9% (143, 12% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.3% (3215, 22% win) | -6.9% (3215, 22% win) | -7.3% (3215, 21% win) |
| schoon | -6.9% (2555, 24% win) | -6.7% (2555, 24% win) | -6.7% (2555, 23% win) |
| bundelgrafiek | -8.7% (660, 16% win) | -7.8% (660, 16% win) | -9.9% (660, 14% win) |
| schoon+houders_ok | -6.6% (1137, 22% win) | -6.2% (1137, 21% win) | -5.4% (1137, 22% win) |
| schoon+houders_ok+final_stretch | -8.7% (437, 12% win) | -7.2% (437, 12% win) | -9.1% (437, 14% win) |
| volledige_screening+schoon | -10.3% (264, 11% win) | -8.6% (264, 10% win) | -10.7% (264, 14% win) |
| volledige_screening+schoon+x_link | -10.6% (205, 10% win) | -8.8% (205, 9% win) | -11.2% (205, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (1315, 29% win); 1,3–2x: -8.2% (1240, 18% win); ≥ 2x (bundelgrafiek): -8.7% (660, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.4% (2039, 28% win); 5–20%: -9.1% (599, 12% win); ≥ 20%: -8.6% (577, 10% win)

**top t.o.v. start:** 2–3x: -7.1% (1791, 21% win); 3–6x: -6.7% (1109, 24% win); ≥ 6x: -10.2% (315, 22% win)

**unieke kopers tot de top:** < 30: -6.2% (2039, 29% win); 30–100: -8.1% (631, 10% win); ≥ 100: -10.4% (545, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.1% (816, 15% win); 1–2: -6.5% (1517, 24% win); ≥ 3 (trap): -7.9% (882, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.9% (810, 11% win); 10–25%: -7.1% (497, 12% win); ≥ 25%: -6.2% (1908, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.9% (2584, 24% win); 30 s–3 min: -8.5% (507, 16% win); ≥ 3 min (langzaam): -10.1% (124, 6% win)

**tijd van start tot top:** < 2 min: -6.9% (2688, 24% win); 2–10 min: -9.4% (416, 15% win); ≥ 10 min: -8.6% (111, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
