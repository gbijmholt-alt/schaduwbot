# Videostrategie op alle trades — 2026-09-12 17:14 UTC

Tokens sinds 2026-09-11 08:47 UTC: 24351 geschikt (≥ 2 uur oud, geen herstart), 20774 met trades, 4202 haalden 2x de startkoers, 3204 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 985 tokens. Houdercheck echt uitgevoerd bij 86% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1135, winkans 22%, EV per trade -6.6% (95%-marge -8.6% tot -4.6%), mediaan -10.1%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2056, winkans 23%, EV -7.5% (95%-marge -9.8% tot -5.3%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 3204 | 39% | 76% | 0% |
| schoon | 2545 | 41% | 76% | 0% |
| bundelgrafiek | 659 | 29% | 77% | 0% |
| schoon+houders_ok | 1135 | 39% | 78% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.5% (3275, 22% win) | -7.3% (3204, 22% win) | -7.6% (3135, 22% win) | -6.4% (2589, 27% win) |
| schoon | -7.1% (2609, 24% win) | -6.9% (2545, 24% win) | -6.9% (2494, 23% win) | -5.8% (2159, 28% win) |
| bundelgrafiek | -9.2% (666, 17% win) | -8.7% (659, 16% win) | -10.2% (641, 14% win) | -9.6% (430, 22% win) |
| schoon+houders_ok | -7.0% (1083, 21% win) | -6.6% (1135, 22% win) | -6.4% (1198, 22% win) | -3.9% (951, 25% win) |
| schoon+houders_ok+final_stretch | -8.0% (423, 13% win) | -8.7% (436, 12% win) | -8.6% (444, 10% win) | -5.9% (341, 16% win) |
| volledige_screening+schoon | -9.1% (257, 13% win) | -10.3% (263, 11% win) | -10.2% (262, 9% win) | -8.0% (194, 14% win) |
| volledige_screening+schoon+x_link | -9.5% (201, 14% win) | -10.5% (204, 10% win) | -10.3% (200, 8% win) | -8.9% (142, 12% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.3% (3204, 22% win) | -6.9% (3204, 22% win) | -7.3% (3204, 21% win) |
| schoon | -6.9% (2545, 24% win) | -6.7% (2545, 24% win) | -6.6% (2545, 23% win) |
| bundelgrafiek | -8.7% (659, 16% win) | -7.8% (659, 16% win) | -9.9% (659, 14% win) |
| schoon+houders_ok | -6.6% (1135, 22% win) | -6.2% (1135, 21% win) | -5.4% (1135, 22% win) |
| schoon+houders_ok+final_stretch | -8.7% (436, 12% win) | -7.2% (436, 12% win) | -9.1% (436, 14% win) |
| volledige_screening+schoon | -10.3% (263, 11% win) | -8.6% (263, 10% win) | -10.7% (263, 14% win) |
| volledige_screening+schoon+x_link | -10.5% (204, 10% win) | -8.7% (204, 9% win) | -11.2% (204, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.8% (1309, 29% win); 1,3–2x: -8.1% (1236, 18% win); ≥ 2x (bundelgrafiek): -8.7% (659, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.4% (2029, 28% win); 5–20%: -9.1% (598, 12% win); ≥ 20%: -8.6% (577, 10% win)

**top t.o.v. start:** 2–3x: -7.1% (1781, 21% win); 3–6x: -6.7% (1109, 24% win); ≥ 6x: -10.2% (314, 22% win)

**unieke kopers tot de top:** < 30: -6.2% (2031, 29% win); 30–100: -8.2% (629, 10% win); ≥ 100: -10.4% (544, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.2% (813, 15% win); 1–2: -6.4% (1513, 24% win); ≥ 3 (trap): -8.0% (878, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.9% (808, 11% win); 10–25%: -7.2% (496, 12% win); ≥ 25%: -6.2% (1900, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.9% (2576, 24% win); 30 s–3 min: -8.4% (505, 16% win); ≥ 3 min (langzaam): -10.0% (123, 6% win)

**tijd van start tot top:** < 2 min: -6.9% (2680, 24% win); 2–10 min: -9.4% (414, 15% win); ≥ 10 min: -9.2% (110, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
