# Videostrategie op alle trades — 2026-09-12 01:53 UTC

Tokens sinds 2026-09-11 08:47 UTC: 13263 geschikt (≥ 2 uur oud, geen herstart), 11080 met trades, 2356 haalden 2x de startkoers, 1804 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 549 tokens. Houdercheck echt uitgevoerd bij 74% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 606, winkans 20%, EV per trade -7.8% (95%-marge -10.3% tot -5.3%), mediaan -10.0%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 929, winkans 22%, EV -7.8% (95%-marge -11.3% tot -4.4%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 1804 | 37% | 77% | 0% |
| schoon | 1418 | 40% | 77% | 0% |
| bundelgrafiek | 386 | 27% | 78% | 0% |
| schoon+houders_ok | 606 | 37% | 79% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.7% (1846, 22% win) | -7.8% (1804, 22% win) | -8.8% (1772, 20% win) | -7.3% (1418, 26% win) |
| schoon | -7.5% (1456, 23% win) | -7.4% (1418, 23% win) | -8.0% (1394, 22% win) | -7.1% (1174, 26% win) |
| bundelgrafiek | -8.7% (390, 19% win) | -9.5% (386, 17% win) | -11.8% (378, 14% win) | -8.4% (244, 23% win) |
| schoon+houders_ok | -7.9% (583, 19% win) | -7.8% (606, 20% win) | -7.8% (645, 19% win) | -5.1% (480, 24% win) |
| schoon+houders_ok+final_stretch | -9.7% (231, 12% win) | -10.3% (238, 10% win) | -9.2% (244, 9% win) | -8.3% (167, 15% win) |
| volledige_screening+schoon | -10.6% (150, 12% win) | -12.0% (155, 8% win) | -10.6% (157, 9% win) | -9.2% (101, 17% win) |
| volledige_screening+schoon+x_link | -10.2% (115, 15% win) | -11.9% (116, 9% win) | -10.8% (116, 8% win) | -9.9% (68, 16% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.8% (1804, 22% win) | -7.2% (1804, 22% win) | -7.4% (1804, 21% win) |
| schoon | -7.4% (1418, 23% win) | -6.8% (1418, 23% win) | -6.1% (1418, 23% win) |
| bundelgrafiek | -9.5% (386, 17% win) | -8.4% (386, 17% win) | -12.3% (386, 14% win) |
| schoon+houders_ok | -7.8% (606, 20% win) | -7.1% (606, 20% win) | -5.4% (606, 21% win) |
| schoon+houders_ok+final_stretch | -10.3% (238, 10% win) | -8.7% (238, 11% win) | -9.7% (238, 13% win) |
| volledige_screening+schoon | -12.0% (155, 8% win) | -10.5% (155, 10% win) | -11.3% (155, 13% win) |
| volledige_screening+schoon+x_link | -11.9% (116, 9% win) | -10.7% (116, 10% win) | -12.0% (116, 10% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -6.0% (690, 29% win); 1,3–2x: -8.6% (728, 17% win); ≥ 2x (bundelgrafiek): -9.5% (386, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -7.0% (1084, 28% win); 5–20%: -9.5% (368, 12% win); ≥ 20%: -8.5% (352, 12% win)

**top t.o.v. start:** 2–3x: -7.5% (991, 20% win); 3–6x: -6.9% (631, 25% win); ≥ 6x: -12.9% (182, 20% win)

**unieke kopers tot de top:** < 30: -6.6% (1085, 29% win); 30–100: -7.8% (373, 10% win); ≥ 100: -11.7% (346, 11% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -9.6% (494, 14% win); 1–2: -6.2% (849, 25% win); ≥ 3 (trap): -9.0% (461, 24% win)

**grootste koper, aandeel koopvolume:** < 10%: -10.2% (508, 11% win); 10–25%: -7.7% (287, 12% win); ≥ 25%: -6.7% (1009, 30% win)

**duur van top naar dip:** < 30 s (crash): -7.4% (1454, 24% win); 30 s–3 min: -8.9% (283, 15% win); ≥ 3 min (langzaam): -11.7% (67, 6% win)

**tijd van start tot top:** < 2 min: -7.0% (1484, 24% win); 2–10 min: -11.9% (252, 13% win); ≥ 10 min: -11.2% (68, 13% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
