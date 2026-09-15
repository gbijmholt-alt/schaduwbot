# Afgeleide tokens ('vamps') — 2026-09-15 10:00 UTC

De claim uit de KOL-video van 14 sept: als er een token loopt en iemand lanceert een gecorrigeerde versie ervan, neemt die afgeleide de plek over. Daar hoort een basisgetal bij en dat gaf de video niet. Hier staat het.

**Wat 'loper' hier betekent**: een token waarvan de koers boven 50% van de voltooiingsprijs kwam (marktkap ≈ 205 SOL) of dat migreerde. Boven de curve zien we niets meer, dus een token dat op de AMM naar $500k loopt — het geval uit de video — meten we alleen tot het de curve verlaat.

**Wat 'afgeleide' hier betekent**: een token gelanceerd binnen 120 minuten na dat moment, met dezelfde ticker, een gedeeld woord van minstens drie letters in de naam, de ticker als woord in de naam, of een naamgelijkenis van 80% of hoger. De 'fout in de naam' uit de video is een oordeel en zit hier niet in.

132582 tokens, 6700 lopers, 119050 koppelingen, **40017 unieke afgeleiden**. 49 tickers uitgesloten omdat ze bij 200+ tokens voorkomen en dus geen identiteit zijn.

## Doen afgeleiden het beter?

| groep | n | mediaan hoogste veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| afgeleiden | 5679 | 4.73x | 100.0% | 30.8% | 25.9% |
| alle andere tokens uit dezelfde uren | 10411 | 4.03x | 100.0% | 20.6% | 15.5% |
| alle andere tokens | 10411 | 4.03x | 100.0% | 20.6% | 15.5% |

Verschil met tokens uit dezelfde uren, met 95%-marge. Loopt de marge door nul, dan is er geen verschil aangetoond.

| maat | verschil | 95%-marge | aangetoond |
|---|---|---|---|
| 2x | +0.0% | +0.0% tot +0.0% | nee |
| 10x | +10.2% | +8.8% tot +11.6% | ja |
| gemigreerd | +10.5% | +9.1% tot +11.8% | ja |

## Per soort koppeling

| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| gedeeld_woord | 3295 | 4.22x | 100.0% | 25.4% | 20.0% |
| gelijkende_naam | 184 | 4.36x | 100.0% | 18.5% | 14.7% |
| ticker_in_naam | 327 | 4.28x | 100.0% | 23.5% | 17.4% |
| zelfde_ticker | 1873 | 6.53x | 100.0% | 42.8% | 39.0% |

## Was de loper al gemigreerd?

| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| loper_gemigreerd | 3707 | 5.30x | 100.0% | 36.9% | 33.1% |
| loper_op_curve | 1972 | 4.12x | 100.0% | 19.3% | 12.3% |

## Hoe snel na de loper

| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| 0-10 min | 1763 | 4.50x | 100.0% | 25.9% | 19.1% |
| 10-30 min | 1707 | 4.62x | 100.0% | 30.8% | 27.5% |
| 30-60 min | 1128 | 4.88x | 100.0% | 34.2% | 30.1% |
| 60-120 min | 1081 | 5.23x | 100.0% | 35.1% | 30.2% |

## Hoeveel gevallen per dag

Zonder aantallen is het geen strategie maar een hobby.

| dag | afgeleiden |
|---|---|
| 2026-09-10 | 4708 |
| 2026-09-11 | 8930 |
| 2026-09-12 | 6654 |
| 2026-09-13 | 7493 |
| 2026-09-14 | 9236 |
| 2026-09-15 | 2996 |

## De tien grootste afgeleiden

Let op: dit zijn de uitschieters, geselecteerd op uitkomst. Ze zeggen niets over de verwachting — ze staan er om te kunnen controleren of de koppelingen inhoudelijk kloppen.

| loper | afgeleide | reden | na (min) | hoogste veelvoud |
|---|---|---|---|---|
| DOCAT (DOG CAT) | dog (Sloppydog) | ticker_in_naam | 112.4 | 120.11x |
| CADOG (CAT DOG) | dog (Sloppydog) | ticker_in_naam | 110.8 | 120.11x |
| $WAR (MAYHEM WAR) | Mayhem (Mayhem) | gedeeld_woord | 39.4 | 93.09x |
| Duluth (beatles) | Duluth (Beatles) | zelfde_ticker | 11.7 | 88.90x |
| Duluth (Beatles) | Duluth (Beatles) | zelfde_ticker | 8.8 | 88.90x |
| Duluth (Beatles) | Duluth (Beatles) | zelfde_ticker | 1.7 | 88.90x |
| Stable (Stable Coin) | $GOAT (goat coin) | gedeeld_woord | 71.4 | 79.19x |
| Stable (Stable Coin) | $GOAT (goat coin) | gedeeld_woord | 63.1 | 79.19x |
| AMC (A Meme Coin) | $GOAT (goat coin) | gedeeld_woord | 52.2 | 79.19x |
| Stable (Stable Coin) | $GOAT (goat coin) | gedeeld_woord | 52.0 | 79.19x |

**Verkennend.** Deze analyse kijkt naar data die er al lag; elke uitkomst hier is een hypothese, geen toets. Komt er iets uit, dan moet het vooraf vastgelegd en op nieuwe tokens gemeten worden.

