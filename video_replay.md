# Videostrategie op alle trades — 2026-09-11 21:43 UTC

Tokens sinds 2026-09-11 08:47 UTC: 7631 geschikt (≥ 2 uur oud, geen herstart), 6168 met trades, 1245 haalden 2x de startkoers, 910 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 315 tokens. Houdercheck echt uitgevoerd bij 50% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 253, winkans 21%, EV per trade -5.9% (95%-marge -9.7% tot -2.1%), mediaan -9.2%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 215, winkans 20%, EV -9.5% (95%-marge -15.2% tot -3.7%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 910 | 37% | 78% | 0% |
| schoon | 704 | 40% | 78% | 0% |
| bundelgrafiek | 206 | 27% | 77% | 0% |
| schoon+houders_ok | 253 | 38% | 80% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -6.0% (934, 24% win) | -5.4% (910, 24% win) | -7.9% (891, 20% win) | -6.8% (719, 26% win) |
| schoon | -5.5% (726, 25% win) | -5.2% (704, 25% win) | -7.1% (692, 22% win) | -7.2% (579, 26% win) |
| bundelgrafiek | -7.6% (208, 19% win) | -6.2% (206, 21% win) | -10.8% (199, 16% win) | -5.0% (140, 26% win) |
| schoon+houders_ok | -5.8% (247, 19% win) | -5.9% (253, 21% win) | -7.6% (269, 18% win) | -4.1% (192, 23% win) |
| schoon+houders_ok+final_stretch | -8.2% (79, 8% win) | -8.6% (80, 6% win) | -9.2% (79, 4% win) | -7.1% (50, 12% win) |
| volledige_screening+schoon | -8.2% (61, 10% win) | -9.0% (62, 6% win) | -10.5% (61, 3% win) | -5.6% (38, 16% win) |
| volledige_screening+schoon+x_link | -7.2% (52, 12% win) | -8.6% (53, 6% win) | -11.1% (52, 2% win) | -4.7% (29, 17% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -5.4% (910, 24% win) | -4.7% (910, 23% win) | -5.8% (910, 22% win) |
| schoon | -5.2% (704, 25% win) | -4.6% (704, 24% win) | -4.9% (704, 23% win) |
| bundelgrafiek | -6.2% (206, 21% win) | -5.0% (206, 20% win) | -8.8% (206, 16% win) |
| schoon+houders_ok | -5.9% (253, 21% win) | -5.6% (253, 21% win) | -7.4% (253, 21% win) |
| schoon+houders_ok+final_stretch | -8.6% (80, 6% win) | -7.0% (80, 5% win) | -10.6% (80, 9% win) |
| volledige_screening+schoon | -9.0% (62, 6% win) | -7.9% (62, 5% win) | -12.0% (62, 10% win) |
| volledige_screening+schoon+x_link | -8.6% (53, 6% win) | -7.5% (53, 6% win) | -12.4% (53, 6% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -2.8% (338, 31% win); 1,3–2x: -7.4% (366, 18% win); ≥ 2x (bundelgrafiek): -6.2% (206, 21% win)

**aandeel supply gekocht in creatieblok:** < 5%: -3.6% (558, 31% win); 5–20%: -9.5% (171, 11% win); ≥ 20%: -7.2% (181, 12% win)

**top t.o.v. start:** 2–3x: -5.6% (500, 22% win); 3–6x: -3.5% (318, 28% win); ≥ 6x: -11.3% (92, 21% win)

**unieke kopers tot de top:** < 30: -3.7% (586, 31% win); 30–100: -7.4% (133, 10% win); ≥ 100: -9.3% (191, 11% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -8.3% (259, 15% win); 1–2: -2.3% (429, 29% win); ≥ 3 (trap): -8.0% (222, 24% win)

**grootste koper, aandeel koopvolume:** < 10%: -8.8% (232, 12% win); 10–25%: -7.4% (142, 11% win); ≥ 25%: -3.4% (536, 32% win)

**duur van top naar dip:** < 30 s (crash): -4.8% (748, 26% win); 30 s–3 min: -6.6% (134, 18% win); ≥ 3 min (langzaam): -15.9% (28, 0% win)

**tijd van start tot top:** < 2 min: -5.0% (770, 25% win); 2–10 min: -7.8% (112, 16% win); ≥ 10 min: -8.1% (28, 14% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
