# Videostrategie op alle trades — 2026-09-12 14:30 UTC

Tokens sinds 2026-09-11 08:47 UTC: 21459 geschikt (≥ 2 uur oud, geen herstart), 18219 met trades, 3737 haalden 2x de startkoers, 2852 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 847 tokens. Houdercheck echt uitgevoerd bij 84% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 1001, winkans 21%, EV per trade -7.0% (95%-marge -9.1% tot -5.0%), mediaan -10.2%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 1789, winkans 23%, EV -7.0% (95%-marge -9.5% tot -4.5%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 2852 | 38% | 76% | 0% |
| schoon | 2278 | 41% | 76% | 0% |
| bundelgrafiek | 574 | 29% | 77% | 0% |
| schoon+houders_ok | 1001 | 38% | 79% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.6% (2915, 22% win) | -7.3% (2852, 22% win) | -7.8% (2789, 21% win) | -5.9% (2290, 27% win) |
| schoon | -7.1% (2335, 24% win) | -6.8% (2278, 24% win) | -7.1% (2233, 23% win) | -5.3% (1913, 28% win) |
| bundelgrafiek | -9.6% (580, 18% win) | -9.2% (574, 16% win) | -10.4% (556, 15% win) | -9.1% (377, 22% win) |
| schoon+houders_ok | -7.1% (954, 20% win) | -7.0% (1001, 21% win) | -7.1% (1058, 20% win) | -3.4% (825, 25% win) |
| schoon+houders_ok+final_stretch | -8.6% (385, 12% win) | -8.7% (397, 13% win) | -8.8% (405, 10% win) | -6.0% (303, 16% win) |
| volledige_screening+schoon | -9.9% (230, 12% win) | -10.3% (236, 11% win) | -10.4% (236, 9% win) | -7.9% (167, 15% win) |
| volledige_screening+schoon+x_link | -10.0% (181, 14% win) | -10.5% (184, 11% win) | -10.6% (182, 8% win) | -8.7% (122, 13% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.3% (2852, 22% win) | -6.9% (2852, 22% win) | -6.9% (2852, 22% win) |
| schoon | -6.8% (2278, 24% win) | -6.5% (2278, 24% win) | -6.1% (2278, 23% win) |
| bundelgrafiek | -9.2% (574, 16% win) | -8.3% (574, 16% win) | -9.9% (574, 14% win) |
| schoon+houders_ok | -7.0% (1001, 21% win) | -6.6% (1001, 21% win) | -5.2% (1001, 22% win) |
| schoon+houders_ok+final_stretch | -8.7% (397, 13% win) | -7.3% (397, 12% win) | -9.1% (397, 14% win) |
| volledige_screening+schoon | -10.3% (236, 11% win) | -8.7% (236, 10% win) | -10.5% (236, 15% win) |
| volledige_screening+schoon+x_link | -10.5% (184, 11% win) | -9.0% (184, 9% win) | -11.2% (184, 12% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -5.5% (1137, 30% win); 1,3–2x: -8.0% (1141, 18% win); ≥ 2x (bundelgrafiek): -9.2% (574, 16% win)

**aandeel supply gekocht in creatieblok:** < 5%: -6.2% (1768, 29% win); 5–20%: -9.2% (565, 12% win); ≥ 20%: -8.7% (519, 10% win)

**top t.o.v. start:** 2–3x: -7.0% (1601, 21% win); 3–6x: -6.9% (973, 24% win); ≥ 6x: -10.0% (278, 23% win)

**unieke kopers tot de top:** < 30: -6.1% (1778, 29% win); 30–100: -8.1% (581, 10% win); ≥ 100: -10.4% (493, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.8% (720, 14% win); 1–2: -6.3% (1366, 25% win); ≥ 3 (trap): -7.6% (766, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -9.9% (758, 11% win); 10–25%: -7.4% (452, 12% win); ≥ 25%: -6.0% (1642, 30% win)

**duur van top naar dip:** < 30 s (crash): -6.8% (2286, 24% win); 30 s–3 min: -8.6% (457, 16% win); ≥ 3 min (langzaam): -11.2% (109, 6% win)

**tijd van start tot top:** < 2 min: -6.7% (2385, 24% win); 2–10 min: -10.6% (363, 14% win); ≥ 10 min: -8.9% (104, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
