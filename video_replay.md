# Videostrategie op alle trades — 2026-09-12 03:56 UTC

Tokens sinds 2026-09-11 08:47 UTC: 15843 geschikt (≥ 2 uur oud, geen herstart), 13363 met trades, 2819 haalden 2x de startkoers, 2173 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 631 tokens. Houdercheck echt uitgevoerd bij 78% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 751, winkans 21%, EV per trade -7.0% (95%-marge -9.3% tot -4.7%), mediaan -10.0%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)

- **H2** (2026-09-11 15:00 UTC): dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek. Aanleiding: +8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties. Resultaat: n = 1243, winkans 23%, EV -6.3% (95%-marge -9.4% tot -3.2%).

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 2173 | 37% | 77% | 0% |
| schoon | 1732 | 40% | 76% | 0% |
| bundelgrafiek | 441 | 27% | 78% | 0% |
| schoon+houders_ok | 751 | 37% | 78% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | -7.2% (2219, 23% win) | -7.1% (2173, 23% win) | -8.0% (2134, 21% win) | -6.3% (1719, 27% win) |
| schoon | -6.7% (1774, 24% win) | -6.5% (1732, 24% win) | -7.0% (1704, 23% win) | -5.7% (1436, 28% win) |
| bundelgrafiek | -9.1% (445, 18% win) | -9.7% (441, 17% win) | -11.9% (430, 14% win) | -9.8% (283, 22% win) |
| schoon+houders_ok | -6.8% (716, 20% win) | -7.0% (751, 21% win) | -7.1% (795, 20% win) | -3.1% (602, 25% win) |
| schoon+houders_ok+final_stretch | -9.1% (279, 12% win) | -10.1% (288, 12% win) | -9.2% (295, 10% win) | -7.1% (211, 16% win) |
| volledige_screening+schoon | -10.9% (171, 12% win) | -11.8% (177, 10% win) | -10.8% (179, 9% win) | -8.7% (118, 16% win) |
| volledige_screening+schoon+x_link | -10.6% (132, 14% win) | -11.8% (134, 10% win) | -11.0% (134, 8% win) | -9.8% (81, 15% win) |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | -7.1% (2173, 23% win) | -6.8% (2173, 22% win) | -6.8% (2173, 21% win) |
| schoon | -6.5% (1732, 24% win) | -6.2% (1732, 24% win) | -5.3% (1732, 23% win) |
| bundelgrafiek | -9.7% (441, 17% win) | -8.8% (441, 16% win) | -12.6% (441, 13% win) |
| schoon+houders_ok | -7.0% (751, 21% win) | -6.6% (751, 21% win) | -4.4% (751, 22% win) |
| schoon+houders_ok+final_stretch | -10.1% (288, 12% win) | -8.8% (288, 10% win) | -10.0% (288, 13% win) |
| volledige_screening+schoon | -11.8% (177, 10% win) | -10.4% (177, 8% win) | -11.8% (177, 13% win) |
| volledige_screening+schoon+x_link | -11.8% (134, 10% win) | -10.5% (134, 8% win) | -12.5% (134, 10% win) |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: -4.5% (848, 31% win); 1,3–2x: -8.4% (884, 18% win); ≥ 2x (bundelgrafiek): -9.7% (441, 17% win)

**aandeel supply gekocht in creatieblok:** < 5%: -5.7% (1317, 30% win); 5–20%: -9.8% (439, 12% win); ≥ 20%: -8.8% (417, 11% win)

**top t.o.v. start:** 2–3x: -6.8% (1213, 21% win); 3–6x: -6.9% (746, 25% win); ≥ 6x: -9.8% (214, 24% win)

**unieke kopers tot de top:** < 30: -5.5% (1328, 30% win); 30–100: -8.4% (454, 10% win); ≥ 100: -11.4% (391, 12% win)

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -9.6% (578, 14% win); 1–2: -5.5% (1024, 26% win); ≥ 3 (trap): -7.6% (571, 26% win)

**grootste koper, aandeel koopvolume:** < 10%: -10.5% (596, 11% win); 10–25%: -7.5% (353, 12% win); ≥ 25%: -5.4% (1224, 31% win)

**duur van top naar dip:** < 30 s (crash): -6.7% (1748, 25% win); 30 s–3 min: -8.6% (343, 16% win); ≥ 3 min (langzaam): -11.3% (82, 5% win)

**tijd van start tot top:** < 2 min: -6.3% (1813, 24% win); 2–10 min: -11.7% (286, 14% win); ≥ 10 min: -11.3% (74, 12% win)

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
