# Videostrategie op alle trades — 2026-09-11 11:59 UTC

Tokens sinds 2026-09-11 08:47 UTC: 67 geschikt (≥ 2 uur oud, geen herstart), 59 met trades, 12 haalden 2x de startkoers, 5 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 3 tokens. Houdercheck echt uitgevoerd bij 60% van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

**n = 2, winkans 100%, EV per trade +29.5% (95%-marge -7.2% tot +66.2%), mediaan +29.5%.** Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|
| alle | 5 | 60% | 80% | 0% |
| schoon | 4 | 75% | 75% | 0% |
| bundelgrafiek | 1 | 0% | 100% | 0% |
| schoon+houders_ok | 2 | 50% | 100% | 0% |

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | +10.4% (7, 57% win) | +8.7% (5, 80% win) | -12.5% (5, 40% win) | +21.8% (5, 80% win) |
| schoon | +15.6% (6, 67% win) | +16.1% (4, 100% win) | -10.5% (4, 50% win) | +17.6% (4, 75% win) |
| bundelgrafiek | -20.6% (1, 0% win) | -20.6% (1, 0% win) | -20.6% (1, 0% win) | +38.6% (1, 100% win) |
| schoon+houders_ok | +48.2% (1, 100% win) | +29.5% (2, 100% win) | -15.4% (3, 33% win) | +21.9% (2, 50% win) |
| schoon+houders_ok+final_stretch | – | – | – | – |
| volledige_screening+schoon | – | – | – | – |
| volledige_screening+schoon+x_link | – | – | – | – |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | +8.7% (5, 80% win) | +8.7% (5, 80% win) | +5.2% (5, 60% win) |
| schoon | +16.1% (4, 100% win) | +16.1% (4, 100% win) | +11.6% (4, 75% win) |
| bundelgrafiek | -20.6% (1, 0% win) | -20.6% (1, 0% win) | -20.6% (1, 0% win) |
| schoon+houders_ok | +29.5% (2, 100% win) | +29.5% (2, 100% win) | +20.6% (2, 50% win) |
| schoon+houders_ok+final_stretch | – | – | – |
| volledige_screening+schoon | – | – | – |
| volledige_screening+schoon+x_link | – | – | – |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: +24.5% (2, 100% win); 1,3–2x: +7.6% (2, 100% win); ≥ 2x (bundelgrafiek): -20.6% (1, 0% win)

**aandeel supply gekocht in creatieblok:** < 5%: +8.7% (5, 80% win); 5–20%: –; ≥ 20%: –

**top t.o.v. start:** 2–3x: +2.6% (2, 100% win); 3–6x: -4.9% (2, 50% win); ≥ 6x: +48.2% (1, 100% win)

**unieke kopers tot de top:** < 30: +8.7% (5, 80% win); 30–100: –; ≥ 100: –

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): -20.6% (1, 0% win); 1–2: +19.9% (3, 100% win); ≥ 3 (trap): +4.5% (1, 100% win)

**grootste koper, aandeel koopvolume:** < 10%: –; 10–25%: –; ≥ 25%: +8.7% (5, 80% win)

**duur van top naar dip:** < 30 s (crash): +8.7% (5, 80% win); 30 s–3 min: –; ≥ 3 min (langzaam): –

**tijd van start tot top:** < 2 min: +8.7% (5, 80% win); 2–10 min: –; ≥ 10 min: –

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- De houdercheck (gelijke saldi, zelfde funding-tijd) mislukt bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
