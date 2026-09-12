# Videostrategie op alle trades — 2026-09-12 06:00 UTC

Tokens sinds 2026-09-11 08:47 UTC: 17903 geschikt (≥ 2 uur oud, geen herstart), 15164 met trades, 3168 haalden 2x de startkoers, 2440 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 715 tokens. Houdercheck echt uitgevoerd bij 81% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 848, winkans 21%, EV per trade -6.8% (95%-marge -9.0% tot -4.5%), mediaan -9.9%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 1459, winkans 22%, EV -6.9% (95%-marge -9.7% tot -4.0%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 2440 | 38% | 76% | 0% |
| schoon | 1948 | 40% | 76% | 0% |
| bundelgrafiek | 492 | 28% | 77% | 0% |
| schoon+houders_ok | 848 | 38% | 78% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.5% (2496, 22% win) | -7.3% (2440, 22% win) | -7.9% (2392, 21% win) | -6.1% (1926, 27% win) |
| schoon | -7.1% (1998, 23% win) | -6.8% (1948, 24% win) | -7.2% (1915, 22% win) | -5.6% (1611, 28% win) |
| bundelgrafiek | -9.5% (498, 17% win) | -9.3% (492, 16% win) | -10.9% (477, 14% win) | -8.9% (315, 22% win) |
| schoon+houders_ok | -6.9% (809, 20% win) | -6.8% (848, 21% win) | -6.8% (900, 20% win) | -3.0% (683, 25% win) |
| schoon+houders_ok+final_stretch | -9.1% (324, 12% win) | -9.8% (334, 11% win) | -9.1% (344, 10% win) | -6.8% (247, 15% win) |
| volledige_screening+schoon | -10.7% (191, 12% win) | -11.6% (197, 9% win) | -10.5% (200, 9% win) | -8.8% (134, 15% win) |
| volledige_screening+schoon+x_link | -10.6% (149, 13% win) | -11.8% (151, 9% win) | -10.6% (151, 8% win) | -10.1% (94, 13% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.3% (2440, 22% win) | -6.9% (2440, 22% win) | -6.7% (2440, 21% win) |
| schoon | -6.8% (1948, 24% win) | -6.5% (1948, 23% win) | -5.9% (1948, 23% win) |
| bundelgrafiek | -9.3% (492, 16% win) | -8.4% (492, 16% win) | -10.2% (492, 14% win) |
| schoon+houders_ok | -6.8% (848, 21% win) | -6.2% (848, 21% win) | -4.9% (848, 21% win) |
| schoon+houders_ok+final_stretch | -9.8% (334, 11% win) | -8.4% (334, 10% win) | -9.8% (334, 13% win) |
| volledige_screening+schoon | -11.6% (197, 9% win) | -10.1% (197, 8% win) | -11.6% (197, 13% win) |
| volledige_screening+schoon+x_link | -11.8% (151, 9% win) | -10.4% (151, 7% win) | -12.5% (151, 11% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.2% (952, 30% win); 1,3–2x: -8.3% (996, 17% win); ≥ 2x (bundelgrafiek): -9.3% (492, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.1% (1476, 30% win); 5–20%: -9.6% (500, 11% win); ≥ 20%: -8.6% (464, 11% win)

**top t.o.v. start:** 2–3x: -7.1% (1375, 21% win); 3–6x: -7.1% (831, 24% win); ≥ 6x: -9.1% (234, 24% win)

**unieke kopers tot de top:** < 30: -5.8% (1492, 30% win); 30–100: -8.1% (523, 9% win); ≥ 100: -11.4% (425, 11% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -9.0% (637, 14% win); 1–2: -6.1% (1171, 25% win); ≥ 3 (trap): -7.8% (632, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -10.5% (664, 10% win); 10–25%: -7.3% (409, 12% win); ≥ 25%: -5.8% (1367, 31% win)

**duur van top naar dip:** < 30 s (crash): -6.8% (1959, 24% win); 30 s–3 min: -8.8% (390, 16% win); ≥ 3 min (langzaam): -12.0% (91, 4% win)

**tijd van start tot top:** < 2 min: -6.5% (2048, 24% win); 2–10 min: -12.0% (310, 13% win); ≥ 10 min: -10.8% (82, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
