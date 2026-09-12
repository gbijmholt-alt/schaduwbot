# Videostrategie op alle trades — 2026-09-12 16:32 UTC

Tokens sinds 2026-09-11 08:47 UTC: 23475 geschikt (≥ 2 uur oud, geen herstart), 19998 met trades, 4063 haalden 2x de startkoers, 3103 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 943 tokens. Houdercheck echt uitgevoerd bij 85% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1097, winkans 22%, EV per trade -6.6% (95%-marge -8.6% tot -4.6%), mediaan -10.1%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 1980, winkans 23%, EV -7.3% (95%-marge -9.6% tot -5.0%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 3103 | 38% | 76% | 0% |
| schoon | 2469 | 41% | 76% | 0% |
| bundelgrafiek | 634 | 29% | 77% | 0% |
| schoon+houders_ok | 1097 | 39% | 79% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.6% (3173, 22% win) | -7.3% (3103, 22% win) | -7.6% (3037, 22% win) | -6.2% (2507, 27% win) |
| schoon | -7.1% (2532, 24% win) | -6.9% (2469, 24% win) | -6.9% (2421, 23% win) | -5.5% (2092, 28% win) |
| bundelgrafiek | -9.4% (641, 18% win) | -9.2% (634, 16% win) | -10.5% (616, 14% win) | -9.7% (415, 22% win) |
| schoon+houders_ok | -7.1% (1046, 20% win) | -6.6% (1097, 22% win) | -6.3% (1157, 21% win) | -3.6% (919, 25% win) |
| schoon+houders_ok+final_stretch | -7.9% (415, 13% win) | -8.6% (428, 13% win) | -8.5% (435, 11% win) | -5.7% (333, 16% win) |
| volledige_screening+schoon | -9.0% (250, 13% win) | -10.2% (256, 11% win) | -10.1% (255, 9% win) | -7.7% (187, 14% win) |
| volledige_screening+schoon+x_link | -9.4% (194, 14% win) | -10.4% (197, 11% win) | -10.2% (193, 8% win) | -8.6% (135, 13% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.3% (3103, 22% win) | -7.0% (3103, 22% win) | -7.2% (3103, 22% win) |
| schoon | -6.9% (2469, 24% win) | -6.7% (2469, 24% win) | -6.4% (2469, 24% win) |
| bundelgrafiek | -9.2% (634, 16% win) | -8.2% (634, 16% win) | -10.4% (634, 14% win) |
| schoon+houders_ok | -6.6% (1097, 22% win) | -6.2% (1097, 21% win) | -5.1% (1097, 22% win) |
| schoon+houders_ok+final_stretch | -8.6% (428, 13% win) | -7.1% (428, 12% win) | -9.0% (428, 14% win) |
| volledige_screening+schoon | -10.2% (256, 11% win) | -8.5% (256, 10% win) | -10.5% (256, 14% win) |
| volledige_screening+schoon+x_link | -10.4% (197, 11% win) | -8.6% (197, 10% win) | -11.0% (197, 13% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.7% (1255, 30% win); 1,3–2x: -8.1% (1214, 18% win); ≥ 2x (bundelgrafiek): -9.2% (634, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.5% (1951, 29% win); 5–20%: -9.2% (593, 12% win); ≥ 20%: -8.4% (559, 11% win)

**top t.o.v. start:** 2–3x: -7.1% (1725, 21% win); 3–6x: -6.9% (1072, 24% win); ≥ 6x: -10.3% (306, 22% win)

**unieke kopers tot de top:** < 30: -6.3% (1957, 29% win); 30–100: -8.1% (614, 10% win); ≥ 100: -10.4% (532, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.4% (787, 15% win); 1–2: -6.6% (1469, 24% win); ≥ 3 (trap): -7.7% (847, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.9% (796, 11% win); 10–25%: -7.1% (486, 12% win); ≥ 25%: -6.3% (1821, 30% win)

**duur van top naar dip:** < 30 s (crash): -7.0% (2492, 24% win); 30 s–3 min: -8.6% (491, 16% win); ≥ 3 min (langzaam): -9.9% (120, 7% win)

**tijd van start tot top:** < 2 min: -6.9% (2592, 24% win); 2–10 min: -9.6% (401, 15% win); ≥ 10 min: -9.2% (110, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
