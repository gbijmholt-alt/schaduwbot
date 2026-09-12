# Videostrategie op alle trades — 2026-09-12 19:28 UTC

Tokens sinds 2026-09-11 08:47 UTC: 24674 geschikt (≥ 2 uur oud, geen herstart), 20970 met trades, 4233 haalden 2x de startkoers, 3230 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 992 tokens. Houdercheck echt uitgevoerd bij 86% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1143, winkans 21%, EV per trade -6.7% (95%-marge -8.6% tot -4.7%), mediaan -10.2%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2077, winkans 23%, EV -7.6% (95%-marge -9.8% tot -5.4%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 3230 | 39% | 76% | 0% |
| schoon | 2566 | 41% | 76% | 0% |
| bundelgrafiek | 664 | 29% | 77% | 0% |
| schoon+houders_ok | 1143 | 39% | 79% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.5% (3301, 22% win) | -7.4% (3230, 22% win) | -7.7% (3161, 22% win) | -6.4% (2612, 27% win) |
| schoon | -7.1% (2630, 24% win) | -7.0% (2566, 24% win) | -7.0% (2515, 23% win) | -5.8% (2177, 28% win) |
| bundelgrafiek | -9.3% (671, 17% win) | -8.9% (664, 16% win) | -10.3% (646, 14% win) | -9.8% (435, 22% win) |
| schoon+houders_ok | -7.1% (1091, 20% win) | -6.7% (1143, 21% win) | -6.5% (1206, 22% win) | -3.9% (959, 25% win) |
| schoon+houders_ok+final_stretch | -8.1% (426, 13% win) | -8.8% (439, 12% win) | -8.6% (447, 10% win) | -6.0% (344, 15% win) |
| volledige_screening+schoon | -9.2% (259, 13% win) | -10.4% (265, 11% win) | -10.2% (264, 9% win) | -8.1% (196, 14% win) |
| volledige_screening+schoon+x_link | -9.5% (203, 14% win) | -10.6% (206, 10% win) | -10.2% (202, 8% win) | -9.0% (144, 12% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.4% (3230, 22% win) | -7.0% (3230, 22% win) | -7.4% (3230, 21% win) |
| schoon | -7.0% (2566, 24% win) | -6.7% (2566, 24% win) | -6.7% (2566, 23% win) |
| bundelgrafiek | -8.9% (664, 16% win) | -7.9% (664, 16% win) | -10.1% (664, 14% win) |
| schoon+houders_ok | -6.7% (1143, 21% win) | -6.3% (1143, 21% win) | -5.5% (1143, 22% win) |
| schoon+houders_ok+final_stretch | -8.8% (439, 12% win) | -7.2% (439, 12% win) | -9.2% (439, 14% win) |
| volledige_screening+schoon | -10.4% (265, 11% win) | -8.6% (265, 10% win) | -10.8% (265, 14% win) |
| volledige_screening+schoon+x_link | -10.6% (206, 10% win) | -8.8% (206, 9% win) | -11.3% (206, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.8% (1324, 29% win); 1,3–2x: -8.2% (1242, 18% win); ≥ 2x (bundelgrafiek): -8.9% (664, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.5% (2049, 28% win); 5–20%: -9.1% (601, 12% win); ≥ 20%: -8.7% (580, 10% win)

**top t.o.v. start:** 2–3x: -7.2% (1799, 21% win); 3–6x: -6.8% (1115, 24% win); ≥ 6x: -10.3% (316, 22% win)

**unieke kopers tot de top:** < 30: -6.3% (2050, 29% win); 30–100: -8.2% (634, 10% win); ≥ 100: -10.4% (546, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.2% (819, 15% win); 1–2: -6.5% (1522, 24% win); ≥ 3 (trap): -8.0% (889, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.9% (810, 11% win); 10–25%: -7.3% (502, 12% win); ≥ 25%: -6.3% (1918, 30% win)

**duur van top naar dip:** < 30 s (crash): -7.0% (2596, 24% win); 30 s–3 min: -8.5% (510, 16% win); ≥ 3 min (langzaam): -10.1% (124, 6% win)

**tijd van start tot top:** < 2 min: -7.0% (2702, 24% win); 2–10 min: -9.4% (417, 15% win); ≥ 10 min: -8.6% (111, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
