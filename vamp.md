# Afgeleide tokens ('vamps') — 2026-09-15 09:17 UTC

De claim uit de KOL-video van 14 sept: als er een token loopt en iemand lanceert een gecorrigeerde versie ervan, neemt die afgeleide de plek over. Daar hoort een basisgetal bij en dat gaf de video niet. Hier staat het.

**Wat 'loper' hier betekent**: een token waarvan de koers boven 50% van de voltooiingsprijs kwam (marktkap ≈ 205 SOL) of dat migreerde. Boven de curve zien we niets meer, dus een token dat op de AMM naar $500k loopt — het geval uit de video — meten we alleen tot het de curve verlaat.

**Wat 'afgeleide' hier betekent**: een token gelanceerd binnen 120 minuten na dat moment, met dezelfde ticker, een gedeeld woord van minstens drie letters in de naam, de ticker als woord in de naam, of een naamgelijkenis van 80% of hoger. De 'fout in de naam' uit de video is een oordeel en zit hier niet in.

131788 tokens, 6654 lopers, 118504 koppelingen, **39751 unieke afgeleiden**. 49 tickers uitgesloten omdat ze bij 200+ tokens voorkomen en dus geen identiteit zijn.

## Doen afgeleiden het beter?

| groep | n | mediaan hoogste veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| afgeleiden | 5629 | 4.72x | 100.0% | 30.8% | 25.9% |
| alle andere tokens uit dezelfde uren | 10343 | 4.02x | 100.0% | 20.6% | 15.4% |
| alle andere tokens | 10343 | 4.02x | 100.0% | 20.6% | 15.4% |

Verschil met tokens uit dezelfde uren, met 95%-marge. Loopt de marge door nul, dan is er geen verschil aangetoond.

| maat | verschil | 95%-marge | aangetoond |
|---|---|---|---|
| 2x | +0.0% | +0.0% tot +0.0% | nee |
| 10x | +10.2% | +8.8% tot +11.7% | ja |
| gemigreerd | +10.4% | +9.1% tot +11.8% | ja |

## Per soort koppeling

| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| gedeeld_woord | 3266 | 4.21x | 100.0% | 25.4% | 20.0% |
| gelijkende_naam | 183 | 4.39x | 100.0% | 18.6% | 14.8% |
| ticker_in_naam | 324 | 4.30x | 100.0% | 23.5% | 17.3% |
| zelfde_ticker | 1856 | 6.54x | 100.0% | 42.8% | 38.9% |

## Was de loper al gemigreerd?

| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| loper_gemigreerd | 3676 | 5.30x | 100.0% | 36.9% | 33.1% |
| loper_op_curve | 1953 | 4.09x | 100.0% | 19.4% | 12.3% |

## Hoe snel na de loper

| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |
|---|---|---|---|---|---|
| 0-10 min | 1753 | 4.49x | 100.0% | 26.0% | 19.1% |
| 10-30 min | 1688 | 4.63x | 100.0% | 30.9% | 27.6% |
| 30-60 min | 1113 | 4.89x | 100.0% | 34.3% | 30.3% |
| 60-120 min | 1075 | 5.20x | 100.0% | 34.9% | 29.9% |

## Hoeveel gevallen per dag

Zonder aantallen is het geen strategie maar een hobby.

| dag | afgeleiden |
|---|---|
| 2026-09-10 | 4708 |
| 2026-09-11 | 8930 |
| 2026-09-12 | 6654 |
| 2026-09-13 | 7493 |
| 2026-09-14 | 9236 |
| 2026-09-15 | 2730 |

## De tien grootste afgeleiden

Let op: dit zijn de uitschieters, geselecteerd op uitkomst. Ze zeggen niets over de verwachting — ze staan er om te kunnen controleren of de koppelingen inhoudelijk kloppen.

| loper | afgeleide | reden | na (min) | hoogste veelvoud |
|---|---|---|---|---|
| DOCAT (DOG CAT) | dog (Sloppydog) | ticker_in_naam | 112.4 | 120.11x |
| CADOG (CAT DOG) | dog (Sloppydog) | ticker_in_naam | 110.8 | 120.11x |
| Duluth (beatles) | Duluth (Beatles) | zelfde_ticker | 11.7 | 88.90x |
| Duluth (Beatles) | Duluth (Beatles) | zelfde_ticker | 8.8 | 88.90x |
| Duluth (Beatles) | Duluth (Beatles) | zelfde_ticker | 1.7 | 88.90x |
| Stable (Stable Coin) | $GOAT (goat coin) | gedeeld_woord | 71.4 | 79.19x |
| Stable (Stable Coin) | $GOAT (goat coin) | gedeeld_woord | 63.1 | 79.19x |
| AMC (A Meme Coin) | $GOAT (goat coin) | gedeeld_woord | 52.2 | 79.19x |
| Stable (Stable Coin) | $GOAT (goat coin) | gedeeld_woord | 52.0 | 79.19x |
| Zcat (The Invisible Cat) | HYCAT (Hyper Cat) | gedeeld_woord | 94.8 | 74.42x |

**Verkennend.** Deze analyse kijkt naar data die er al lag; elke uitkomst hier is een hypothese, geen toets. Komt er iets uit, dan moet het vooraf vastgelegd en op nieuwe tokens gemeten worden.

