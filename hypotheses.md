# Hypotheseregister — 2026-09-12 17:23 UTC

Elke hypothese hier is vastgelegd vóórdat er naar de data gekeken werd: oorzakelijk verhaal, voorspelling, één primaire meetcel en de drempels. Alleen tokens van ná de registratietijd tellen als toets; alles daarvoor is verkennend en levert nooit een oordeel op. Eén herkansing, daarna staat het oordeel vast.

## S1 — Sniper-rang op de bonding curve

Vastgelegd: 2026-09-12 18:00 UTC.

**Oorzaak.** De curve is een constant-product op virtuele reserves: elke volgende koop verhoogt de prijs deterministisch. Wie als k-de koper instapt, koopt vóór alle latere kopers en verkoopt aan hen. Het voordeel zit dus niet in selectie of vaardigheid maar in positie in de rij. De geldstroom bevestigt dat: de enige rollen met netto instroom zijn de rollen die er vóór de zichtbare koers in zitten (dev, bundel, sniper ≤ 5 s).

**Voorspelling.** EV per trade daalt monotoon met de instaprang. Voor lage rang (≤ 3) en een uitstap 'verkopen aan de volgende golf kopers' is de EV na kosten positief, óók zonder enige selectie op het token. Is de EV op rang 1–3 negatief, dan is er op de curve géén positie die winst geeft zonder informatie van vóór de creatie, en is deze lijn dood.

**Primaire cel.** filter `ongefilterd`, rang 3, uitstap `na_10_kopers`. Drempels: n ≥ 500, EV ≥ +3%, winkans ≥ 50%, rug ≤ 5%, maxDD@20% ≤ 40%.

**Oordeel: te vroeg** — 0 van de 500 benodigde tokens in de toets.

Toetsdata: 0 tokens ná registratie; verkennend: 23481 tokens ervoor (11630 overgeslagen wegens herstart of te jong). Inzet 0.2 SOL, tip 0.005 SOL per kant, horizon 180 s.

| primaire cel | toets (telt) | verkennend (telt niet) |
|---|---|---|
| rang 3, na_10_kopers, ongefilterd | – | +5.2% (+4%…+6%) n=14555 |

### Toets (ná registratie)

### Verkennend (vóór registratie — niet gebruiken als bewijs)

**filter `ongefilterd`** — EV per trade (95%-marge) n

| rang | latentie (mediaan) | rug | t10 | t30 | t60 | t180 | na_3_kopers | na_10_kopers | tp50_sl30 | trail20 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.74 s | 62% | +13.0% (+11%…+15%) n=18858 | +11.1% (+9%…+13%) n=18858 | +10.5% (+8%…+13%) n=18858 | +7.6% (+4%…+11%) n=18858 | +5.3% (+4%…+7%) n=18858 | +12.2% (+10%…+14%) n=18858 | -0.2% (-1%…+0%) n=18858 | +13.4% (+11%…+15%) n=18858 |
| 2 | 1.82 s | 64% | +8.7% (+7%…+10%) n=16044 | +7.2% (+5%…+9%) n=16044 | +6.0% (+4%…+8%) n=16044 | +3.4% (-0%…+7%) n=16044 | +6.4% (+6%…+7%) n=16044 | +8.6% (+7%…+10%) n=16044 | +2.8% (+2%…+3%) n=16044 | +9.6% (+8%…+11%) n=16044 |
| 3 | 3.31 s | 67% | +4.7% (+4%…+6%) n=14555 | +3.2% (+1%…+5%) n=14555 | +1.7% (-1%…+4%) n=14555 | -0.7% (-4%…+3%) n=14555 | +2.9% (+2%…+4%) n=14555 | +5.2% (+4%…+6%) n=14555 | +1.5% (+1%…+2%) n=14555 | +5.5% (+4%…+7%) n=14555 |
| 5 | 6.17 s | 68% | +0.6% (-1%…+2%) n=12644 | -1.2% (-3%…+1%) n=12644 | -2.6% (-6%…+0%) n=12644 | -4.2% (-8%…+0%) n=12644 | -0.3% (-1%…+0%) n=12644 | +1.5% (+0%…+3%) n=12644 | -0.3% (-1%…+0%) n=12644 | +1.6% (+1%…+3%) n=12644 |
| 10 | 12.74 s | 69% | -1.1% (-3%…+0%) n=9922 | -3.0% (-5%…-1%) n=9922 | -3.9% (-8%…-0%) n=9922 | -8.3% (-13%…-4%) n=9922 | -0.5% (-1%…+0%) n=9922 | -0.0% (-1%…+1%) n=9922 | -1.0% (-2%…-0%) n=9922 | +0.4% (-1%…+2%) n=9922 |
| 20 | 23.52 s | 68% | -4.2% (-6%…-3%) n=7521 | -6.2% (-9%…-3%) n=7521 | -6.2% (-11%…-1%) n=7521 | -8.8% (-17%…-0%) n=7521 | -3.2% (-4%…-3%) n=7521 | -3.6% (-5%…-2%) n=7521 | -3.8% (-5%…-3%) n=7521 | -2.2% (-4%…-1%) n=7521 |

**filter `geen_bundel`** — EV per trade (95%-marge) n

| rang | latentie (mediaan) | rug | t10 | t30 | t60 | t180 | na_3_kopers | na_10_kopers | tp50_sl30 | trail20 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.14 s | 58% | -5.3% (-7%…-4%) n=12694 | -6.1% (-8%…-4%) n=12694 | -6.0% (-9%…-3%) n=12694 | -7.4% (-11%…-3%) n=12694 | -5.9% (-7%…-5%) n=12694 | -5.0% (-6%…-4%) n=12694 | -5.4% (-6%…-5%) n=12694 | -5.9% (-7%…-5%) n=12694 |
| 2 | 2.88 s | 60% | +1.7% (+0%…+3%) n=10364 | +1.1% (-1%…+3%) n=10364 | +0.2% (-3%…+3%) n=10364 | -0.8% (-6%…+4%) n=10364 | +1.2% (+1%…+2%) n=10364 | +2.5% (+1%…+4%) n=10364 | +1.6% (+1%…+2%) n=10364 | +1.6% (+0%…+3%) n=10364 |
| 3 | 4.96 s | 64% | +3.1% (+2%…+5%) n=9207 | +2.4% (-0%…+5%) n=9207 | +0.4% (-3%…+4%) n=9207 | +0.1% (-5%…+6%) n=9207 | +2.1% (+1%…+3%) n=9207 | +4.5% (+3%…+6%) n=9207 | +2.5% (+2%…+3%) n=9207 | +2.6% (+1%…+4%) n=9207 |
| 5 | 8.63 s | 66% | +3.8% (+2%…+5%) n=7880 | +2.2% (-1%…+5%) n=7880 | -0.1% (-4%…+4%) n=7880 | +1.2% (-5%…+8%) n=7880 | +3.2% (+2%…+4%) n=7880 | +5.5% (+4%…+7%) n=7880 | +4.0% (+3%…+5%) n=7880 | +3.5% (+2%…+5%) n=7880 |
| 10 | 16.75 s | 67% | +1.9% (-0%…+4%) n=6172 | +0.7% (-3%…+4%) n=6172 | -0.5% (-6%…+5%) n=6172 | -4.1% (-11%…+3%) n=6172 | +3.2% (+2%…+4%) n=6172 | +3.7% (+2%…+6%) n=6172 | +3.4% (+2%…+5%) n=6172 | +2.7% (+1%…+4%) n=6172 |
| 20 | 29.39 s | 64% | -1.7% (-4%…+1%) n=4595 | -3.0% (-7%…+1%) n=4595 | -2.1% (-10%…+6%) n=4595 | -2.2% (-16%…+11%) n=4595 | -0.6% (-2%…+1%) n=4595 | -0.4% (-3%…+2%) n=4595 | +0.2% (-1%…+2%) n=4595 | -0.4% (-2%…+1%) n=4595 |

**filter `dev_eerder_gemigreerd`** — EV per trade (95%-marge) n

| rang | latentie (mediaan) | rug | t10 | t30 | t60 | t180 | na_3_kopers | na_10_kopers | tp50_sl30 | trail20 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.96 s | 84% | -1.4% (-4%…+1%) n=3703 | -3.3% (-8%…+1%) n=3703 | -3.5% (-10%…+3%) n=3703 | -3.3% (-14%…+7%) n=3703 | +0.5% (-1%…+2%) n=3703 | +0.3% (-2%…+3%) n=3703 | +0.3% (-1%…+2%) n=3703 | -1.1% (-3%…+1%) n=3703 |
| 2 | 2.39 s | 83% | +3.8% (+1%…+6%) n=3478 | +2.9% (-2%…+8%) n=3478 | +1.7% (-5%…+8%) n=3478 | +1.8% (-9%…+12%) n=3478 | +5.2% (+4%…+6%) n=3478 | +5.5% (+3%…+8%) n=3478 | +5.0% (+3%…+7%) n=3478 | +5.2% (+3%…+8%) n=3478 |
| 3 | 3.86 s | 83% | +2.7% (+0%…+5%) n=3372 | +2.6% (-2%…+8%) n=3372 | +1.9% (-5%…+9%) n=3372 | -0.2% (-11%…+10%) n=3372 | +3.6% (+2%…+5%) n=3372 | +5.6% (+3%…+8%) n=3372 | +3.6% (+2%…+5%) n=3372 | +3.9% (+1%…+6%) n=3372 |
| 5 | 6.76 s | 82% | +1.8% (-1%…+5%) n=3116 | +1.0% (-4%…+6%) n=3116 | +0.0% (-8%…+8%) n=3116 | +1.0% (-12%…+14%) n=3116 | +3.2% (+2%…+5%) n=3116 | +5.0% (+2%…+8%) n=3116 | +3.7% (+2%…+5%) n=3116 | +3.7% (+1%…+6%) n=3116 |
| 10 | 13.29 s | 79% | +0.5% (-3%…+4%) n=2618 | -1.9% (-8%…+4%) n=2618 | -6.5% (-14%…+1%) n=2618 | -7.7% (-18%…+3%) n=2618 | +1.6% (+0%…+3%) n=2618 | +2.1% (-1%…+5%) n=2618 | +2.2% (+0%…+4%) n=2618 | +1.2% (-1%…+4%) n=2618 |
| 20 | 24.41 s | 77% | -1.4% (-6%…+3%) n=2061 | -4.8% (-11%…+2%) n=2061 | -9.5% (-20%…+0%) n=2061 | -5.0% (-26%…+16%) n=2061 | -1.8% (-3%…-0%) n=2061 | -0.7% (-4%…+3%) n=2061 | -1.5% (-4%…+1%) n=2061 | -0.9% (-4%…+2%) n=2061 |

**Beperking.** De simulatie zet ons vóór koper k zonder iemand te verdringen en zonder eigen koersimpact, tegen een vaste tip. Echt snipen is een latentieveiling: de kosten van rang k zijn niet vast en niet gemeten. Deze toets zegt of er op rang k waarde zít — of die rang haalbaar is, zegt hij niet.

