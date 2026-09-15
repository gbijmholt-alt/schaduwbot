# Afgeleide tokens ('vamps') — 2026-09-15 12:01 UTC

De claim uit de KOL-video van 14 sept: als er een token loopt en iemand lanceert een gecorrigeerde versie ervan, neemt die afgeleide de plek over. Daar hoort een basisgetal bij en dat gaf de video niet. Hier staat het.

**Wat 'loper' hier betekent**: een token waarvan de koers boven 50% van de voltooiingsprijs kwam (marktkap ≈ 205 SOL) of dat migreerde. Boven de curve zien we niets meer, dus een token dat op de AMM naar $500k loopt — het geval uit de video — meten we alleen tot het de curve verlaat.

**Wat 'afgeleide' hier betekent**: een token gelanceerd binnen 120 minuten na dat moment, met dezelfde ticker, een gedeeld woord van minstens drie letters in de naam, de ticker als woord in de naam, of een naamgelijkenis van 80% of hoger. De 'fout in de naam' uit de video is een oordeel en zit hier niet in.

134689 tokens, 6807 lopers, 49968 koppelingen, **27625 unieke afgeleiden** van de 134665 tokens die in een venster vielen. 49 tickers en 18 woorden uitgesloten omdat ze te vaak voorkomen om nog een identiteit te zijn.

**Uitkomst** = hoogste koers gedeeld door de eerste koers minstens 30 seconden na creatie. Niet gedeeld door de startkoers van de curve: die is de prijs bij nul verkochte tokens, daar springt elke eerste koop ver overheen, en dan haalt 100% van álle tokens 'meer dan 2x' — in beide groepen. Een maat die overal hetzelfde uitkomt kan geen verschil aantonen.

## Doen afgeleiden het beter?

| groep | n | mediaan veelvoud vanaf instap | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| afgeleiden | 13795 | 1.00x | 14.9% | 1.4% | 2.9% |
| géén kopie, wél hetzelfde venster na dezelfde loper | 55072 | 1.00x | 12.4% | 1.1% | 2.1% |
| alle andere tokens | 55087 | 1.00x | 12.4% | 1.1% | 2.1% |

Verschil met de tokens uit hetzelfde venster die géén kopie zijn — zelfde moment, zelfde loper, zelfde marktstemming. Met 95%-marge; loopt die door nul, dan is er geen verschil aangetoond.

| maat | verschil | 95%-marge | aangetoond |
|---|---|---|---|
| 2x | +2.5% | +1.8% tot +3.1% | ja |
| 10x | +0.4% | +0.1% tot +0.6% | ja |
| gemigreerd | +0.8% | +0.5% tot +1.1% | ja |

## Per soort koppeling

| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| gedeeld_woord | 6361 | 1.00x | 12.4% | 1.1% | 2.3% |
| gelijkende_naam | 834 | 1.00x | 13.9% | 1.1% | 2.2% |
| ticker_in_naam | 1758 | 1.00x | 15.0% | 1.1% | 2.1% |
| zelfde_ticker | 4842 | 1.01x | 18.3% | 2.0% | 4.1% |

## Was de loper al gemigreerd?

| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| loper_gemigreerd | 8414 | 1.00x | 12.7% | 1.1% | 2.8% |
| loper_op_curve | 5381 | 1.02x | 18.3% | 1.9% | 3.0% |

## Hoe snel na de loper

| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| 0-10 min | 4107 | 1.00x | 16.0% | 1.6% | 3.5% |
| 10-30 min | 3465 | 1.01x | 15.6% | 1.2% | 3.0% |
| 30-60 min | 2762 | 1.00x | 14.4% | 1.5% | 2.5% |
| 60-120 min | 3461 | 1.00x | 13.3% | 1.4% | 2.3% |

## Hoeveel gevallen per dag

Zonder aantallen is het geen strategie maar een hobby.

| dag | afgeleiden |
|---|---|
| 2026-09-10 | 3125 |
| 2026-09-11 | 5889 |
| 2026-09-12 | 4390 |
| 2026-09-13 | 5156 |
| 2026-09-14 | 6488 |
| 2026-09-15 | 2577 |

## De tien grootste afgeleiden

Let op: dit zijn de uitschieters, geselecteerd op uitkomst. Ze zeggen niets over de verwachting — ze staan er om te kunnen controleren of de koppelingen inhoudelijk kloppen.

| loper | afgeleide | reden | na (min) | hoogste veelvoud |
|---|---|---|---|---|
| stocklana (stocklana) | stocklana (stocklana) | zelfde_ticker | 40.4 | 983.47x |
| stocklana (stocklana) | stocklana (stocklana) | zelfde_ticker | 54.4 | 983.47x |
| stocklana (stocklana) | stocklana (stocklana) | zelfde_ticker | 53.9 | 983.47x |
| stocklana (stocklana) | stocklana (stocklana) | zelfde_ticker | 51.7 | 983.47x |
| stocklana (stocklana) | stocklana (stocklana) | zelfde_ticker | 29.0 | 983.47x |
| stocklana (stocklana) | stocklana (stocklana) | zelfde_ticker | 32.0 | 983.47x |
| stocklana (stocklana) | stocklana (stocklana) | zelfde_ticker | 24.0 | 983.47x |
| stocklana (stocklana) | stocklana (stocklana) | zelfde_ticker | 8.7 | 983.47x |
| stocklana (stocklana) | stocklana (stocklana) | zelfde_ticker | 4.7 | 983.47x |
| Bricko (Bricko) | Bricko (Bricko) | zelfde_ticker | 31.0 | 161.02x |

**Verkennend.** Deze analyse kijkt naar data die er al lag; elke uitkomst hier is een hypothese, geen toets. Komt er iets uit, dan moet het vooraf vastgelegd en op nieuwe tokens gemeten worden.

