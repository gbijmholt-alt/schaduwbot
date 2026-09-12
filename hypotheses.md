# Hypotheseregister — 2026-09-12 19:23 UTC

Elke hypothese hier is vastgelegd vóórdat er naar de data gekeken werd: oorzakelijk verhaal, voorspelling, één primaire meetcel en de drempels. Alleen tokens van ná de registratietijd tellen als toets; alles daarvoor is verkennend en levert nooit een oordeel op. Eén herkansing, daarna staat het oordeel vast.

## S1 — Sniper-rang op de bonding curve

Vastgelegd: 2026-09-12 18:00 UTC.

**Oorzaak.** De curve is een constant-product op virtuele reserves: elke volgende koop verhoogt de prijs deterministisch. Wie als k-de koper instapt, koopt vóór alle latere kopers en verkoopt aan hen. Het voordeel zit dus niet in selectie of vaardigheid maar in positie in de rij. De geldstroom bevestigt dat: de enige rollen met netto instroom zijn de rollen die er vóór de zichtbare koers in zitten (dev, bundel, sniper ≤ 5 s).

**Voorspelling.** EV per trade daalt monotoon met de instaprang. Voor lage rang (≤ 3) en een uitstap 'verkopen aan de volgende golf kopers' is de EV na kosten positief, óók zonder enige selectie op het token. Is de EV op rang 1–3 negatief, dan is er op de curve géén positie die winst geeft zonder informatie van vóór de creatie, en is deze lijn dood.

**Primaire cel.** filter `ongefilterd`, rang 3, uitstap `na_10_kopers`. Drempels: n ≥ 500, EV ≥ +3%, winkans ≥ 50%, rug ≤ 5%, maxDD@20% ≤ 40%.

**Oordeel: te vroeg** — 0 van de 500 benodigde tokens in de toets.

Toetsdata: 0 tokens ná registratie; verkennend: 23823 tokens ervoor (11512 overgeslagen wegens herstart of te jong). Inzet 0.2 SOL, tip 0.005 SOL per kant, horizon 180 s.

| primaire cel | toets (telt) | verkennend (telt niet) |
|---|---|---|
| rang 3, na_10_kopers, ongefilterd | – | +5.1% (+4%…+6%) n=14656 |

### Toets (ná registratie)

### Verkennend (vóór registratie — niet gebruiken als bewijs)

**filter `ongefilterd`** — EV per trade (95%-marge) n

| rang | latentie (mediaan) | rug | t10 | t30 | t60 | t180 | na_3_kopers | na_10_kopers | tp50_sl30 | trail20 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.74 s | 62% | +12.2% (+10%…+14%) n=19127 | +10.2% (+8%…+12%) n=19127 | +9.7% (+7%…+12%) n=19127 | +6.8% (+3%…+10%) n=19127 | +4.6% (+3%…+6%) n=19127 | +11.5% (+9%…+13%) n=19127 | -0.9% (-2%…-0%) n=19127 | +12.6% (+11%…+15%) n=19127 |
| 2 | 1.82 s | 64% | +8.7% (+7%…+10%) n=16158 | +7.0% (+5%…+9%) n=16158 | +5.9% (+4%…+8%) n=16158 | +3.2% (-0%…+7%) n=16158 | +6.4% (+6%…+7%) n=16158 | +8.5% (+7%…+10%) n=16158 | +2.8% (+2%…+3%) n=16158 | +9.5% (+8%…+11%) n=16158 |
| 3 | 3.31 s | 66% | +4.7% (+4%…+6%) n=14656 | +3.1% (+1%…+5%) n=14656 | +1.6% (-1%…+4%) n=14656 | -0.8% (-4%…+3%) n=14656 | +2.9% (+2%…+4%) n=14656 | +5.1% (+4%…+6%) n=14656 | +1.5% (+1%…+2%) n=14656 | +5.5% (+4%…+7%) n=14656 |
| 5 | 6.18 s | 68% | +0.5% (-1%…+2%) n=12727 | -1.4% (-3%…+1%) n=12727 | -2.6% (-6%…+0%) n=12727 | -4.3% (-9%…-0%) n=12727 | -0.3% (-1%…+0%) n=12727 | +1.5% (+0%…+3%) n=12727 | -0.2% (-1%…+0%) n=12727 | +1.5% (+0%…+3%) n=12727 |
| 10 | 12.75 s | 69% | -1.2% (-3%…+0%) n=9982 | -3.1% (-5%…-1%) n=9982 | -4.1% (-8%…-0%) n=9982 | -8.4% (-13%…-4%) n=9982 | -0.5% (-1%…+0%) n=9982 | -0.1% (-1%…+1%) n=9982 | -1.0% (-2%…-0%) n=9982 | +0.3% (-1%…+1%) n=9982 |
| 20 | 23.55 s | 68% | -4.3% (-6%…-3%) n=7568 | -6.2% (-9%…-3%) n=7568 | -6.3% (-11%…-2%) n=7568 | -8.9% (-17%…-0%) n=7568 | -3.2% (-4%…-3%) n=7568 | -3.6% (-5%…-2%) n=7568 | -3.8% (-5%…-3%) n=7568 | -2.2% (-4%…-1%) n=7568 |

**filter `geen_bundel`** — EV per trade (95%-marge) n

| rang | latentie (mediaan) | rug | t10 | t30 | t60 | t180 | na_3_kopers | na_10_kopers | tp50_sl30 | trail20 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.14 s | 58% | -5.7% (-7%…-4%) n=12833 | -6.5% (-8%…-5%) n=12833 | -6.4% (-9%…-4%) n=12833 | -7.9% (-12%…-4%) n=12833 | -6.2% (-7%…-6%) n=12833 | -5.3% (-6%…-4%) n=12833 | -5.7% (-6%…-5%) n=12833 | -6.2% (-7%…-5%) n=12833 |
| 2 | 2.88 s | 60% | +1.7% (+0%…+3%) n=10438 | +1.0% (-1%…+3%) n=10438 | +0.2% (-3%…+3%) n=10438 | -1.1% (-6%…+4%) n=10438 | +1.2% (+0%…+2%) n=10438 | +2.5% (+1%…+4%) n=10438 | +1.5% (+1%…+2%) n=10438 | +1.6% (+0%…+3%) n=10438 |
| 3 | 4.96 s | 64% | +3.0% (+2%…+5%) n=9271 | +2.2% (-0%…+5%) n=9271 | +0.3% (-3%…+4%) n=9271 | -0.1% (-6%…+5%) n=9271 | +2.1% (+1%…+3%) n=9271 | +4.5% (+3%…+6%) n=9271 | +2.5% (+2%…+3%) n=9271 | +2.6% (+1%…+4%) n=9271 |
| 5 | 8.64 s | 66% | +3.7% (+2%…+5%) n=7932 | +2.1% (-1%…+5%) n=7932 | -0.2% (-4%…+4%) n=7932 | +1.0% (-6%…+8%) n=7932 | +3.2% (+2%…+4%) n=7932 | +5.4% (+4%…+7%) n=7932 | +4.0% (+3%…+5%) n=7932 | +3.5% (+2%…+5%) n=7932 |
| 10 | 16.77 s | 67% | +1.8% (-0%…+4%) n=6211 | +0.5% (-3%…+4%) n=6211 | -0.7% (-6%…+5%) n=6211 | -4.3% (-11%…+2%) n=6211 | +3.2% (+2%…+4%) n=6211 | +3.6% (+2%…+6%) n=6211 | +3.4% (+2%…+5%) n=6211 | +2.6% (+1%…+4%) n=6211 |
| 20 | 29.42 s | 65% | -1.8% (-4%…+1%) n=4625 | -3.0% (-7%…+1%) n=4625 | -2.3% (-10%…+5%) n=4625 | -2.5% (-16%…+11%) n=4625 | -0.6% (-2%…+1%) n=4625 | -0.5% (-3%…+2%) n=4625 | +0.1% (-1%…+2%) n=4625 | -0.4% (-2%…+1%) n=4625 |

**filter `dev_eerder_gemigreerd`** — EV per trade (95%-marge) n

| rang | latentie (mediaan) | rug | t10 | t30 | t60 | t180 | na_3_kopers | na_10_kopers | tp50_sl30 | trail20 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.96 s | 84% | -1.5% (-4%…+1%) n=3726 | -3.5% (-8%…+1%) n=3726 | -3.5% (-10%…+3%) n=3726 | -3.5% (-14%…+7%) n=3726 | +0.4% (-1%…+2%) n=3726 | +0.2% (-2%…+3%) n=3726 | +0.3% (-1%…+2%) n=3726 | -1.1% (-3%…+1%) n=3726 |
| 2 | 2.41 s | 83% | +3.8% (+1%…+6%) n=3498 | +2.7% (-2%…+7%) n=3498 | +1.7% (-5%…+8%) n=3498 | +1.7% (-9%…+12%) n=3498 | +5.1% (+4%…+6%) n=3498 | +5.4% (+3%…+8%) n=3498 | +5.0% (+3%…+7%) n=3498 | +5.2% (+3%…+8%) n=3498 |
| 3 | 3.86 s | 83% | +2.6% (-0%…+5%) n=3391 | +2.4% (-3%…+7%) n=3391 | +1.8% (-5%…+9%) n=3391 | -0.4% (-11%…+10%) n=3391 | +3.5% (+2%…+5%) n=3391 | +5.5% (+3%…+8%) n=3391 | +3.5% (+2%…+5%) n=3391 | +3.9% (+1%…+6%) n=3391 |
| 5 | 6.76 s | 82% | +1.8% (-1%…+5%) n=3134 | +0.9% (-4%…+6%) n=3134 | +0.1% (-8%…+8%) n=3134 | +0.9% (-12%…+14%) n=3134 | +3.3% (+2%…+5%) n=3134 | +5.0% (+2%…+8%) n=3134 | +3.7% (+2%…+5%) n=3134 | +3.7% (+1%…+6%) n=3134 |
| 10 | 13.3 s | 79% | +0.6% (-3%…+4%) n=2633 | -1.9% (-8%…+4%) n=2633 | -6.6% (-14%…+1%) n=2633 | -8.0% (-18%…+3%) n=2633 | +1.6% (+0%…+3%) n=2633 | +2.0% (-1%…+5%) n=2633 | +2.2% (+0%…+4%) n=2633 | +1.1% (-1%…+4%) n=2633 |
| 20 | 24.5 s | 77% | -1.4% (-6%…+3%) n=2076 | -4.6% (-11%…+2%) n=2076 | -9.4% (-19%…+1%) n=2076 | -4.9% (-26%…+16%) n=2076 | -1.8% (-3%…-0%) n=2076 | -0.7% (-4%…+3%) n=2076 | -1.5% (-4%…+1%) n=2076 | -0.8% (-4%…+2%) n=2076 |

**Beperking.** De simulatie zet ons vóór koper k zonder iemand te verdringen en zonder eigen koersimpact, tegen een vaste tip. Echt snipen is een latentieveiling: de kosten van rang k zijn niet vast en niet gemeten. Deze toets zegt of er op rang k waarde zít — of die rang haalbaar is, zegt hij niet.

