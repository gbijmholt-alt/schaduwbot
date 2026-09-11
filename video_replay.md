# Videostrategie op alle trades — 2026-09-11 09:54 UTC

Tokens sinds 2026-09-11 08:47 UTC: 0 geschikt (≥ 2 uur oud, geen herstart), 0 met trades, 0 haalden 2x de startkoers, 0 kregen een 45%-dip binnen het eerste uur. Bundelgrafiek (≥ 2x vóór de eerste verkoop): 0 tokens. Houdercheck echt uitgevoerd bij – van de gescreende tokens.

## Hoofdtoets (vooraf vastgelegd)

dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap.

Nog geen trades die aan alle voorwaarden voldoen.

## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?

| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |
|---|---|---|---|---|

## Raster: EV per trade (n) — videoregel

| filter | d40_direct | d45_direct | d50_direct | d45_herstel5 |
|---|---|---|---|---|
| alle | – | – | – | – |
| schoon | – | – | – | – |
| bundelgrafiek | – | – | – | – |
| schoon+houders_ok | – | – | – | – |
| schoon+houders_ok+final_stretch | – | – | – | – |
| volledige_screening+schoon | – | – | – | – |
| volledige_screening+schoon+x_link | – | – | – | – |

## Uitstapregels vergeleken (dip 45%, direct)

| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |
|---|---|---|---|
| alle | – | – | – |
| schoon | – | – | – |
| bundelgrafiek | – | – | – |
| schoon+houders_ok | – | – | – |
| schoon+houders_ok+final_stretch | – | – | – |
| volledige_screening+schoon | – | – | – |
| volledige_screening+schoon+x_link | – | – | – |

## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)

Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.

**max koers vóór eerste verkoop (x start):** < 1,3x: –; 1,3–2x: –; ≥ 2x (bundelgrafiek): –

**aandeel supply gekocht in creatieblok:** < 5%: –; 5–20%: –; ≥ 20%: –

**top t.o.v. start:** 2–3x: –; 3–6x: –; ≥ 6x: –

**unieke kopers tot de top:** < 30: –; 30–100: –; ≥ 100: –

**tussentijdse dips ≥ 15% tot de top:** 0 (rechte lijn): –; 1–2: –; ≥ 3 (trap): –

**grootste koper, aandeel koopvolume:** < 10%: –; 10–25%: –; ≥ 25%: –

**duur van top naar dip:** < 30 s (crash): –; 30 s–3 min: –; ≥ 3 min (langzaam): –

**tijd van start tot top:** < 2 min: –; 2–10 min: –; ≥ 10 min: –

## Beperkingen

- De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.
- 'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.
- De houdercheck (gelijke saldi, zelfde funding-tijd) mislukt bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'.
- Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.
- Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.
