# Schaduwbot — fase 1

Meet of de memecoin-scalpstrategie uit de video (pump.fun, dip-vanaf-ATH, houder- en bundle-checks) na kosten een positieve verwachtingswaarde heeft. **Er wordt niets gehandeld**: geen wallet, geen sleutel, alleen virtuele trades tegen echte prijzen. Specificatie: `Fase1_Schaduwbot_Bouwplan.docx`.

Alle bestanden staan plat in één map (geen submappen) zodat een upload via de GitHub-website altijd goed gaat.

## Werking

```
Solana websocket (logsSubscribe op pump.fun-programma)
  └─ decoder.py      CreateEvent / TradeEvent / CompleteEvent uit "Program data:"
     └─ state.py     reserves, prijs, ATH, kopers, creator-positie, rug-detectie
        ├─ filters   New pairs ≥ $7k  |  Final stretch: curve ≥ 70%, ≤ 40 min, $8k–$30k
        ├─ screening.py (eenmalig, async)  top-5 saldi & funding-datum, bundle-patroon,
        │                                   dev-%, insiders-%, pro-traders-proxy, X-link, RugCheck
        └─ simulator.py  dip 35/40/45% ➜ herstel ➜ fill na 2 s ➜ V1/V2/V3 ➜ fill na 2 s
                          slippage exact via bonding curve; fees pump 1,25% + Axiom 0,855% / PP 0,5% + prio
store.py (SQLite)  ➜ report.py (funnel, winkans, rug-%, EV, drawdown, Monte Carlo) ➜ reports/latest.md
health.py          GET :8080/health  (lokaal, op de server zelf)
status_push.py      elke 5 min: status.md + report.json naar GitHub-branch 'status' (geheimen weggelakt)
```

Tokens die filter A nooit halen worden niet gesimuleerd. Tokens die filter A halen worden **altijd** gesimuleerd, ook als de screening faalt — zo meten we of de checks waarde toevoegen (`screen_pass` 1/0 in `sim_trades`).

## Commando's

```
python3 main.py run        # 24/7 (systemd)
python3 main.py probe 60   # 60 s meeluisteren, decoder-sanity
python3 main.py report     # rapport uit de database
python3 test_all.py        # unit tests (decoder, curve, simulator)
```

## Deploy (Hetzner, zonder SSH of console)

1. `cloud-init.yaml` met drie ingevulde waarden (GitHub-gebruiker, GitHub-token, Helius-key) in het veld *Cloud config* bij het aanmaken van de server.
2. Dat bestand doet vrijwel niets zelf: het haalt alleen `bootstrap.sh` op en start het. Alle installatielogica — pakketten, git clone, venv, systemd — zit in `bootstrap.sh`, niet in de cloud-config. Dat houdt het cloud-config-veld kort en ongevoelig voor typefouten of een lastig toetsenbord in de Hetzner-console.
3. `bootstrap.sh` installeert **eerst** een timer (`schaduwbot-tick.timer`, elke 5 minuten) die `status_push.py` aanroept, en pas **daarna** de pakketten en de bot zelf. Gaat er ergens iets mis (apt-get, git clone, install.sh), dan wordt dat gemeld via `status_push.py` naar de branch **`status`** (bestand `status.md`, inclusief bootstrap- en cloud-init-log) én automatisch opnieuw geprobeerd bij de volgende tick — zonder dat iemand hoeft in te loggen op de server.
4. Zodra de bot draait, zorgt `update.sh` (aangeroepen via dezelfde tick) voor nieuwe code van `main` en herstart de service bij wijziging of bij een crash.

Alle parameters staan in `config.py` en zijn via `.env` te overschrijven.

## Status volgen

- `status.md` op branch `status`: tijdstip, service-status, code-versie, health, laatste rapport, bot-log, bootstrap-log, cloud-init-log. Geheimen (tokens, keys) worden er altijd uitgefilterd voordat iets naar GitHub gaat.
- `report.json` op dezelfde branch: het laatste dagrapport, alleen gepusht als het is veranderd.

## Bekende benaderingen (zie bouwplan §2 en §8)

- "Final stretch" en "pro traders" zijn Axiom-labels zonder publieke definitie → benaderd.
- Community-check op X wordt niet gemeten; X-link-aanwezigheid en unieke kopers worden gelogd.
- Schaduwfills zijn een bovengrens: mislukte transacties en MEV zitten er niet in.

## Wallet-analyse (met terugwerkende kracht)

`wallet_analysis.py` zoekt in de gelogde trades naar wallets die structureel winnen, en toetst of dat te kopiëren is:

1. Posities per wallet en token reconstrueren (pump-fee meegerekend). Posities zonder verkoop tellen verlies mee, papieren winst niet.
2. Per wallet: winkans, winst, winst zonder beste trade, houdtijd en type (dev, hoogfrequente bot, vroege houder, scalper, swing).
3. Overrendement: elke positie tegen vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap), zodat "vroeg in een stijgende markt" niet als talent telt.
4. Geluk-toets: echte toppers tegen toppers na willekeurig husselen (corrigeert voor het testen van duizenden wallets).
5. Persistentie: top 20 gekozen op de eerste helft van de periode, gemeten op de tweede helft.
6. Kopieer-simulatie: hun aankopen volgen na 0 / 2 / 10 / 60 s met 0,2 SOL en onze kosten.

Draait via `update.sh` als aparte systemd-taak met lage prioriteit: direct na een nieuwe versie en daarna elke 6 uur. Resultaat staat op de branch `status` als `wallets.md` en `wallets.json`.

Sinds deze versie bewaart de bot alle trades, ook op tokens die nooit $7k halen (uitschakelen met `LOG_ALL_TRADES=0`; stopt vanzelf onder `MIN_FREE_DISK_GB`, standaard 5 GB vrij). Oudere data bevat alleen trades vanaf het moment dat een token $7k haalde.

## Geldstroom per wallet (`ledger.py`)

Houdt bij waar het geld naartoe gaat, over de hele meetperiode. Per wallet per token: hoeveel SOL erin ging (aankopen, incl. pump-fee) en hoeveel eruit kwam (verkopen, na pump-fee). Alleen tokens die ontstonden nadat de bot alle trades ging loggen en die geen herstart overlapten.

- Geldstroom per rol: dev, bundel (kocht in het creatieblok), sniper (≤ 5 s), vroeg (< $7k), laat (≥ $7k), zonder koop (doorgestuurde tokens).
- Concentratie: hoeveel van de winst bij de top 10 / 100 / 1% landt.
- Groeiers: wallets die aan vooraf vastgelegde criteria voldoen (`CRITERIA` in het script). Eenmaal op de lijst worden ze elke run gevolgd.
- Vooruit-toets: wat de koers doet na elke aankoop van een groeier (+1/5/15/60 min) en wat kopiëren oplevert, apart voor aankopen vóór en ná opname in de lijst.

Eigen database `data/ledger.sqlite`, incrementeel bijgewerkt. De bot logt trades tot 6 uur na creatie (`LOG_MAX_AGE_S`); de simulatie stopt zoals voorheen na 1 uur.

## Videostrategie op alle trades (`video_replay.py`)

Speelt de kern van de video na op elk token met volledige geschiedenis: instap op een dip van 40/45/50% vanaf de top (direct, of na 5% herstel), uitstap volgens de video (-3% onder instap of +45%), strikt, of met trailing stop. Splitst naar bundelgrafiek (≥ 2x vóór de eerste verkoop) versus schone grafiek, houdercheck, final-stretch-regels en X-link, en toetst de claim dat een 45%-dip "elke keer" weer 45% herstelt. Resultaten per token worden bewaard; elke run rekent alleen nieuwe tokens.

Alle drie de analyses draaien elke 2 uur via `update.sh` en staan op de branch `status`: `wallets.md`, `ledger.md`, `video_replay.md`.

## Handmatig volgen en herkomst (sinds 11 sept)

- `volg_wallets.txt`: wallets die altijd gevolgd worden, los van de criteria. Per run: netto, winkans, sniper/bundel-aandeel, verloop sinds de eerste meting, en de vooruit-toets op hun aankopen.
- Herkomst: voor verkopen van tokens die een wallet nooit op de curve kocht, zoekt `ledger.py` (max. 40 per run, 2 RPC-calls per seconde) de transactie waarin de tokens binnenkwamen. Zo worden bundel-clusters zichtbaar: afzender plus doorstuurwallets, met hun gezamenlijke netto.
- Houdercheck: bij een RPC-fout probeert de bot het tot twee keer opnieuw en leidt hij anders de top-5 houders af uit de eigen tradestroom. Lukt beide niet, dan wordt het token afgekeurd in plaats van doorgelaten (vanaf `screening_v2_since` in de meta-tabel).
- `video_replay.py` kent later vastgelegde hypothesen (`HYPOTHESEN`), die alleen getoetst worden op tokens van ná het vastleggen.

## Grote spelers (in `ledger.py`)

Van de 2000 meest actieve wallets in de meetperiode haalt de analyse het SOL-saldo op (elke 6 uur, 100 per RPC-call) en toetst of het adres een gewone wallet is of een programma-adres (PDA, zoals een kluis van een botplatform). 'Groot' = ≥ 100 SOL saldo of ≥ 100 SOL verhandeld, met ≥ 10 tokens. Per groot account: profiel (insider, sniper, snelle scalper, scalper, swing), netto, ROI, winkans, houdtijd en consistentie per blok van 6 uur. Het rapport vergelijkt groot met de rest en toont of saldo of volume samenhangt met rendement.

`update.sh` herstart de bot alleen nog als botcode verandert. Wijzigingen in de analyses, documentatie of `volg_wallets.txt` gaan live zonder herstart.

## PumpSwap: de data na migratie (`pumpswap.py`, sinds 12 sept)
Zodra een token migreert, stopt de bonding curve en stopt onze data. Daardoor stond er in het
ledger een groot bedrag "open" waarvan we niet wisten of het winst of verlies werd. Twee sporen:

1. **`pumpswap.py na_migratie`** — beantwoordt de vraag zonder kennis van de event-layout.
   Voor open posities in gemigreerde tokens halen we het huidige tokensaldo van de wallet op:
   leeg = ze zijn eruit (er is dus ná migratie verkocht), nog vol = ze zitten er nog in. De
   poolprijs leiden we generiek af (grootste tokenaccount → eigenaar = pool → WSOL-saldo van
   die pool), zonder aannames over het programma. Gevolgde wallets gaan voor; daarna de
   grootste bedragen. Wat we hiermee **niet** weten is de opbrengst in SOL.
2. **`pumpswap.py probe`** — verificatie vóór ingestie. We raden de layout niet: per transactie
   weten we uit pre/post-balansen wat er werkelijk van eigenaar wisselde, en daarna zoeken we op
   welke offset die bedragen in de eventbytes staan. Een offset geldt pas als vastgesteld bij
   ≥ 95% match over ≥ 50 transacties. Alleen dan komt er een `data/pumpswap_layout.json`.
   De probe kijkt zowel naar `Program data:`-logregels als naar binnenste instructies
   (`emit_cpi!`); dat verschil bepaalt of de websocket-logstream de bedragen kan zien.

De bot kijkt elke 5 minuten of dat bestand er is (`_amm_gate`). Zo ja én staan de bedragen in de
logs, dan start hij een tweede logstream op het AMM-programma en schrijft hij naar `amm_trades`.
Ontbreekt het bestand, of staan de bedragen alleen in `emit_cpi`, dan gebeurt er niets: liever
geen data dan verkeerd gedecodeerde data. Er is geen herstart nodig om dit aan te zetten.

## Uitstapregels op dezelfde aankopen (in `ledger.py`, sinds 12 sept)
De vooruit-toets vergelijkt nu tien uitstapregels op exact dezelfde instapmomenten: volgen,
videoregel, winst nemen op +20/+30/+50% (stop −15%, horizon 15 min), hard uit na 15/30/60/180 s,
en trailing (−10% of 20% onder de piek). Aanleiding: de koers na een groeier-aankoop stijgt
gemiddeld sterk binnen 15 minuten (max +216%) maar staat na 15 minuten mediaan −55%. Dat ziet
eruit als een uitstapprobleem; deze tabel toetst of dat zo is. Zelfde n, zelfde aankopen, alleen
een ander moment van verkopen — verschillen komen dus alleen van de uitstapregel.

## Register van vroege kopers (in `ledger.py`, sinds 12 sept)
De enige groep met een positieve mediaan is wie er vóór $7k in zit. Die groep is per definitie
niet te kopiëren. Daarom een andere toets: wallets met ≥ 15 tokens waarin ze binnen 30 s na
creatie kochten, winkans ≥ 55%, netto plus en dev-aandeel ≤ 5% komen in een register
(`vroegkopers-v1`). Per token tellen we hoeveel registerwallets vroeg kochten — en alleen
wallets die er al vóór de creatie van dat token op stonden, anders kijk je vooruit met kennis
van later. Instap 2 s na het $7k-moment, dus op het eerste moment dat wij zouden kunnen handelen.
Als tokens met 2 of 3+ registerwallets structureel beter uitpakken dan tokens met nul, is dat een
signaal dat wél op tijd beschikbaar is. Zo niet, dan is ook deze route dood en kunnen we de hele
"volg de slimme wallets"-lijn sluiten.
