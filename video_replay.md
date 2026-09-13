# Videostrategie op alle trades — 2026-09-13 01:38 UTC

Tokens sinds 2026-09-11 08:47 UTC: 29103 geschikt (≥ 2 uur oud, geen herstart), 23902 met trades, 4735 haalden 2x de startkoers, 3615 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 1108 tokens. Houdercheck echt uitgevoerd bij 87% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1185, winkans 21%, EV per trade -6.7% (95%-marge -8.6% tot -4.8%), mediaan -10.2%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 2378, winkans 23%, EV -6.8% (95%-marge -9.1% tot -4.6%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 3615 | 40% | 76% | 0% |
| schoon | 2867 | 42% | 76% | 0% |
| bundelgrafiek | 748 | 29% | 77% | 0% |
| schoon+houders_ok | 1185 | 38% | 79% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.3% (3699, 23% win) | -7.1% (3615, 22% win) | -7.4% (3530, 22% win) | -6.5% (2940, 27% win) |
| schoon | -6.9% (2942, 24% win) | -6.8% (2867, 24% win) | -6.9% (2804, 23% win) | -6.0% (2444, 28% win) |
| bundelgrafiek | -8.7% (757, 17% win) | -8.3% (748, 16% win) | -9.4% (726, 15% win) | -9.1% (496, 22% win) |
| schoon+houders_ok | -7.1% (1127, 20% win) | -6.7% (1185, 21% win) | -6.5% (1253, 21% win) | -3.9% (988, 24% win) |
| schoon+houders_ok+final_stretch | -8.0% (445, 13% win) | -8.6% (463, 12% win) | -8.6% (475, 10% win) | -5.8% (359, 15% win) |
| volledige_screening+schoon | -8.7% (272, 14% win) | -10.0% (282, 11% win) | -10.0% (284, 9% win) | -7.9% (207, 14% win) |
| volledige_screening+schoon+x_link | -9.1% (213, 15% win) | -10.3% (217, 11% win) | -10.2% (212, 8% win) | -8.7% (152, 12% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.1% (3615, 22% win) | -6.7% (3615, 22% win) | -6.8% (3615, 22% win) |
| schoon | -6.8% (2867, 24% win) | -6.5% (2867, 24% win) | -6.2% (2867, 24% win) |
| bundelgrafiek | -8.3% (748, 16% win) | -7.3% (748, 16% win) | -9.2% (748, 15% win) |
| schoon+houders_ok | -6.7% (1185, 21% win) | -6.3% (1185, 21% win) | -5.8% (1185, 21% win) |
| schoon+houders_ok+final_stretch | -8.6% (463, 12% win) | -7.4% (463, 11% win) | -9.3% (463, 14% win) |
| volledige_screening+schoon | -10.0% (282, 11% win) | -8.7% (282, 10% win) | -10.8% (282, 14% win) |
| volledige_screening+schoon+x_link | -10.3% (217, 11% win) | -8.9% (217, 9% win) | -11.3% (217, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.6% (1509, 29% win); 1,3–2x: -8.0% (1358, 18% win); ≥ 2x (bundelgrafiek): -8.3% (748, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.3% (2327, 28% win); 5–20%: -8.7% (641, 13% win); ≥ 20%: -8.2% (647, 10% win)

**top t.o.v. start:** 2–3x: -7.0% (2021, 21% win); 3–6x: -6.8% (1239, 24% win); ≥ 6x: -8.6% (355, 22% win)

**unieke kopers tot de top:** < 30: -6.1% (2322, 29% win); 30–100: -7.6% (697, 10% win); ≥ 100: -10.2% (596, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.1% (913, 15% win); 1–2: -6.4% (1723, 24% win); ≥ 3 (trap): -7.3% (979, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.7% (881, 11% win); 10–25%: -7.0% (550, 12% win); ≥ 25%: -6.0% (2184, 29% win)

**duur van top naar dip:** < 30 s (crash): -6.7% (2903, 24% win); 30 s–3 min: -8.5% (562, 16% win); ≥ 3 min (langzaam): -9.3% (150, 7% win)

**tijd van start tot top:** < 2 min: -6.7% (3018, 24% win); 2–10 min: -8.6% (472, 15% win); ≥ 10 min: -8.9% (125, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
