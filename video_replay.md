# Videostrategie op alle trades — 2026-09-13 03:46 UTC

Tokens sinds 2026-09-11 08:47 UTC: 31549 geschikt (≥ 2 uur oud, geen herstart), 25652 met trades, 5028 haalden 2x de startkoers, 3834 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1171 tokens. Houdercheck echt uitgevoerd bij 87% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1202, winkans 21%, EV per trade -6.9% (95%-marge -8.8% tot -5.0%), mediaan -10.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2557, winkans 23%, EV -7.1% (95%-marge -9.2% tot -5.0%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 3834 | 40% | 76% | 0% |
| schoon | 3046 | 42% | 76% | 0% |
| bundelgrafiek | 788 | 29% | 77% | 0% |
| schoon+houders_ok | 1202 | 38% | 79% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.2% (3928, 23% win) | -7.0% (3834, 22% win) | -7.5% (3743, 22% win) | -6.8% (3133, 27% win) |
| schoon | -6.8% (3129, 24% win) | -6.8% (3046, 24% win) | -7.0% (2977, 23% win) | -6.3% (2605, 27% win) |
| bundelgrafiek | -8.6% (799, 17% win) | -8.0% (788, 16% win) | -9.2% (766, 15% win) | -9.4% (528, 22% win) |
| schoon+houders_ok | -7.2% (1141, 20% win) | -6.9% (1202, 21% win) | -6.6% (1273, 21% win) | -4.0% (1000, 24% win) |
| schoon+houders_ok+final_stretch | -8.1% (455, 13% win) | -8.8% (474, 12% win) | -8.7% (489, 10% win) | -5.9% (366, 15% win) |
| volledige_screening+schoon | -8.8% (278, 13% win) | -10.1% (288, 11% win) | -10.0% (292, 9% win) | -7.9% (210, 13% win) |
| volledige_screening+schoon+x_link | -9.1% (217, 14% win) | -10.4% (221, 10% win) | -10.2% (218, 9% win) | -8.8% (155, 12% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.0% (3834, 22% win) | -6.7% (3834, 22% win) | -6.9% (3834, 22% win) |
| schoon | -6.8% (3046, 24% win) | -6.6% (3046, 24% win) | -6.4% (3046, 24% win) |
| bundelgrafiek | -8.0% (788, 16% win) | -7.1% (788, 16% win) | -8.8% (788, 15% win) |
| schoon+houders_ok | -6.9% (1202, 21% win) | -6.5% (1202, 20% win) | -6.0% (1202, 21% win) |
| schoon+houders_ok+final_stretch | -8.8% (474, 12% win) | -7.5% (474, 11% win) | -9.7% (474, 14% win) |
| volledige_screening+schoon | -10.1% (288, 11% win) | -8.8% (288, 9% win) | -11.1% (288, 14% win) |
| volledige_screening+schoon+x_link | -10.4% (221, 10% win) | -9.0% (221, 9% win) | -11.5% (221, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (1619, 29% win); 1,3–2x: -8.0% (1427, 18% win); ≥ 2x (bundelgrafiek): -8.0% (788, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.2% (2476, 29% win); 5–20%: -8.7% (681, 13% win); ≥ 20%: -8.3% (677, 10% win)

**top t.o.v. start:** 2–3x: -6.8% (2150, 22% win); 3–6x: -7.0% (1309, 24% win); ≥ 6x: -8.7% (375, 22% win)

**unieke kopers tot de top:** < 30: -6.0% (2473, 29% win); 30–100: -7.7% (744, 11% win); ≥ 100: -10.3% (617, 11% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.0% (968, 16% win); 1–2: -6.3% (1828, 25% win); ≥ 3 (trap): -7.4% (1038, 25% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.8% (924, 11% win); 10–25%: -6.8% (588, 13% win); ≥ 25%: -6.0% (2322, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.6% (3077, 25% win); 30 s–3 min: -8.6% (599, 15% win); ≥ 3 min (langzaam): -9.6% (158, 7% win)

**tijd van start tot top:** < 2 min: -6.8% (3199, 24% win); 2–10 min: -8.3% (505, 15% win); ≥ 10 min: -8.7% (130, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
